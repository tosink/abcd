# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Lot & Serial by Intelligenti.io',
    'version': '1.5',
    'category': 'Hidden',
    'summary': 'Lot & Serial',
    'description': """
Manage lot and serial numbers
==================================


""",
    'depends': ['sale', 'stock_account'],
    'data': [
        'security/security.xml',
        'views/report_invoice.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
