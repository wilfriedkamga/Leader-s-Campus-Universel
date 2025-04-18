from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError

class EstateProperty(models.Model):
    _name='estate.property'
    _description='description du model propriété'
    _order='id desc'

    name = fields.Char(string='Title')
    postcode = fields.Char(string="Postcode")
    description = fields.Char(string='Description')
    date_availability = fields.Date(string="Date de Disponibilité")
    expected_price = fields.Float(string="Prix Attendu")
    selling_price = fields.Float(string="Prix de Vente")
    best_price = fields.Float(string="Meilleur prix", compute='_compute_best')
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area(sqm)")
    facades = fields.Integer(string="Nombre de Façades")
    garage = fields.Boolean(string="Garage Disponible")
    garden = fields.Boolean(string="Jardin Disponible")
    garden_area = fields.Integer(string="Surface du Jardin")
    state = fields.Selection(string='Status', required=True, selection=[
            ('open', 'NEW'),
            ('posted', 'OFFER RECEIVED'),
            ('confirm', 'OFFER ACCEPTED'),
            ('sold', 'SOLD'),
        ])
    garden_orientation = fields.Selection([
        ('north', 'Nord'),
        ('south', 'Sud'),
        ('east', 'Est'),
        ('west', 'Ouest')
    ], string="Orientation du Jardin")
    type_id = fields.Many2one(
        'estate.property.type',
        string='Property Type',
        )
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='offers')
    seller_id = fields.Many2one(
        'res.users',
        string='Vendeur',
        )

    @api.depends('expected_price')
    @api.depends('selling_price')
    def _compute_best(self):
        for record in self:
            record.best_price= record.selling_price * record.expected_price

    @api.onchange('garden')
    def onchange_garden(self):
     if(self.garden==True):
        self.garden_area = 10
        self.garden_orientation='north'
    
    def test_action(self):
       for record in self:
          record.postcode="Test du bouton"
       return True
    
  
    _sql_constraints = [
        ('check_selling_price', 'CHECK(selling_price >= 0','Le prix d\'achart doit etre positif.'),
    ]

    @api.constrains('selling_price')
    def _check_field_name(self):
        for record in self:
           if(record.best_price==0):
              raise ValidationError('Le meilleur prix doit ')
    @api.model
    def create(self, vals):
        # Do some business logic, modify vals...
        vals['state']='posted'
        # Then call super to execute the parent method
        return super().create(vals)
    
    def print_property_offers_report(self):
        return self.env.ref('estate.action_report_estate_property_offer').report_action(self)