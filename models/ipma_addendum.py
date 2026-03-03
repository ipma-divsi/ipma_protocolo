from dateutil.relativedelta import relativedelta

from odoo import models, fields, api
from odoo.exceptions import UserError


class Addendum(models.Model):
    _name = 'ipma.addendum'
    _description = 'Addendum Model'

    name = fields.Char(string='Designação do Addendum')
    data_assinatura = fields.Date(string='Data de assinatura')
    entrada_vigor = fields.Date(string='Entrada em vigor')
    data_vigencia = fields.Date(string='Data de Vigência')
    periodo_vigencia = fields.Char(string='Período de Vigência')
    observacoes = fields.Text(string='Observações')
    
    
    protocolo_id = fields.Many2one('ipma.protocolo', string='Protocolos Relacionados')
 