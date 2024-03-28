{
    'name':'Qualiopi',
    'author':'Ithar',
    'category': 'Tools',
    'description': """
    Qualiopi Elearning
    """,
    'depends': ['base','website',],
    'data': [
        'views/qualiopi.xml',
        'views/templates.xml',
        
    
        
     ],
    'assets': {

    'web.assets_frontend': [
        'qualiopi/static/src/css/custom.css',
    ],

    },
    
    'installable': True,
    'application': True,
}