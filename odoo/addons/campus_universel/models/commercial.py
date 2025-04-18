from odoo import _, api, fields, models, tools

class ProcedureCommercial(models.Model):
    
    _name = 'campus_universel.procedure.commercial'
    _description = 'Intermédiaire chargé d’attirer et d’accompagner les clients dans l’entreprise.'
    _table='cu_commercial'

    name = fields.Char(string='Nom du Commercial')
    birthday = fields.Char(string='Date de naissance')
    phone = fields.Char(string='Télephone')
    is_gestClient  = fields.Boolean(default=False)
    contrat  = fields.Binary()
    procedure_ids = fields.One2many('campus_universel.procedure', 'commercial_id',string='Procedures')
    gest_client_id = fields.Many2one(
        'res.users',
        string='Gestionnaire Client',
        domain=lambda self: [('groups_id', 'in', self.env.ref('campus_universel.group_gestclient_campus').id)]
        )
    
   
    