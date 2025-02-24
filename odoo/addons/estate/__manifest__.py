{
    'name' : 'Real State',
    'version' : '1.0',
    'summary': 'Gestion de l\'immobilier',
    'sequence': 10,
    'description': "Gérer les procédures de voyages de l'ouverture du dossier jusqu'au voyage.",
    'author':"Wilfried",
    'category': '',
    'website': 'https://www.wifriju.com',
    'depends': ['base','base_setup'],
    'data': [
      
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
        'views/estate_menu_view.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_tag_view.xml',
        'views/res_users_view.xml'
        
    ],
   
    'auto_install':False,
    'application': True,
    'installable': True,
    'license': 'OEEL-1',
    
}
