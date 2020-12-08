# -*- coding: UTF-8 -*-

{
    'name': 'TP Purchase',
    'description': 'TP Purchase',
    'author': 'arRki1',
    'depends': ['base', 'purchase', 'stock', 'account'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'data/purchase_stage.xml',
        'views/overview.xml',
        'views/menu.xml',
    ]
}