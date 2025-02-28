{
    'name' : 'Campus Universel',
    'version' : '1.0',
    'summary': 'Traitement et suivi des procédures de voyage2.',
    'sequence': 10,
    'description': "Gérer les procédures de voyages de l'ouverture du dossier jusqu'au voyage.",
    'author':"Wilfried",
    'category': '',
    'website': 'https://www.wifriju.com',
    'depends': ['base','base_setup'],
    'data': [
      
        'security/ir.model.access.csv',
        'data/cu_trait_sequence.xml',
        'views/cu_traitement_etape_reel_view.xml',
        'views/cu_traitement_phase_reel_view.xml',
        'views/cu_procedure_phase_view.xml',
        'views/cu_procedure_pays_view.xml',
        'views/cu_procedure_cible_view.xml',
        'views/cu_procedure_payment_mode_view.xml',
        'views/cu_procedure_payment_method_view.xml',
        'views/cu_procedure_payment_operation_view.xml',
        'views/cu_transaction_view.xml',
        'views/cu_traitement.xml',
        'views/cu_procedure_etape_view.xml',
        'views/cu_procedure_phase_view.xml',
        'views/cu_procedure_view.xml',
        'views/cu_registration.xml',
        'views/cu_menu_view.xml', 
    ],

    'assets': {

    'web.assets_backend': [
        'campus_universel/static/src/css/custom_styles.css',
        'campus_universel/static/src/css/dashboard.css',
        'campus_universel/static/src/js/dashboard.js',
        'campus_universel/static/src/xml/dashboard.xml'],
},
   
    'auto_install':False,
    'application': True,
    'installable': True,
    'license': 'OEEL-1',
    
}
