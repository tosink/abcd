# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sales and Warehouse Management',
    'version': '1.1',
    'category': 'Hidden',
    'summary': 'Quotation, Sales Orders, Delivery & Invoicing Control',
    'description': """
Manage sales quotations and orders
==================================

This module makes the link between the sales and warehouses management applications.

Preferences
-----------
* Shipping: Choice of delivery at once or partial delivery
* Invoicing: choose how invoices will be paid
* Incoterms: International Commercial terms

""",
    'depends': ['sale', 'stock_account'],
    'data': [
        'views/report_invoice.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
