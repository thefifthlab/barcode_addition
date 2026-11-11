from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    customer_code = fields.Char(
        string='Customer Code',
        related='partner_id.customer_code',  # Change to partner_id.your_custom_field if needed
        store=True,
        readonly=True
    )

    @api.onchange('partner_id')
    def _onchange_partner_id_customer_code(self):
        self.customer_code = self.partner_id.customer_code or ''
