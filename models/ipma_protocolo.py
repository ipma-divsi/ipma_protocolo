from dateutil.relativedelta import relativedelta

from odoo import models, fields, api
from odoo.exceptions import UserError

class Protocolo(models.Model):
    _name = 'ipma.protocolo'
    _description = 'Protocolo Model'

    siged = fields.Char(string='SIGED')
    tipo_documento = fields.Char(string='Tipo de documento')
    ambito_geografico = fields.Char(string='Âmbito geográfico')
    entidades_signatarias = fields.Char(string='Entidades signatárias')
    classificacao_entidades = fields.Char(string='Classificação da(s) entidade(s)')
    designacao_documento = fields.Char(string='Designação do documento')
    sigla = fields.Char(string='Sigla')
    ambito_objeto = fields.Text(string='Âmbito / Objeto')
    data_assinatura = fields.Date(string='Data de assinatura') # Validar
    entrada_vigor = fields.Date(string='Entrada em vigor') # Validar
    data_vigencia = fields.Date(string='Data de Vigência') # Validar
    periodo_vigencia = fields.Char(string='Período de Vigência')
    antecedencia_revisao_denuncia = fields.Char(string='Antecedência para revisão e denúncia')
    obrigacoes_financeiras = fields.Text(string='Obrigações financeiras')
    valor = fields.Float(string='Valor')
    ponto_focal_ipma_nome = fields.Char(string='Ponto Focal IPMA - Nome')
    ponto_focal_ipma_uo = fields.Char(string='Ponto Focal IPMA - UO')
    ponto_focal_ipma_tlf = fields.Char(string='Ponto Focal IPMA - Tlf.')
    ponto_focal_ipma_email = fields.Char(string='Ponto Focal IPMA - email')
    ponto_focal_parceiros_nome = fields.Char(string='Ponto Focal (parceiros) - Nome')
    ponto_focal_parceiros_tlf = fields.Char(string='Ponto Focal (parceiros) - Tlf.')
    ponto_focal_parceiros_email = fields.Char(string='Ponto Focal (parceiros) - email')
    outros_protocolos_mesmas_entidades = fields.Text(string='Outros protocolos com a(s) mesma(s) entidade(s)')
    numero_documento_relacionado = fields.Char(string='N.º Documento Relacionado')
    ativo = fields.Boolean(string='Ativo', default=True)
    observacoes = fields.Text(string='Observações')
    vigencia_prestes_expirar = fields.Boolean(
        string='Vigência a expirar',
        compute='_compute_vigencia_prestes_expirar',
    )
    
    ata_ids = fields.One2many('ipma.ata', 'protocolo_id', string='Atas Relacionadas')
    addendum_ids = fields.Many2many('ipma.addendum', 'protocolo_id', string='Addendos')

    # Red Line for records with vigencia_prestes_expirar eas about to expired in 1 month tree view
    @api.depends('data_vigencia')
    def _compute_vigencia_prestes_expirar(self):
        today = fields.Date.context_today(self)
        limite = today + relativedelta(months=1)
        for record in self:
            if record.data_vigencia:
                record.vigencia_prestes_expirar = today <= record.data_vigencia <= limite
            else:
                record.vigencia_prestes_expirar = False