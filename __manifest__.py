{
    "version": "1.0",
    "name": "qualiopi workflow",
    "category": "Human Resources",
    "author": "ithar",
    "summary": "",
    "description": "",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/workflow.xml",
    ],
    'assets': {

    'web.assets_frontend': [
        'workflow/static/src/css/custom.css',
    ],

    },
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}
