{
    'name' : 'Campus Universel',
    'version' : '1.0',
    'summary': 'Traitement et suivi des procédures de voyage2.',
    'sequence': 10,
    'description': "Gérer les procédures de voyages de l'ouverture du dossier jusqu'au voyage.",
    'author':"Wilfried",
    'category': '',
    'website': 'https://www.wifriju.com',
    'depends': ['base','base_setup','mail'],
    'data': [
        
        'security/ir.model.access.csv',
        'security/groups.xml',
        'data/cu_trait_sequence.xml',
        'views/cu_procedure_phase_view.xml',
        'views/cu_procedure_pays_view.xml',
        'views/cu_procedure_cible_view.xml',
        'views/cu_procedure_payment_mode_view.xml',
        'views/cu_procedure_payment_method_view.xml',
        'views/cu_procedure_payment_operation_view.xml',
        'views/cu_transaction_view.xml',
        'views/cu_procedure_etape_view.xml',
        'views/cu_procedure_phase_view.xml',
        'views/cu_procedure_config_view.xml',
        'views/cu_procedure_view.xml',
        'views/cu_procedure_commercial.xml',
        'views/cu_consultation.xml',
        'views/cu_menu_view.xml',
        'report/cu_regisration_report.xml',
        'report/cu_registration_template.xml',
        'report/Procedure/cu_procedure_report.xml',
        'report/Procedure/cu_procedure_template.xml',
        
    ],

    'assets': {

    'web.assets_backend': [
        'campus_universel/static/src/css/custom_styles.css',
        'campus_universel/static/src/css/dashboard.css',
        'campus_universel/static/src/css/registration_report.css',
        'campus_universel/static/src/js/dashboard.js',
        'campus_universel/static/src/xml/dashboard.xml',
        'campus_universel/static/src/scss/campus-kanban.scss'],
},
   
    'auto_install':False,
    'application': True,
    'installable': True,
    'license': 'OEEL-1',
    
}
