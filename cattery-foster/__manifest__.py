# -*- coding: utf-8 -*-
{
    'name': "cattery-foster",

    'description': """
        Manage the foster process of cattery's rescue kittens
    """,

    'author': "Phamorphosis",
    'website': "https://www.odoo-optimo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'cattery', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/cattery_foster_message_view.xml',
        'views/cattery_foster_parent_views.xml',
        'views/cattery_kitten_views.xml',
        # 'views/cattery_foster_stage_views.xml',
        # 'data/cattery_foster_stage.xml',
        'views/cattery_foster_menu.xml',
    ],
    
    'license': 'LGPL-3',
}

