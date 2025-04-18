from odoo import _, api, fields, models, tools
class ProcedureMotifVoyage(models.Model):
    _name = 'campus_universel.procedure.motif_voyage'
    _description = 'Motifs de voyage'
    _table = 'cu_motif_voyage'
    
    name = fields.Char(string='Motif de voyage')
    procedure_ids = fields.One2many('campus_universel.procedure', 'motif_voyage_id', string='Procedures')