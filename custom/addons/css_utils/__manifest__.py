# -*- coding: utf-8 -*-
{
    'name': "css_utils",

    'summary': """
        CSS utility classes for styling""",

    'author': "LIVEPlaza",
    'website': "http://www.liveplaza.online",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'views/frontend_assets.xml',
    ],
}
