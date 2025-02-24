from odoo import _, api, fields, models, tools
class ProcedurePaymentMode(models.Model):

    _name = 'campus_universel.procedure.payment_mode'
    _description = ''
    _table='cu_pay_mod'
    
    name  = fields.Char(string='nom')
    amount = fields.Float(string='Montant total',compute="_compute_total_amount", store=True)
    procedure_id = fields.Many2one('campus_universel.procedure', string='Procédure', readonly=True)
    payment_operation_ids = fields.One2many('campus_universel.procedure.payment_operation','payment_mode_id' ,string='Tranches de paiement')
    payment_method_ids = fields.Many2many('campus_universel.procedure.payment_method', string='Méthodes de paiment')
    
    @api.depends('payment_operation_ids.amount')
    def _compute_total_amount(self):
        for record in self:
            record.amount = sum(record.payment_operation_ids.mapped('amount'))