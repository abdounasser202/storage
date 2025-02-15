# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Storage Media",
    "summary": "Give the posibility to store media data in Odoo",
    "version": "14.0.2.2.0",
    "category": "Uncategorized",
    "website": "https://github.com/OCA/storage",
    "author": " Akretion, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    "depends": ["storage_file", "storage_thumbnail"],
    "data": [
        "wizards/replace_file.xml",
        "views/storage_media_view.xml",
        "data/ir_parameter.xml",
        "security/res_group.xml",
        "security/ir_rule.xml",
        "security/ir.model.access.csv",
    ],
    "demo": [],
    "qweb": [],
}
