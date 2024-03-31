from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date


class Subject(models.Model):
    _name = "subject"
    _description = 'Subject'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    display_name = fields.Char(string='Subject Name', readonly=1)
    name = fields.Char(string='Subject Name', required=1)
    session_cost = fields.Float()
    product_id = fields.Many2one('product.product', string='Product', store=1, required=1)
    stage_id = fields.Many2one('stage', store=1, required=1)
    note = fields.Text()
