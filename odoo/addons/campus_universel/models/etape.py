from odoo import _, api, fields, models, tools

class ProcedureEtape(models.Model):

    _name = 'campus_universel.procedure.etape'
    _description = 'Suivi et traitement des procédures de voyages'
    _table='cu_etape'
    _inherit = ['mail.thread', 'mail.activity.mixin'] 
    
    name = fields.Char(string='Name')
    details = fields.Char(string='Détails')
    description  = fields.Char(string='Description')
    color = fields.Integer(string="Color")
    state = fields.Selection([('wait', 'En attente'),('start', 'En cours'),('end', 'Terminé'),('cancel','Annulé')])
    progress = fields.Float(string="Progression", compute="_compute_progress", store=True)
    progress_percentage = fields.Float(string="progression(%)", compute="_compute_progress_percentage", store=True)
    procedure_id = fields.Many2one(
        'campus_universel.procedure',
        string='Procedure',required=True,ondelete='cascade')
    phase_id = fields.Many2one(
        'campus_universel.procedure.phase',
        string='Phase',
        )
    
    document_ids = fields.One2many('campus_universel.procedure.document', 'etape_id',string='Documents',ondelete='cascade')

    document2_ids = fields.Many2many(
        'campus_universel.procedure.document',
        string="Documents de l'étape",
        domain="[('procedure_id', '=', procedure_id)]"
    )

    action_ids = fields.One2many('campus_universel.procedure.action', 'etape_id',string='Actions',ondelete='cascade')
    
    transaction_ids = fields.One2many(
        'campus_universel.transaction',
        'etape_id',
        string='Transactions',
        ondelete='cascade'
    )
    
    @api.model
    def default_get(self, fields_list):
        """ Définit la procédure active comme valeur par défaut """
        defaults = super(ProcedureEtape, self).default_get(fields_list)
        if self.env.context.get('default_procedure_id'):
            defaults['procedure_id'] = self.env.context.get('default_procedure_id')
        return defaults
    @api.depends('state')
    def _compute_progress(self):
        
        for etape in self:
            if etape.state == 'wait':
                etape.progress = 0.0
            elif etape.state == 'start':
                etape.progress = 50.0
            elif etape.state == 'end':
                etape.progress = 100.0
            else:
                etape.progress = 0.0

    @api.depends('progress')
    def _compute_progress_percentage(self):

        for record in self:
            record.progress_percentage=record.progress/100
    