from odoo import models, fields, api

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
    kitten_id = fields.Many2one("cattery.kitten", required=True,
                                domain=[('state', '=', 'available')])
    caregiver_id = fields.Many2one("cattery.caregiver", required=True)
    
    stage_id = fields.Many2one(
        "cattery.foster_stage", string = "Foster Stage", 
        default = _default_stage_id,
        group_expand = "_group_expand_stage_id",
    )
    state = fields.Selection(related="stage_id.state")