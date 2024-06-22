from odoo import models, fields, api

class FosterStage(models.Model):
    _name = "cattery.foster_stage"
    _description = "Foster Stages"
    _order = "sequence"

    name = fields.Char()
    sequence = fields.Integer(default=0)
    fold = fields.Boolean()
    active = fields.Boolean()
    state = fields.Selection(
        selection=[('intake', 'Intake'),
                   ('care', 'Care'),
                   ('preparation', 'Preparation'),
                   ('adoption', 'Adoption'),
                   ('return', 'Return')],
        default='intake',
    )
