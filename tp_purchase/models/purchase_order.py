# -*- coding: UTF-8 -*-

from odoo import models, fields, api

class PurchaseStage(models.Model):
    _inherit = 'purchase.order'

    is_shipped = fields.Boolean(compute="_compute_is_shipped", store=True)
    