from odoo import _, api, fields, models, tools
class ProcedureMention(models.Model):
    _name = 'campus_universel.procedure.mention'
    _description = 'Mentions académiques'
    _table = 'cu_mention'
    
    name = fields.Char(string='Mention')
    procedure_ids = fields.One2many('campus_universel.procedure', 'mention_id', string='Procedures')