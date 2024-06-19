# -*- coding: utf-8 -*-
{
    'name': "cattery-caregiver",

    'description': """
        Manage the caregiver process of the cattery's kittens
    """,

    'author': "Phamorphosis",
    'website': "https://www.odoo-optimo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'cattery'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/cattery_menu.xml',
        'views/cattery_caregiver_views.xml',
        'views/cattery_foster_stage_views.xml',
        'data/cattery_foster_stage.xml',
    ],
    
    'license': 'LGPL-3',
}

