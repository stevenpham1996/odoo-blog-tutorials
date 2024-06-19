
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
    name = fields.Many2one("res.partner", required=True, ondelete="cascade")
    email = fields.Many2one("res.partner", required=True, ondelete="cascade")
    contact_address = fields.Many2one("res.partner", required=True, ondelete="cascade")
    register_date = fields.Date(default=fields.Date.today, string="Register Date")
    
    kitten_ids = fields.One2many(
        "cattery.fostered_kitten", "name", string="Fostered Kittens", index=True, required=True
    )
    
    stage_id = fields.Many2one(
        "cattery.foster_stage", string = "Stage", 
        default = _default_stage_id,
        group_expand = "_group_expand_stage_id",
    )
    state = fields.Selection(related="stage_id.state")