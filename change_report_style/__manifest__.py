# -*- coding: utf-8 -*-
{
    'name': "Edit company Options",
    'author': "Upward co.",
    'version': '17.0',
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/external_layout_modified.xml',
        'views/change_style_view.xml',

        'reports/upward_invoice_report.xml',
    ],

    'installable': True,
}
