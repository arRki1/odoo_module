# -*- coding: UTF-8 -*-

from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
import logging
import time
from datetime import timedelta, datetime

_logger = logging.getLogger(__name__)

class PurchaseStage(models.Model):
    _name = "purchase.stage"
    _description = "Purchase Stage"
    _order = 'sequence, id'
    _check_company_auto = True

    name = fields.Char('Purchase Stage', required=True, translate=True)
    color = fields.Integer('Color')
    sequence = fields.Integer('Sequence', help="Used to order the 'All Opesrations' kanban view")
    code = fields.Selection([('wait_rfq', 'Wait RFQ'), ('wait_confirm', 'Wait Confirm'), ('wait_wh', 'Wait Warehousing'), 
        ('wait_pay', 'Wait Pay'), ('refund', 'Refund')], 
        string='code', required=True)
    cnt_wait_rfq = fields.Integer(compute='_compute_wait_count')
    cnt_wait_confirm = fields.Integer(compute='_compute_wait_count')
    cnt_wait_wh = fields.Integer(compute='_compute_wait_count')
    cnt_wait_pay = fields.Integer(compute='_compute_wait_count')
    cnt_receive_delay = fields.Integer(compute='_compute_wait_count')
    cnt_has_refund_reconcilation = fields.Integer(compute='_compute_wait_count')
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company.id)

    def _compute_wait_count(self):
        PO = self.env['purchase.order']
        self.cnt_wait_rfq = PO.search_count([('state', '=', 'draft')])
        self.cnt_wait_confirm = PO.search_count([('state', '=', 'sent')])
        self.cnt_wait_wh = PO.search_count([('is_shipped', '=', False), ('state', 'in', ['purchase', 'done']), 
            ('picking_count', '!=', 0)])
        self.cnt_wait_pay = PO.search_count([('state', 'in', ['purchase', 'done']), 
            ('invoice_status', 'not in', ['no', 'invoiced'])])
        self.cnt_receive_delay = PO.search_count([('date_planned', '<', time.strftime(DEFAULT_SERVER_DATETIME_FORMAT)), 
            ('is_shipped', '=', False), ('state', 'in', ['purchase', 'done']), 
            ('picking_count', '!=', 0)])
        self.cnt_has_refund_reconcilation = PO.search_count([('state', 'in', ['purchase', 'done']), 
            ('has_refund_reconcilation', '=', True)])
            