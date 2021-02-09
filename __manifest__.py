# -*- coding: utf-8 -*-
{
    'name': "Banco",

    'summary': """
        Modulo para la gestio cuentas, movimientos de un banco""",

    'description': """
       Modulo que permite anañdir, modificar y eliminar cuentas
    """,

    'author': "My Company",
   #se elimina la pagina generada. 
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
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
        'views/view_account.xml',
        'views/view_movement.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}