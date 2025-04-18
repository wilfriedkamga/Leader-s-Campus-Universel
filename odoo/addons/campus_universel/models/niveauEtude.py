from odoo import _, api, fields, models, tools
class ProcedureNiveauEtude(models.Model):
    _name = 'campus_universel.procedure.niveau_etude'
    _description = 'Niveaux d\'étude'
    _table = 'cu_niveau_etude'
    
    name = fields.Char(string='Niveau d\'étude')
    procedure_ids = fields.One2many('campus_universel.procedure', 'niveau_etude_id', string='Procedures')