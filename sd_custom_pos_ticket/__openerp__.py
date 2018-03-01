{
    'name': 'SDatos Custom POS Ticket',
    'version': '0.2',
    'category': 'Point Of Sale',
    'sequence': 6,
    'summary': 'Custom pos ticket',
    'description': """
Custom pos ticket
=================


    """,
    'author': 'Sistemas de Datos S.L',
    'depends': ['report',
                'point_of_sale',
                'l10n_es_pos'],
    'data': ['reports/inherit_pos.xml',
             'reports/invoice_report.xml'],
    'installable': True,
    'application': False,
    'qweb': [],
    'website': 'https://www.odoo.com/page/point-of-sale',
    'auto_install': False,
}