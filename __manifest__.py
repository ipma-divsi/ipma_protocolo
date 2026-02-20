# -*- coding: utf-8 -*-
{
    'name': 'IPMA Protocolos',
    'version': '17.0.1.0.0',
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
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        
        # Data
        # 'data/sequences.xml',
        # 'data/equipment_categories.xml',
        # 'data/mail_templates.xml',  
        # 'data/cron_jobs.xml',
        # 'data/report_paperformat.xml',
        
        # Views
        'views/ipma_protocolos_views.xml',
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