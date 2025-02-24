from odoo import _, api, fields, models, tools

class Procedure(models.Model):

    _name = 'campus_universel.procedure'
    _description = 'Suivi et traitement des procédures de voyages'
    
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
    statut  = fields.Selection([('actif', 'Actif'), ('inactif','Inanctif')], string='Statut de la procédure')
   
    @api.onchange('pays_id')
    def _onchange_pays_id(self):
        if self.pays_id:
            # Si un pays est sélectionné, mettre à jour l'image associée
            self.drapeau_pays = self.pays_id.flag
        else:
            # Si aucun pays n'est sélectionné, laisser la photo vide
            self.drapeau_pays = False
            
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