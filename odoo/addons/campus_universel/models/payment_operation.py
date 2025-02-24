from odoo import _, api, fields, models, tools
class ProcedurePaymentOperation(models.Model):

    _name = 'campus_universel.procedure.payment_operation'
    _description = ''
    _table='cu_pay_ope'
    
    name  = fields.Char(string='Label')
    amount = fields.Float(string='Montant')
    payment_mode_id = fields.Many2one('campus_universel.procedure.payment_mode', string='Mode de paiment')
    transaction_ids = fields.One2many('campus_universel.transaction', 'payment_operation_id', string='Transactions')