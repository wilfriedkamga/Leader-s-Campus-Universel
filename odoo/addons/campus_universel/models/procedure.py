from odoo import _, api, fields, models, tools
from datetime import datetime
from odoo.exceptions import ValidationError
import time

class Procedure(models.Model):

    _name = 'campus_universel.procedure'
    _description = 'Suivi et traitement des procédures de voyages'
    _inherit = ['mail.thread', 'mail.activity.mixin'] 
    _table='cu_procedure'
    
    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    cible_ids = fields.Many2many('campus_universel.procedure.cible', string='Cibles')
    payment_mode_id= fields.One2many('campus_universel.procedure.payment_mode','procedure_id', string='Modes de paiment')
    payment_mode_ids= fields.Many2many('campus_universel.procedure.payment_mode','procedure_id', string='Modes de paiment')
    pays_id = fields.Many2one(
        'campus_universel.procedure.pays',
        string='Pays de destination',
        )
    etape_ids = fields.One2many('campus_universel.procedure.etape', 'procedure_id', string='Étapes',ondelete='cascade')
    drapeau_pays = fields.Binary(string='Drapeau', compute='_compute_pays_photo',store=True)
    amount_min = fields.Float(string='Montant minimal')
    amount_max = fields.Float(string='Montant max')
    statut  = fields.Selection([('new', 'Création'), ('actif','Actif'),('block','Bloqué')],default='new', string='Statut')
    statut_trait  = fields.Selection([('actif','En cours de traitement'),('stop','En attente de document'),('block','Suspendu'),('end','terminé'),('cancel','Procédure annulée')],default='actif', string='Statut')
    statut_message = fields.Char(string='Message Statut')
    color = fields.Integer(string="Couleur")
    mat = fields.Char(string=' ')
    name2 = fields.Char(string='Nom')
    last_name = fields.Char(string='Prénom')
    photo = fields.Binary(string='Photo')
    birthday = fields.Date(string="Date de naissance")
    opened_date = fields.Date(string="Date d\' ouverture")
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
    progress = fields.Float(string="Progression", compute="_compute_progress", store=True)
    ## information sur le commercial
    commercial_id = fields.Many2one(
        'campus_universel.procedure.commercial',
        string='Commercial',
        )
    client_manager_contact = fields.Char(string="Contact du gestionnaire client")
    desired_country = fields.Char(string="Pays de destination")
    desired_school = fields.Char(string="Établissement souhaité")
    comments = fields.Text(string="Remarques / Exigences supplémentaires")
    etape_count = fields.Integer(string="Nombre d'Étapes", compute="_compute_etape_count")
    nature  = fields.Selection([('template', 'Template'),('record','Record'),('registration','Registration'),('client','Client'),('gest','Gestionnaire Client')])
    state_client = fields.Selection([('prospect', 'Prospect'),('client','Client')], default='prospect')

    info_source = fields.Selection([
        ('website', 'Site Internet'),
        ('youtube', 'YouTube'),
        ('facebook', 'Facebook'),
        ('word_of_mouth', 'D’un particulier'),
        ('client_manager', 'Un gestionnaire client')
    ], string="Comment avez-vous entendu parler de nous ?")

    client_manager_name = fields.Char(string="Nom du gestionnaire client")
    client_manager_contact = fields.Char(string="Contact du gestionnaire client")
    secretary_payment = fields.Float(
        string="Frais d'ouverture du dossier."
    )
    secretary_validation = fields.Boolean(string='Sécrétaire Validation')
    caissiere_validation = fields.Boolean(string='Caissière Validation')
    user_id = fields.Many2one('res.users', string="Utilisateur")

    gest_client_id = fields.Many2one(
        'res.users',
        string='Gestionnaire Client',
        )
    
    agent_id = fields.Many2one(
        'res.users',
        string='Agent de traitement',
        )

    procedure_id = fields.Many2one(
        'campus_universel.procedure',
        string="Sélectionner une procédure",
        domain="[('nature', '=', 'template'),('statut','=','actif')]",
        ondelete='cascade'  # Filtrage dans toutes les vues
    )
    
    consultation_ids= fields.One2many('campus_universel.consultation','procedure_id', string='Consultation')
    
    # Champs supplémentaires
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

    # 📄 Liste des documents de la procédure (récupérés des étapes)
    document_ids = fields.One2many(
        'campus_universel.procedure.document',
        'procedure_id',
        string=' ',
        store=True,
        ondelete='cascade'
    )

     # 📄 Liste des transactions de la procédure (récupérés des étapes)
    transaction_ids = fields.One2many(
        'campus_universel.transaction',
        'procedure_id',
        string='Transactions ',
        ondelete='cascade'
    )

    
    # ✅ Liste des actions de la procédure (récupérées des étapes)
    action_ids = fields.One2many(
        'campus_universel.procedure.action',
        'procedure_id',
        compute='_compute_actions',
        string='Actions de la procédure',
        store=True,
        ondelete='cascade'
    )
    niveau_etude_id = fields.Many2one('campus_universel.procedure.niveau_etude', string='Niveau d\'étude')
    filiere_ids = fields.Many2many('campus_universel.procedure.filiere', string='Filière/Domaine')
    diplome_id = fields.Many2one('campus_universel.procedure.diplome', string='Diplôme')
    motif_voyage_id = fields.Many2one('campus_universel.procedure.motif_voyage', string='Motif de voyage')
    mention_id = fields.Many2one('campus_universel.procedure.mention', string='Mention')

    @api.constrains('filiere_ids')
    def _check_filiere_limit(self):
        for record in self:
            if len(record.filiere_ids)>3:
                raise ValidationError('Vous ne pouvez sélectionner que trois filières au maximum.')
    
    @api.depends('etape_ids.action_ids')
    def _compute_actions(self):
        """Récupère toutes les actions des étapes pour les afficher dans la procédure"""
        for procedure in self:
            all_actions = procedure.etape_ids.mapped('action_ids')
            procedure.action_ids = [(6, 0, all_actions.ids)]
   
    @api.onchange('pays_id')
    def _onchange_pays_id(self):
        if self.pays_id:
            # Si un pays est sélectionné, mettre à jour l'image associée
            self.drapeau_pays = self.pays_id.flag
        else:
            # Si aucun pays n'est sélectionné, laisser la photo vide
            self.drapeau_pays = False
    def activate_procedure(self):
        for record in self: 
            record.statut='actif'

    def _compute_etape_count(self):
        for record in self:
            record.etape_count = len(record.etape_ids)
    def creation_procedure(self):
        for record in self: 
            record.statut='new'   
    def block_procedure(self):
        for record in self: 
            record.statut='block'     
    @api.depends('pays_id')
    def _compute_pays_photo(self):
        for record in self:
            if record.pays_id:
                # Assurez-vous que le pays a une image attachée
                record.drapeau_pays = record.pays_id.flag
            else:
                record.drapeau_pays = False
    
    def test_action(self):
        print('Bonjour')
    
    def print_registration_report(self):
        return self.env.ref('campus_universel.action_report_registration').report_action(self)
    
    def print_procedure_report(self):
        return self.env.ref('campus_universel.action_report_procedure').report_action(self)
    
    @api.onchange('commercial_id')
    def _onchange_commercial_id(self):
  
        if self.commercial_id:
            self.gest_client_id = self.commercial_id.gest_client_id.id if self.commercial_id.gest_client_id else False
        else:
            self.gest_client_id = False
    
    @api.depends('etape_ids.progress')
    def _compute_progress(self):
        for procedure in self:
            etapes = procedure.etape_ids
            if etapes:
                procedure.progress = sum(etapes.mapped('progress')) / len(etapes)
            else:
                procedure.progress = 0.0
    
    def action_duplicate_procedure(self):

        time.sleep(2)
        for record in self:
            if record.nature != 'registration':
                raise ValueError("Cette action ne peut être exécutée que sur une procédure de type 'registration'.")

            if not record.procedure_id or record.procedure_id.nature != 'template':
                raise ValueError("Veuillez sélectionner une procédure de type 'Template'.")

            # Création du nouvel enregistrement avec fusion des données
            new_procedure_values = {
                'name': f"{record.name}",  # Nom mis à jour
                'nature': 'record',
                'procedure_id': record.procedure_id.id,  # Associer au template original
            }
               
            # 🔹 Fusionner les champs spécifiques de l'individu depuis "registration"
            individual_fields = [
                'name2', 'last_name', 'photo', 'birthday', 'nationality', 'passport_number',
                'passport_issue_date', 'passport_expiry_date', 'email', 'phone', 'address',
                'father_name', 'father_profession', 'father_contact', 'mother_name',
                'mother_profession', 'mother_contact', 'client_manager_name',
                'client_manager_contact', 'desired_country', 'desired_school', 'comments'
            ]
            for field in individual_fields:
                new_procedure_values[field] = record[field]
            
            new_procedure_values['opened_date']=datetime.now()
            # 🔹 Fusionner les champs spécifiques à la procédure depuis le template
            procedure_fields = [
                'description', 'amount_min', 'amount_max'
            ]
            for field in procedure_fields:
                new_procedure_values[field] = record.procedure_id[field]
            
            # Création de la nouvelle procédure avec les données fusionnées
            new_procedure = record.copy(new_procedure_values)

            # ✅ **Duplication des étapes associées**
            for etape in record.procedure_id.etape_ids:
                new_etape_values = {
                    'name': etape.name,
                    'details':etape.details,
                    'description': etape.description,
                    'color': etape.color,
                    'state': etape.state,
                    'progress': etape.progress,
                    'procedure_id': new_procedure.id,  # Associer l'étape à la nouvelle procédure
                    'phase_id': etape.phase_id.id,
                }
                new_etape = self.env['campus_universel.procedure.etape'].create(new_etape_values)

                # ✅ **Lier les documents à la nouvelle étape**
                for document in etape.document_ids:
                    new_document_values = {
                        'name': document.name,
                        'url': document.url,
                        'file': document.file,
                        'is_uploaded': document.is_uploaded,
                        'provenance': document.provenance,
                        'category': document.category,
                        'extension': document.extension,
                        'etape_id': new_etape.id,  # 📌 Lier au NOUVELLE ÉTAPE !
                    }
                    self.env['campus_universel.procedure.document'].create(new_document_values)

                # ✅ **Lier les actions à la nouvelle étape**
                for action in etape.action_ids:
                    new_action_values = {
                        'name': action.name,
                        'description': action.description,
                        'etape_id': new_etape.id,  # 📌 Lier au NOUVELLE ÉTAPE !
                    }
                    self.env['campus_universel.procedure.action'].create(new_action_values)

                # ✅ **Lier les transactions à la nouvelle étape**
                for transaction in etape.transaction_ids:
                    new_transaction_values = {
                        'name': transaction.name,
                        'amount': transaction.amount,
                        'payment_operation_id': transaction.payment_operation_id.id,
                        'type': transaction.type,
                        'etape_id': new_etape.id,  # 📌 Lier au NOUVELLE ÉTAPE !
                    }
                    self.env['campus_universel.transaction'].create(new_transaction_values)
            return {
                    'type': 'ir.actions.act_window',
                    'name': 'Nouvelle Procédure',
                    'res_model': 'campus_universel.procedure',
                    'res_id': new_procedure.id,
                    'view_mode': 'form',
                    'view_type': 'form',
                    'target': 'current',
            }
        
        
    