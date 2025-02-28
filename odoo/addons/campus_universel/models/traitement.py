from odoo import _, api, fields, models, tools
import logging

_logger = logging.getLogger(__name__)

class Traitement(models.Model):
    _name = 'campus_universel.traitement'
    _description = ''
    _table='cu_traitement'
    
    # ATTRIBUTS SIMPLES
    mat = fields.Char(string=' ')
    name = fields.Char(string='Nom')
    last_name = fields.Char(string='Prénom')
    photo = fields.Binary(string='Photo')
    birthday = fields.Date(string="Date de naissance")
    nationality = fields.Char(string="Nationalité")
    passport_number = fields.Char(string="Numéro de passeport")
    passport_issue_date = fields.Date(string="Date de délivrance du passeport")
    passport_expiry_date = fields.Date(string="Date d'expiration du passeport")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Téléphone")
    address = fields.Text(string="Adresse complète")
    father_name = fields.Char(string="Nom du père")
    father_profession = fields.Char(string="Profession du père")
    father_contact = fields.Char(string="Contact du père")
    mother_name = fields.Char(string="Nom de la mère")
    mother_profession = fields.Char(string="Profession de la mère")
    mother_contact = fields.Char(string="Contact de la mère")
    client_manager_name = fields.Char(string="Nom du gestionnaire client")
    client_manager_contact = fields.Char(string="Contact du gestionnaire client")
    desired_country = fields.Char(string="Pays de destination")
    desired_school = fields.Char(string="Établissement souhaité")
    comments = fields.Text(string="Remarques / Informations complémentaires")
    procedureName = fields.Char(string='Nom de la procédure')
    description = fields.Char(string='Description')
    registration_amount = fields.Float(
        string="Montant pour l'enregistrement",
        readonly=True, 
        default=50000
    )
    secretary_payment = fields.Float(string="Montant versé à la caissière")
    cashier_validation = fields.Boolean(string="Validation de la caissière", default=False)
    amount_min = fields.Float(string='Montant minimal')
    amount_max = fields.Float(string='Montant maximal')
    flag = fields.Binary(string='Drapeau', store=True)
    color = fields.Integer(string="Couleur")

    # 🟡 CHAMPS DE SÉLECTION
    gender = fields.Selection([
        ('male', 'Masculin'), 
        ('female', 'Féminin'), 
        ('other', 'Autre')
    ], string="Genre")

    info_source = fields.Selection([
        ('website', 'Site Internet'),
        ('youtube', 'YouTube'),
        ('facebook', 'Facebook'),
        ('word_of_mouth', 'D’un particulier'),
        ('client_manager', 'Un gestionnaire client')
    ], string="Comment avez-vous entendu parler de nous ?")

    study_level = fields.Selection([
        ('high_school', 'Baccalauréat'),
        ('bachelor', 'Licence'),
        ('master', 'Master'),
        ('phd', 'Doctorat'),
        ('other', 'Autre')
    ], string="Niveau d’études")

    travel_purpose = fields.Selection([
        ('study', 'Études'),
        ('work', 'Travail'),
        ('tourism', 'Tourisme'),
        ('family', 'Regroupement familial'),
        ('other', 'Autre')
    ], string="Motif du voyage")

    state = fields.Selection([
        ('new', 'En traitement'), 
        ('late', 'En attente'), 
        ('cancel', 'Annulée')
    ], string='Statut du traitement')

    # 🔵 RELATIONS
    etape_reel_ids = fields.One2many(
        'campus_universel.traitement.etape_reel',
        'traitement_id',
        string='Étapes',
        )


    # 🔴 FONCTIONS
    


    def test_action(self):
        """Fonction de test"""
        print('Bonjour')
    
    @api.model
    def create(self, vals):
        new_seq = self.env['ir.sequence'].next_by_code('cu.traitement.sequence')
        vals['mat'] = new_seq
        return super(Traitement, self).create(vals)
    
    def create_treatment_with_steps(self):
        treatment_name='TEst de la création automatique avec les étapes'
        treatment = self.create({'name': treatment_name})
        phase_initiale = self.env['campus_universel.traitement.phase_reel'].create({
        'name': 'Préparation initiale'
    })
        phase_finale = self.env['campus_universel.traitement.phase_reel'].create({
        'name': 'Préparation finale'
    })
        steps_data = [
        {'name': 'Collecte des documents', 'phase_reel_id': phase_initiale.id, 'traitement_id': treatment.id},
        {'name': 'Vérification des documents', 'phase_reel_id': phase_initiale.id, 'traitement_id': treatment.id},
        {'name': 'Validation finale', 'phase_reel_id': phase_finale.id, 'traitement_id': treatment.id},
        {'name': 'Envoi des documents', 'phase_reel_id': phase_finale.id, 'traitement_id': treatment.id},
    ]
        for step in steps_data:
            self.env['campus_universel.traitement.etape_reel'].create(step)

        return treatment
   
   
    

