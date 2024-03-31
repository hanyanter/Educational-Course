{
    'name': "Courses",
    'author': "Eng. Hany Antar Hassan",
    'category': "Educational",
    'version': "17.0.0.1.0",
    'description': """This module made to save the main
    information about Educational Institute""",
    'depends': ['base', 'mail', 'hr', 'om_account_accountant', 'account',
                ],
    'data': [
        # 'security/res_group.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/base_menu.xml',
        'views/teacher_accrual.xml',
        'views/course.xml',
        'views/session.xml',
        'views/subject.xml',
        'views/stage.xml',
        'views/account_edit_inherit.xml',
    ],
    'assets': {'web.assets_backend': ['course/static/src/css/course.css']},
    'application': True
}
