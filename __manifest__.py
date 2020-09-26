# -*- coding: utf-8 -*-
{
    'name': "Library Managment system",

    'summary': "A custom library management library for learning odoo development addons",

    'description': """
        Long description of module's purpose
    """,

    'author': "MAONO",
    'website': "http://www.new.maono.co",
    'application':True,
    'installable':True,
    'auto-install':True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
