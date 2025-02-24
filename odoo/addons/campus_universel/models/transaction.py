from odoo import _, api, fields, models, tools
class ProcedureTransaction(models.Model):

    _name = 'campus_universel.transaction'
    _description = ''
    
    name  = fields.Char(string='Description')
    amount = fields.Float(string='Montant')
    payment_operation_id = fields.Many2one('campus_universel.procedure.payment_operation', string='Opération financière')