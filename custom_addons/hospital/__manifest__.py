# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital Solution',
    'version': '1.0.0',
    'sequence': -100,
    'author': 'Sijan Shrestha',
    'category': 'Hospital',
    'summary': 'Hospital Management System',
    'description': """
This module contains all the  features of Hospital Management.
    """,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
