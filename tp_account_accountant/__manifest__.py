# -*- coding: utf-8 -*-

{
    'name': 'TP Accounting',
    'category': 'Accounting',
    'sequence': '8',
    'author': 'arRki1',
    'depends': ['accounting_pdf_reports', 'tp_account_asset', 'tp_account_budget'],
    'demo': [],
    'data': [
        'wizard/change_lock_date.xml',
        'views/account.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
