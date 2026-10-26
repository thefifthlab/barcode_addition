{
    'name': 'Line Item ISBN Display',
    'version': '18.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Display product ISBN next to product name in Sales, Stock, Purchase, and Invoice lines',
    'description': """
        This module adds a ISBN field directly next to the product field in lines
        Also Adds a barcode field to invoices for Excel import
    """,
    'author': '',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'stock',
        'purchase',
        'account',
        'sale_stock',
        'purchase_stock'
    ],
    'data': [
        'views/views.xml',
        'views/account_move_views.xml',
        # 'data/action.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
