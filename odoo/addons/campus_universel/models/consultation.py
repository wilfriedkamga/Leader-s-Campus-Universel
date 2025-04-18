from odoo import _, api, fields, models, tools
class consultation(models.Model):
    _name = 'campus_universel.consultation'
    _description = 'consultation des candidats'
    _table = 'cu_consultation'
    
    name = fields.Char(string='Diplôme')
    date = fields.Datetime(string="Date et Heure de la consultation")
    comment = fields.Text(string='Commentaires')
    document_ids = fields.Many2many('campus_universel.procedure.document',string='Documents',domain="[('procedure_id', '=', procedure_id)]")
    procedure_id = fields.Many2one('campus_universel.procedure', string='Procedures')
    