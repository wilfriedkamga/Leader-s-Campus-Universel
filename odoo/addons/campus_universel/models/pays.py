from odoo import _, api, fields, models, tools
class ProcedurePays(models.Model):

    _name = 'campus_universel.procedure.pays'
    _description = ''
    _table='cu_pays'
    
    name  = fields.Char(string='nom')
    area = fields.Float(string='superficie')
    flag = fields.Binary(string='Drapeau')
    procedure_ids = fields.One2many('campus_universel.procedure', 'pays_id', string='Procedures')