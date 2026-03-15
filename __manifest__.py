# -*- coding: utf-8 -*-
{
    'name': "Cherry Land Development",

    'summary': "Cherry Land Project",

    'description': """
Cherry Land Project Development
    """,

    'author': "ARI",
    'sequence': '1',
    'website': "https://arimm.io/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'account_asset', 'analytic'],

    # always loaded
    'data': [
        # Security
        'security/ir.model.access.csv',

        # Data

        # Actions
        'views/action.xml',

        # Menus
        'views/menu.xml',

        # Search
        'views/search.xml',

        # Views
        'views/cl_asset.xml',
        'views/cl_product.xml',
        'views/cl_contact.xml',
        'views/cl_account_move.xml',
        'views/cl_account_account.xml',
        'views/cl_account_tax.xml',
        'views/cl_account_integration.xml',
        'views/cl_account_journal.xml',
        'views/cl_account_integration_line.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
