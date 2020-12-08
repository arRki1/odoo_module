# -*- coding: utf-8 -*-

{
    'name': 'Odoo 13 Budget Management',
    'author': 'arRki1',
    'category': 'Accounting',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'security/account_budget_security.xml',
        'views/account_analytic_account_views.xml',
        'views/account_budget_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'demo': ['data/account_budget_demo.xml'],
}
