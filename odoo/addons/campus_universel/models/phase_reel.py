from odoo import _, api, fields, models, tools

class ProcedurePhaseReel(models.Model):

    _name = 'campus_universel.traitement.phase_reel'
    _description = 'Suivi et traitement des procédures de voyages'
    _table='cu_phase'
    
    name = fields.Char(string='Name')
    etape_ids = fields.One2many('campus_universel.traitement.etape_reel', 'phase_reel_id', string='Étapes')
    progress = fields.Float(string='Progress Bar',default=60)
    