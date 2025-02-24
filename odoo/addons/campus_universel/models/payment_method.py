from odoo import _, api, fields, models, tools
class ProcedurePaymentMethod(models.Model):

    _name = 'campus_universel.procedure.payment_method'
    _description = ''
    _table='cu_pay_met'
    
    name  = fields.Char(string='nom')
    Description  = fields.Char(string='Description')
    image = fields.Binary(string='Logo')
    payment_mode_ids = fields.Many2many('campus_universel.procedure.payment_mode', string='Modes de paiment')