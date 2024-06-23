from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class FosteredKitten(models.Model):
    _name = "cattery.fostered_kitten"
    _description = "Fostered Kittens"
    _inherit = "cattery.kitten"
    
    ############# Default Methods #############
    @api.model
    def _default_stage_id(self):
        stage = self.env["cattery.foster_stage"].search(
            [("state", "=", "intake")], limit=1
            )
        return stage
    
    @api.model
    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search([domain], order=order)
    
    ############ Fields #############
    # kitten_id = fields.Many2one("cattery.kitten", required=True,
    #                             domain=[('state', '=', 'available')])
    state = fields.Selection(
        selection=[
            ("not_available", "Not Arrived"),
            ("available", "Available"),
            ("adopted", "Adopted"),
            ("fostered", "Fostered"),
        ],)
    
    caregiver_id = fields.Many2one("cattery.caregiver", required=True)
    
    stage_id = fields.Many2one(
        "cattery.foster_stage", string = "Foster Stage", 
        default = _default_stage_id,
        group_expand = "_group_expand_stage_id",
    )
    
    ############ Action Methods #############
    def action_foster(self):
        if self.state == "adopted":
            raise UserError("Sorry, kitten has found a permanent home.")
        elif self.state == "not_available":
            raise UserError("Kitten not yet ready, please wait a while.")
        return self.write({"state": "fostered"})
    
    ############ Constraints ###############
    @api.constrains("state", "caregiver_id")
    def _check_adopter_id(self):
        for record in self:
            if record.state != "fostered" and record.caregiver_id:
                raise ValidationError("Only fostered kittens can have a caregiver.")