# -*- coding: utf-8 -*-
{
    'name': "invoice_auto_analytic_account",
    'version': '13.0',

    'summary': """
        This module will add a analytic account field in invoices (account.move), which can auto-fill all the analytic account in 
        all the invoice lines (account.move.lines). """,

    'description': """
        This module will add a analytical account field in invoices, which can auto-generate analytical account in 
        all the invoice lines. 
    """,

    'author': "Tradetec Info Pvt Ltd.",
    'website': "https://www.tradetec.info",

    'category': 'Invoicing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'analytic'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ]
}
