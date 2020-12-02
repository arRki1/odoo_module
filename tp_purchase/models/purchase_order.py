# -*- coding: UTF-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_shipped = fields.Boolean(compute="_compute_is_shipped", store=True)
    has_refund_reconcilation = fields.Boolean(compute="_compute_has_refund_reconcilation", store=True)

    @api.depends('order_line.qty_over_billed')
    def _compute_has_refund_reconcilation(self):
        for order in self:
            has_refund_reconcilation = False
            for line in order.order_line:
                if line.qty_over_billed > 0:
                    has_refund_reconcilation = True
                    break
            order.has_refund_reconcilation = has_refund_reconcilation


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    qty_over_billed = fields.Float(compute="_compute_qty_over_billed", compute_sudo=True, store=True, digits='Product Unit of Measure')

    @api.depends('qty_invoiced', 'qty_received', 'order_id.state')
    def _compute_qty_over_billed(self):
        for line in self:
            if line.order_id.state in ['purchase', 'done']:
                line.qty_over_billed = line.qty_invoiced - line.qty_received if line.qty_invoiced > line.qty_received else 0.0
            else:
                line.qty_over_billed = 0.0
