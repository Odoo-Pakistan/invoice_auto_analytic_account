# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account', ondelete='set null')

    @api.onchange('analytic_account_id')
    def _onchange_analytic_account_id(self):

        # update all the lines if changed
        for line in self.line_ids:
            line.analytic_account_id = self.analytic_account_id

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    @api.onchange('product_id')
    def _onchange_product_id(self):
        super(AccountMoveLine, self)._onchange_product_id()

        for line in self:
            line.analytic_account_id = line.move_id.analytic_account_id


