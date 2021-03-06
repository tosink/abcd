# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.



from odoo import api, fields, models, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sale_id = fields.Many2one(related="group_id.sale_id", string="Sales Order", store=True, readonly=False)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    picking_ids = fields.One2many('stock.picking', 'sale_id', string='Transfers')


class ProcurementGroup(models.Model):
    _inherit = 'procurement.group'

    sale_id = fields.Many2one('sale.order', 'Sale Order')


    @api.model
    def create(self, values):
        if 'name' in values:
            order = self.env['sale.order'].sudo().search([('name','=',values['name'])], limit=1)
            if order:
                values['sale_id'] = order.id
        return super(ProcurementGroup, self).create(values)

