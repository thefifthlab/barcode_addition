from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    import_barcode = fields.Char(
        string='Import Barcode'
    )

    @api.onchange('import_barcode')
    def _onchange_import_barcode(self):
        if self.import_barcode:
            product = self.env['product.product'].search(
                [('barcode', '=', self.import_barcode)],
                limit=1
            )
            self.product_id = product