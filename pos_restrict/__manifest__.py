# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'POS Restriction',
    'version': '1.0',
    'summary': 'Custom Hidden Button in Point of Sale',
    'sequence': 10,
    'description': """ """,
    'category': '',
    'website': 'https://odoo-optimo.com',
    'depends': ['point_of_sale'],
    'license': 'LGPL-3',
    'data': [
        "xml/view.xml"
    ],
    'assets': {
        'point_of_sale.assets': [
            "wb_pos_restrict/static/src/js/sample_button.js",
            "wb_pos_restrict/static/src/xml/sample_button.xml"
        ]
    }
}
