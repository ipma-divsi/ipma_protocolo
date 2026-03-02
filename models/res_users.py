from odoo import models


class ResUsers(models.Model):
    _inherit = 'res.users'

    def _auth_ldap(self, password):
        """Override LDAP authentication to auto-assign read-only group to new LDAP users."""
        user_id, credentials = super()._auth_ldap(password)
        
        # If authentication succeeded and we have a user
        if user_id:
            user = self.browse(user_id)
            # Get the LDAP read-only group
            ldap_readonly_group = self.env.ref(
                'ipma_protocolo.group_ldap_readonly',
                raise_if_not_found=False
            )
            
            if ldap_readonly_group:
                # Check if user doesn't already have the group
                if ldap_readonly_group not in user.groups_id:
                    # Add user to LDAP read-only group
                    user.groups_id = [(4, ldap_readonly_group.id)]
        
        return user_id, credentials
