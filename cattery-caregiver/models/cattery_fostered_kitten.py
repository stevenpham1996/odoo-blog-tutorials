from odoo import models, fields, api

class FosteredKitten(models.Model):
    _name = "cattery.fostered_kitten"
    _description = "Fostered Kittens"

    kitten_id = fields.Many2one("cattery.kitten", required=True)
    fostered_parent = fields.Many2one("cattery.caregiver", required=True)
    