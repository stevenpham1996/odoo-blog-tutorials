
from odoo import models, fields, api


class Caregiver(models.Model):
    _name = 'cattery.caregiver'
    _description = 'Foster Parents'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _inherits = {
        "res.partner": "name", 
        "res.partner": "email",
        "res.partner": "contact_address"
    }
    
    name = fields.Many2one("res.partner", required=True, ondelete="cascade")
    email = fields.Many2one("res.partner", required=True, ondelete="cascade")
    contact_address = fields.Many2one("res.partner", required=True, ondelete="cascade")
    registered_date = fields.Date(default=fields.Date.today)
    kitten_ids = fields.One2many(
        "cattery.fostered_kitten", "name", string="Fostered Kittens", index=True, required=True
    )
    

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

