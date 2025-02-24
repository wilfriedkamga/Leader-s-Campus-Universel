from odoo import _, api, fields, models, tools

class ProcedureEtape(models.Model):

    _name = 'campus_universel.procedure.etape'
    _description = 'Suivi et traitement des procédures de voyages'
    
    name = fields.Char(string='Name')
    state = fields.Selection([('open', 'En attente'),('start', 'En cours'),('end', 'Terminé')])
    procedure_id = fields.Many2one(
        'campus_universel.procedure',
        string='Procedure',
        )
    phase_id = fields.Many2one(
        'campus_universel.procedure.phase',
        string='Phase',
        )

    