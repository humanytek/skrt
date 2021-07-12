# Copyright 2021, Héctor Aguilar
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Base extension Addons for skyalert',
    'summary': 'Module summary',
    'version': '0.0.1',
    'category': 'SkyAlert',
    'website': 'https://odoo-community.org/',
    'author': '<Héctor Aguilar>, Odoo Community Association (OCA)',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    'external_dependencies': {
    },
    'depends': [
        'base',
    ],
    'data': [
        'views/res_partner_view.xml'
    ],
    'demo': [
    ],
    'qweb': [
    ]
}