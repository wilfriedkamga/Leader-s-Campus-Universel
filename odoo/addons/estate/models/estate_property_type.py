from odoo import _, api, fields, models, tools

class EstatePropertyType(models.Model):
    _name='estate.property.type'
    _description='Définition des types de propriétés pour les maisons'
    _order='id desc'

    name = fields.Char(string='Label')
    property_ids = fields.One2many('estate.property', 'type_id', string='Properties')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='offers')
    offer_count = fields.Integer(string='Offers Nb', compute="_compute_offer_count")
    
    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count=len(record.offer_ids)
