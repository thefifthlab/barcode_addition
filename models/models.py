from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    barcode = fields.Char(related='product_id.barcode', string='Barcode/ISBN', store=True)


class StockMove(models.Model):
    _inherit = 'stock.move'

    barcode = fields.Char(related='product_id.barcode', string='Barcode/ISBN', store=True)


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    barcode = fields.Char(related='product_id.barcode', string='Barcode/ISBN', store=True)


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    barcode = fields.Char(related='product_id.barcode', string='Barcode/ISBN', store=True)


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    barcode = fields.Char(related='product_id.barcode', string='Barcode/ISBN', store=True)

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    barcode = fields.Char(
        related='product_id.barcode',
        string='Barcode/ISBN',
        store=True,
        readonly=True
    )
    barcode_name = fields.Char(
        string='Barcode Name',
        compute='_compute_barcode_name',
        store=True,
        readonly=True
    )

    @api.depends('product_id.barcode', 'product_id.display_name')
    def _compute_barcode_name(self):
        for record in self:
            product = record.product_id
            if product:
                barcode = product.barcode
                if barcode:
                    record.barcode_name = f"[{barcode}] {product.display_name}"
                else:
                    record.barcode_name = product.display_name
            else:
                record.barcode_name = False
