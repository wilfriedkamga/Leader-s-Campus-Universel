from odoo import _, api, fields, models

class ResUsers(models.Model):
    _inherit = 'res.users'

    group_agent_campus_id = fields.Boolean(
        string="Est un Agent Campus",
        compute="_compute_group_agent_campus_id",
        store=False
    )

    procedure_ids = fields.One2many(
        'campus_universel.procedure',
        'gest_client_id',
        string="Procédure",  # Assurez-vous que le groupe est correct
    )

    nb_clients  = fields.Integer(
        string="Nombre de Clients",
        compute="_compute_nb_clients_prospects",
        store=True
    )

    nb_clients_af  = fields.Integer(
        string="Clients affectés",
        compute="_compute_nb_clients_prospects",
        store=True
    )

    nb_prospects = fields.Integer(
        string="Nombre de Prospects",
        compute="_compute_nb_clients_prospects",
        store=True
    )



    commercial_id = fields.One2many(
        'campus_universel.procedure.commercial',
        'gest_client_id',
        string='Commercial',
        )
    
    @api.depends("groups_id")
    def _compute_group_agent_campus_id(self):
        """Détermine si l'utilisateur appartient au groupe Agent Campus."""
        group = self.env.ref("campus_universel.group_agent_campus", raise_if_not_found=False)
        for user in self:
            user.group_agent_campus_id = bool(group and group in user.groups_id)
    
    @api.depends('procedure_ids.state_client')
    def _compute_nb_clients_prospects(self):
        """Compte le nombre de clients et de prospects par utilisateur."""
        for user in self:
            clients = user.procedure_ids.filtered(lambda p: p.state_client == 'client')
            prospects = user.procedure_ids.filtered(lambda p: p.state_client == 'prospect')
            user.nb_clients_af=len(clients) - len(prospects)
            user.nb_clients = len(clients)
            user.nb_prospects = len(prospects)
    def test_action(self):
        print('bonjour')
