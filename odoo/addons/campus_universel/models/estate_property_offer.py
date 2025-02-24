from odoo import _, api, fields, models, tools

class EstatePropertyOffer(models.Model):
    _name='campus_universel.property.offer'
    _description='Définition des types de propriétés pour les maisons'
    _order='sequence'

    name = fields.Char(string='Label')
    sequence = fields.Integer(string="Sequence", default=10)
    price  = fields.Float(string='Prix')
    partner  = fields.Char(string='Partenaire')
    status  = fields.Selection([('Refused', 'Refused'),('Accepted','Accepted')])
    property_id = fields.Many2one(
        'estate.property',
        string='property',
        )
    type_id = fields.Many2one(
        'estate.property.type',
        string='Property Type',
        )
    
    def accepte_offer(self):
       for record in self:
          record.status='Accepted'
       return True
     
    def refuse_offer(self):
       for record in self:
          record.status='Refused'
       return True

