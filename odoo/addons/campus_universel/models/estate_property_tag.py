from odoo import _, api, fields, models, tools

class EstatePropertyTag(models.Model):
    _name='estate.property.tag'
    _description='Définition des types de propriétés pour les maisons'
    _order='id desc'

    name = fields.Char(string='Label')
    
    

