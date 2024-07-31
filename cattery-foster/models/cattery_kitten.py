from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Kitten(models.Model):
    _inherit = "cattery.kitten"
    
    
    ############ Fields #############
    caregiver_id = fields.Many2one("cattery.foster.parent")
    state = fields.Selection(
        selection=[
            ("not_available", "Not Arrived"),
            ("available", "Available"),
            ("fostered", "Fostered"),
            ("adopted", "Adopted"),
        ],
        ondelete={'fostered': 'cascade'},)
        

    ############ Computed Fields #############
    age = fields.Integer(string="Weeks Old", compute="_compute_age", 
                         store=True, readonly=False, required=True)

    @api.depends("birth_date")
    def _compute_age(self):
        for record in self:
            if record.birth_date: 
                record.age = round((fields.Date.today() - record.birth_date).days / 7)
            else:
                record.age = record.age if record.age else 8


    ############ Action Methods #############
    def action_foster(self):
        if self.state == "adopted":
            raise UserError("Sorry, kitten has found a permanent home.")
        elif self.state == "not_available":
            raise UserError("Kitten not yet ready, please wait a while.")
        return self.write({"state": "fostered"})
    
    ############ Onchange Methods #############
    @api.onchange("caregiver_id")
    def _onchange_caregiver_id(self):
        if self.caregiver_id:
            self.state = "fostered"
    
