from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date


class CustomerInherit(models.Model):

    _inherit = ['res.partner']

    customer = fields.Boolean(string='Is a Customer')
    supplier = fields.Boolean(string='Is a Vendor')
