from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class FosterKitten(models.Model):
    _name = "cattery.foster.kitten"
    _description = "Fostered Kittens"

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

    caregiver_id = fields.Many2one("cattery.foster.parent", required=True)
    kitten_id = fields.Many2one("cattery.kitten", required=True)
    image = fields.Binary(related="kitten_id.image")
    # stage_id = fields.Many2one(
    #     "cattery.foster.stage", string = "Foster Stage", 
    #     default = _default_stage_id,
    #     group_expand = "_group_expand_stage_id",
    # )