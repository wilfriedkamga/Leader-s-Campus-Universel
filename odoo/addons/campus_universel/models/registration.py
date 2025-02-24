from odoo import _, api, fields, models, tools

class Registration(models.Model):
    _name = 'campus_universel.registration'
    _description = 'Suivi et traitement des procédures de voyages'

    name = fields.Char(string='Nom')
    last_name = fields.Char(string='Prénom')
    num_reg = fields.Integer(string='Numéro du dossier', readonly=True)
    photo = fields.Binary(string='photo')
    birthday = fields.Date(string="Date de naissance")
    gender = fields.Selection([('male', 'Masculin'), ('female', 'Féminin'), ('other', 'Autre')], string="Genre")
    nationality = fields.Char(string="Nationalité")
    passport_number = fields.Char(string="Numéro de passeport")
    passport_issue_date = fields.Date(string="Date de délivrance du passeport")
    passport_expiry_date = fields.Date(string="Date d'expiration du passeport")

    # Coordonnées
    email = fields.Char(string="Email")
    phone = fields.Char(string="Téléphone")
    address = fields.Text(string="Adresse complète")

    # Informations parentales
    father_name = fields.Char(string="Nom du père")
    father_profession = fields.Char(string="Profession du père")
    father_contact = fields.Char(string="Contact du père")

    mother_name = fields.Char(string="Nom de la mère")
    mother_profession = fields.Char(string="Profession de la mère")
    mother_contact = fields.Char(string="Contact de la mère")

    # Source d'information
    info_source = fields.Selection([
        ('website', 'Site Internet'),
        ('youtube', 'YouTube'),
        ('facebook', 'Facebook'),
        ('word_of_mouth', 'D’un particulier'),
        ('client_manager', 'Un gestionnaire client')
    ], string="Comment avez-vous entendu parler de nous ?")

    client_manager_name = fields.Char(string="Nom du gestionnaire client")
    client_manager_contact = fields.Char(string="Contact du gestionnaire client")
    
    
    # Champs supplémentaires
    study_level = fields.Selection([
        ('high_school', 'Baccalauréat'),
        ('bachelor', 'Licence'),
        ('master', 'Master'),
        ('phd', 'Doctorat'),
        ('other', 'Autre')
    ], string="Niveau d’études")
    
    desired_country = fields.Char(string="Pays de destination")
    desired_school = fields.Char(string="Établissement souhaité")
    travel_purpose = fields.Selection([
        ('study', 'Études'),
        ('work', 'Travail'),
        ('tourism', 'Tourisme'),
        ('family', 'Regroupement familial'),
        ('other', 'Autre')
    ], string="Motif du voyage")

    comments = fields.Text(string="Remarques / Informations complémentaires")
    
    registration_amount = fields.Float(
        string="Montant pour l'enregistrement",
        readonly=True, 
        default=50000  # Montant fixe ou dynamique selon vos besoins
    )
    secretary_payment = fields.Float(
        string="Montant versé à la caissière"
    )
    cashier_validation = fields.Boolean(
        string="Validation de la caissière", 
        default=False
    )

    @api.onchange('info_source')
    def _onchange_info_source(self):
        """ Affiche les champs du gestionnaire client uniquement si l'utilisateur a sélectionné cette source. """
        if self.info_source != 'client_manager':
            self.client_manager_name = False
            self.client_manager_contact = False
    @api.model
    def action_print_registration(self, record):
        # Le rapport peut maintenant être généré pour l'enregistrement spécifique
        return self.env.ref('campus_universel.action_report_registration').report_action(record)

    