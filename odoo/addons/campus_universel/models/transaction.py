from odoo import _, api, fields, models, tools
class ProcedureTransaction(models.Model):

    _name = 'campus_universel.transaction'
    _description = ''
   
    
    name  = fields.Char(string='Description')
    amount = fields.Float(string='Montant')
    validation_secretaire = fields.Boolean()
    validation_caissiere = fields.Boolean()
    payment_operation_id = fields.Many2one('campus_universel.procedure.payment_operation', string='Opération financière')
    type = fields.Selection([
        ('entree', 'Entrée'),
        ('sortie', 'Sortie')
    ], string='Type de transaction', required=True,ondelete='cascade', default='entree')
    
    etape_id = fields.Many2one(
        'campus_universel.procedure.etape',
        string='Étape associée',
        required=True,
        ondelete='cascade'
    )

    procedure_id = fields.Many2one(
        'campus_universel.procedure',
        string='Procédure associée',
        required=True,
        ondelete='cascade'
    )