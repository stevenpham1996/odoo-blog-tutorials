
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class FosterParent(models.Model):
    _name = 'cattery.foster.parent'
    _description = 'Caregivers'
    _inherits = {
        "res.partner": "partner_id",
    }
    _inherit = ['mail.thread', 'mail.activity.mixin'] 
    
    ############ Fields #############
    partner_id = fields.Many2one("res.partner", string="Name", required=True, ondelete="cascade")
    register_date = fields.Date(default=fields.Date.today, string="Register Date")
    active = fields.Boolean(string="Is Active?")
    
    foster_kitten_ids = fields.One2many(
        "cattery.foster.kitten", "caregiver_id", string="Fostered Kittens", index=True, required=True
    )
    ############ Computed Fields #############
    num_kittens = fields.Integer(compute="_compute_num_kittens")
    
    ############ Computed Methods #############
    @api.depends("foster_kitten_ids")
    def _compute_num_kittens(self):
        for record in self:
            record.num_kittens = len(record.foster_kitten_ids)
 
     ############ Constraints ###############
    @api.constrains("foster_kitten_ids", "active")
    def _check_foster_parent(self):
        for record in self:
            for kitten in record.foster_kitten_ids:
                if kitten.state != "fostered" \
                or kitten.caregiver_id.partner_id != record.partner_id:
                    raise ValidationError("Please choose the correct foster kitten.")
            if record.active and len(record.foster_kitten_ids) < 1:
                    raise ValidationError("Active parent must foster at least 1 kitten.")
            elif not record.active and len(record.foster_kitten_ids) > 1:
                    raise ValidationError("Inactive parent can not foster any kitten.")
                

            