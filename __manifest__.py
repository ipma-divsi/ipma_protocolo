# -*- coding: utf-8 -*-
{
    'name': 'IPMA Protocolos',
    'version': '17.0.1.1.0',
    'category': 'Protocolos',
    'summary': '',
    'description': '''
        IPMA Protocolos - 
        =========================================================
    ''',
    'author': 'IPMA - Lucas Dias',
    'website': 'https://www.ipma.pt',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'auth_ldap',
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        
        # Data
        'data/groups.xml',

        # Views
        'views/ipma_protocolos_views.xml',
        'views/ipma_ata_views.xml',
        'views/ipma_addendum_views.xml',
        'views/ipma_menu_view.xml',
        
        # Wizards
        'wizards/ipma_import_protocolos_wizard.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    # 'images': ['static/description/Banner.png'],
}