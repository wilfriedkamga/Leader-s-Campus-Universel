from odoo import _, api, fields, models, tools
class ProcedureDiplome(models.Model):
    _name = 'campus_universel.procedure.diplome'
    _description = 'Diplômes'
    _table = 'cu_diplome'
    
    name = fields.Char(string='Diplôme')
    procedure_ids = fields.One2many('campus_universel.procedure', 'diplome_id', string='Procedures')