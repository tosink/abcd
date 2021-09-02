# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.



from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    picking_ids = fields.One2many('stock.picking', 'sale_id', string='Transfers')


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sale_id = fields.Many2one(related="group_id.sale_id", string="Sales Order", store=True, readonly=False)