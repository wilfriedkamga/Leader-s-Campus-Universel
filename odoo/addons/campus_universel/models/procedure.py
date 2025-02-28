from odoo import _, api, fields, models, tools

class Procedure(models.Model):

    _name = 'campus_universel.procedure'
    _description = 'Suivi et traitement des procédures de voyages'
    _table='cu_procedure'
    
    
    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    cible_ids = fields.Many2many('campus_universel.procedure.cible', string='Cibles')
    payment_mode_ids= fields.One2many('campus_universel.procedure.payment_mode','procedure_id', string='Modes de paiment')
    pays_id = fields.Many2one(
        'campus_universel.procedure.pays',
        string='Pays de destination',
        )
    etape_ids = fields.One2many('campus_universel.procedure.etape', 'procedure_id', string='Étapes')
    drapeau_pays = fields.Binary(string='Drapeau', compute='_compute_pays_photo',store=True)
    amount_min = fields.Float(string='Montant minimal')
    amount_max = fields.Float(string='Montant max')
    statut  = fields.Selection([('new', 'Création'), ('actif','Actif'),('block','Bloqué')], string='Statut de la procédure')
    color = fields.Integer(string="Couleur")
    mat = fields.Char(string=' ')
    name2 = fields.Char(string='Nom')
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
    nature  = fields.Selection([('template', 'Template'),('record','Record')])
    # 📄 Liste des documents de la procédure (récupérés des étapes)
    document_ids = fields.One2many(
        'campus_universel.procedure.document',
        'procedure_id',
        compute='_compute_documents',
        string='Documents de la procédure',
        store=True
    )

    # ✅ Liste des actions de la procédure (récupérées des étapes)
    action_ids = fields.One2many(
        'campus_universel.procedure.action',
        'procedure_id',
        compute='_compute_actions',
        string='Actions de la procédure',
        store=True
    )

    @api.depends('etape_ids.document_ids')
    def _compute_documents(self):
        """Récupère tous les documents des étapes pour les afficher dans la procédure"""
        for procedure in self:
            all_documents = procedure.etape_ids.mapped('document_ids')
            procedure.document_ids = [(6, 0, all_documents.ids)]

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

    def create_procedure(self):
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