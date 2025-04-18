from odoo import models, fields

class ProcedureTutoriel(models.Model):
    _name = 'campus_universel.procedure.tutoriel'
    _description = 'Tutoriels associés aux actions'
    _table='cu_tutoriel'

    name = fields.Char(string='Nom du tutoriel', required=True)
    action_id = fields.Many2one(
        'campus_universel.procedure.action',
        string='Action',
        required=True,
        ondelete='cascade'
    )
    type = fields.Selection([
        ('video', 'Vidéo'),
        ('audio', 'Audio'),
        ('document', 'Document')
    ], string='Type de tutoriel', required=True)
    file = fields.Binary(string='Fichier')
    file_name = fields.Char(string='Nom du fichier')

