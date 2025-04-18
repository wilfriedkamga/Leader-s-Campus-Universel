from random import randint
from odoo import _, api, fields, models, tools

class ProcedureFiliere(models.Model):
    _name = 'campus_universel.procedure.filiere'
    _description = 'Filières et domaines'
    _table = 'cu_filiere'
    
    def _get_default_color(self):
        return randint(1, 20)
    name = fields.Char(string='Filière/Domaine')
    procedure_ids = fields.Many2many('campus_universel.procedure', string='Procedures')
    group = fields.Char(string="Groupe")
    color = fields.Integer(string='Color', default=_get_default_color,
        help="Transparent tags are not visible in the kanban view of your projects and tasks.")
    
    