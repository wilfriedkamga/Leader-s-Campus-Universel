from odoo import _, api, fields, models, tools
from odoo.exceptions import UserError


class Registration(models.Model):
    _name = 'campus_universel.registration'
    _description = 'Suivi et traitement des procédures de voyages'
    _table='cu_registration'

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
    procedure_id = fields.Many2one(
        'campus_universel.procedure',
        string='Procedure',
        )
    
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
    def action_print_registration(self):
        # Le rapport peut maintenant être généré pour l'enregistrement spécifique
        return True
    
    def action_create_treatment(self):
        self.ensure_one()  # Vérifie qu'un seul enregistrement est sélectionné

        if not self.procedure_id:
            raise UserError(_("Aucune procédure associée à cet enregistrement."))

        # 🔹 Création du traitement
        treatment = self.env['campus_universel.traitement'].create({
            'name': self.name,
            'last_name': self.last_name,
            'num_reg': self.num_reg,
            'photo': self.photo,
            'birthday': self.birthday,
            'nationality': self.nationality,
            'passport_number': self.passport_number,
            'passport_issue_date': self.passport_issue_date,
            'passport_expiry_date': self.passport_expiry_date,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'father_name': self.father_name,
            'father_profession': self.father_profession,
            'father_contact': self.father_contact,
            'mother_name': self.mother_name,
            'mother_profession': self.mother_profession,
            'mother_contact': self.mother_contact,
            'client_manager_name': self.client_manager_name,
            'client_manager_contact': self.client_manager_contact,
            'desired_country': self.desired_country,
            'desired_school': self.desired_school,
            'comments': self.comments,
            'procedureName': self.procedure_id.name,
            'description': self.procedure_id.description,
            'registration_amount': self.registration_amount,
            'secretary_payment': self.secretary_payment,
            'cashier_validation': self.cashier_validation,
            'amount_min': self.procedure_id.amount_min,
            'amount_max': self.procedure_id.amount_max,
            'pays_id': self.procedure_id.pays_id.id,
            'color': self.procedure_id.color,
            'gender': self.gender,
            'info_source': self.info_source,
            'study_level': self.study_level,
            'travel_purpose': self.travel_purpose,
            'state': 'new',  # Démarre avec le statut "En traitement"
        })

        # 🔹 Copie des étapes de la procédure dans le traitement
        etape_vals = []
        for etape in self.procedure_id.etape_ids:
            etape_vals.append({
                'name': etape.name,
                'description': etape.description,
                'procedure_id': treatment.id,  # L'étape est liée au traitement créé
                'state': etape.state,
            })

        if etape_vals:
            self.env['campus_universel.procedure.etape'].create(etape_vals)

        # 🔹 Copie des documents de la procédure dans le traitement
        document_vals = []
        for document in self.procedure_id.document_ids:
            document_vals.append({
                'name': document.name,
                'procedure_id': treatment.id,  # Lier les documents au traitement
                'document_type': document.document_type,
                'mandatory': document.mandatory,
            })

        if document_vals:
            self.env['campus_universel.procedure.document'].create(document_vals)

        return {
            'type': 'ir.actions.act_window',
            'name': 'Traitement',
            'res_model': 'campus_universel.traitement',
            'view_mode': 'form',
            'res_id': treatment.id,
            'target': 'current',
        }

    

    