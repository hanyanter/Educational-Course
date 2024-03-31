from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date


class Stage(models.Model):
    _name = "stage"
    _description = 'Stage'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Subject Name')
    display_name = fields.Char(string='Subject Name')
    note = fields.Text()
