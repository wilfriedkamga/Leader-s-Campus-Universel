from odoo import _, api, fields, models, tools

class ProcedureEtape(models.Model):

    _name = 'campus_universel.procedure.etape'
    _description = 'Suivi et traitement des procédures de voyages'
    _table='cu_etape'
    
    name = fields.Char(string='Name')
    description  = fields.Char(string='Description')
    color = fields.Integer(string="Color")
    state = fields.Selection([('wait', 'En attente'),('start', 'En cours'),('end', 'Terminé'),('cancel','Annulé')])
    progress = fields.Float(default=0.0, compute='_compute_progress',store=True)
    procedure_id = fields.Many2one(
        'campus_universel.procedure',
        string='Procedure',required=True
        )
    phase_id = fields.Many2one(
        'campus_universel.procedure.phase',
        string='Phase',
        )
    
    document_ids = fields.One2many('campus_universel.procedure.document', 'etape_id',string='Documents')

    action_ids = fields.One2many('campus_universel.procedure.action', 'etape_id',string='Actions')

    transaction_ids = fields.One2many(
        'campus_universel.transaction',
        'etape_id',
        string='Transactions'
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
        for record in self:
            if(record.state=='wait'):
                record.progress=0.0
            if(record.state=='start'):
                record.progress=50.0
            if(record.state=='end'):
                record.progress=100.0
            if(record.state=='cancel'):
                record.progress=-1.0
    

    