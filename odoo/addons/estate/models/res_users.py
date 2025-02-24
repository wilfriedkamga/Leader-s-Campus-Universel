from odoo import _, api, fields, models, tools
class ResUsers(models.AbstractModel):

    _inherit = 'res.users'
    property_ids = fields.One2many('estate.property', 'seller_id', string='Properties')