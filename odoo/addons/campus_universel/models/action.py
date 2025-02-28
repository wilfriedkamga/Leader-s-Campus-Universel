from odoo import _, api, fields, models, tools

class ProcedureAction(models.Model):
    _name = 'campus_universel.procedure.action'
    _description = 'Actions à mener dans une étape de la procédure'
    _table='cu_action'

    name = fields.Char(string='Nom de l\'action')
    description = fields.Text(string='Description')

    etape_id = fields.Many2one(
        'campus_universel.procedure.etape',
        string='Étape',
    )
    tutoriel_ids = fields.One2many(
        'campus_universel.procedure.tutoriel',
        'action_id',
        string='Tutoriels'
    )
    # ✅ Nouveau champ pour relier directement une action à une procédure
    procedure_id = fields.Many2one(
        'campus_universel.procedure',
        string="Procédure",
        compute='_compute_procedure',
        store=True
    )

    @api.depends('etape_id')
    def _compute_procedure(self):
        """Récupérer la procédure associée à partir de l'étape"""
        for action in self:
            action.procedure_id = action.etape_id.procedure_id if action.etape_id else False