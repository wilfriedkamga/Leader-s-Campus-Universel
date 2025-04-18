from odoo import _, api, fields, models, tools
from random import randint

class ProcedureCible(models.Model):

    _name = 'campus_universel.procedure.cible'
    _description = ''
    _table='cu_cible'

    def _get_default_color(self):
        return randint(1, 11)
    
    name  = fields.Char(string='Label')
    description  = fields.Text(string='Description')
    procedure_ids = fields.Many2many('campus_universel.procedure', string='Procédure')
     
    color = fields.Integer(string='Color', default=_get_default_color,
        help="Transparent tags are not visible in the kanban view of your projects and tasks.")
    

    