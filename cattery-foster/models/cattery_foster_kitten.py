from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class FosterKitten(models.Model):
    _inherit = "cattery.kitten"
    
    ############# Default Methods #############
    # @api.model
    # def _default_stage_id(self):
    #     stage = self.env["cattery.foster.stage"].search(
    #         [("state", "=", "intake")], limit=1
    #         )
    #     return stage
    
    # @api.model
    # def _group_expand_stage_id(self, stages, domain, order):
    #     return stages.search([domain], order=order)
    
    ############ Fields #############
    # kitten_id = fields.Many2one("cattery.kitten", required=True,
    #                             domain=[('state', '=', 'available')])
    state = fields.Selection(
        selection=[
            ("not_available", "Not Arrived"),
            ("available", "Available"),
            ("fostered", "Fostered"),
            ("adopted", "Adopted"),
        ],
        ondelete={'fostered': 'cascade'},)
    
    caregiver_id = fields.Many2one("cattery.foster.parent")
    
    # stage_id = fields.Many2one(
    #     "cattery.foster.stage", string = "Foster Stage", 
    #     default = _default_stage_id,
    #     group_expand = "_group_expand_stage_id",
    # )
    
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