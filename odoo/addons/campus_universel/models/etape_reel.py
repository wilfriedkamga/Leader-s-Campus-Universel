from odoo import _, api, fields, models, tools

class ProcedureEtapeReel(models.Model):

    _name = 'campus_universel.traitement.etape_reel'
    _description = 'Suivi et traitement des procédures de voyages'
    _table='cu_etaper'
    
    name = fields.Char(string='Name')
    description  = fields.Char(string='Description')
    color = fields.Integer(string="Color")
    state = fields.Selection([('wait', 'En attente'),('start', 'En cours'),('end', 'Terminé'),('cancel','Annulé')])
    progress = fields.Float(default=0.0,store=True)
    traitement_id = fields.Many2one(
        'campus_universel.traitement',
        string='Traitement',required=True
        )
    phase_reel_id = fields.Many2one(
        'campus_universel.traitement.phase_reel',
        string='Phase',
        )

    