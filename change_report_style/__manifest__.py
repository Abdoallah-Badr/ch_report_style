# -*- coding: utf-8 -*-
{
    'name': "Edit company Options",
    'author': "Upward co.",
    'version': '17.0',
    'depends': ['base','account','l10n_gcc_invoice','l10n_sa'],

    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'reports/upward_invoice_report.xml',
        'views/change_style_view.xml'
    ],

    'installable': True,
}
