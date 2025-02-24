from odoo import _, api, fields, models, tools

class ProcedurePhase(models.Model):

    _name = 'campus_universel.procedure.phase'
    _description = 'Suivi et traitement des procédures de voyages'
    
    name = fields.Char(string='Name')
    etape_ids = fields.One2many('campus_universel.procedure.etape', 'phase_id', string='Étapes')

    