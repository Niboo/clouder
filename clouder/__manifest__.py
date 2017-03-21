# -*- coding: utf-8 -*-
# Copyright 2015 Clouder SASU
# License LGPL-3.0 or later (http://gnu.org/licenses/lgpl.html).

{
    'name': 'Clouder',
    'version': '10.0.10.0.0',
    'category': 'Clouder',
    'depends': ['base'],
    'author': 'Yannick Buron (Clouder), LasLabs',
    'license': 'LGPL-3',
    'website': 'https://github.com/clouder-community/clouder',
    'demo': [],
    'data': [
        'views/view.xml',
        'views/ir_actions.xml',
        'data/data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'external_dependencies': {
        'python': [
            'libcloud',
            'paramiko',
        ],
    },
    'installable': True,
    'application': True,
}
