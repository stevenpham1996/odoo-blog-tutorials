from odoo import api, fields, models
from odoo.exceptions import ValidationError

class FosterMessage(models.TransientModel):
    _name = "cattery.foster.message"
    _description = "Fostering Messages"

    caregiver_ids = fields.Many2many("cattery.foster.parent", string="Foster Parents")
    message_head = fields.Char()
    message_body = fields.Html()

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        caregiver_ids = self.env.context["active_ids"]
        res["caregiver_ids"] = [(6, 0, caregiver_ids)]
        return res
    
    def send_message(self):
        self.ensure_one()
        if not self.caregiver_ids:
            raise ValidationError("Please select at least one foster parent.")
        if not self.message_body:
            raise ValidationError("Can not send a blank message.")
        for caregiver in self.caregiver_ids:
            caregiver.message_post(
                body=self.message_body,
                subject=self.message_head,
                subtype="mail.mt_comment",
            )
        return True