# -*- coding: utf-8 -*-
{
    'name': 'IPMA Protocolos',
    'version': '17.0.1.1.0',
    'category': 'Protocolos',
    'summary': 'Gestão completa de protocolos interadministrativos do IPMA',
    'description': '''
        IPMA Protocolos - Sistema de Gestão de Protocolos
        ==================================================
        
        Funcionalidades principais:
        * Gestão centralizada de protocolos interadministrativos
        * Registro e rastreabilidade de atas e aditivos
        * Autenticação integrada com LDAP corporativo
        * Controlo de acesso baseado em funções
        * Workflow de aprovação e validação
        * Análise de datas de vigência
        * Gestão de observações e documentação
        * Importação em lote de protocolos
        * Relatórios e exportações em Excel
        * Auditoria completa de alterações
        
        Módulo desenvolvido especificamente para o IPMA - Instituto Português do Mar e da Atmosfera
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
    'images': ['static/description/Banner.png'],
}