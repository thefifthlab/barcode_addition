from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    barcode = fields.Char(
        string='Barcode',
        copy=False,
        index=True,
        help="Barcode associated with this invoice."
    )
    customer_code = fields.Char(
        string='Customer Code',
        copy=False,
        index=True,
        help="Code or reference number for the customer."
    )