
from odoo import models, fields, api


class Caregiver(models.Model):
    _name = 'cattery.caregiver'
    _description = 'Foster Parents'
    _inherits = {
        "res.partner": "partner_id",
    }
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    ############ Fields #############
    partner_id = fields.Many2one("res.partner", string="Caregiver", required=True, ondelete="cascade")
    register_date = fields.Date(default=fields.Date.today, string="Register Date")
    active = fields.Boolean(string="Is Fostering?")
    
    kitten_ids = fields.One2many(
        "cattery.fostered_kitten", "caregiver_id", string="Fostered Kittens", index=True, required=True
    )
    ############ Computed Fields #############
    num_kittens = fields.Integer(compute="_compute_num_kittens")
    
    ############ Methods #############
    @api.depends("kitten_ids")
    def _compute_num_kittens(self):
        for record in self:
            record.num_kittens = len(record.kitten_ids)
 