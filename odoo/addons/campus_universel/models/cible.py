from odoo import _, api, fields, models, tools
class ProcedureCible(models.Model):

    _name = 'campus_universel.procedure.cible'
    _description = ''
    _table='cu_cible'
    
    name  = fields.Char(string='Label')
    description  = fields.Text(string='Description')
    procedure_ids = fields.Many2many('campus_universel.procedure', string='Procédure')