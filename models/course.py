from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date


class Course(models.Model):
    _name = "course"
    _description = 'Course'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=1, default="New", readonly=1, string='Reference')
    display_name = fields.Char()
    course_ids = fields.Many2many('res.partner.category')
    stage_id = fields.Many2one('stage')
    subject_id = fields.Many2one('subject')
    teacher_id = fields.Many2one('hr.employee')
    admin_id = fields.Many2one('hr.employee')
    course_type = fields.Selection([('online', 'Online'),
                                    ('offline', 'Offline')],
                                   default='offline',
                                   string='Course Type')
    cost = fields.Float()
    discount = fields.Float(string='Discount Percentage')
    start_date = fields.Date()
    end_date = fields.Date()
    number_of_sessions = fields.Integer(string='No. Sessions')
    number_of_invoiced_sessions = fields.Integer(string='No. Invoiced sessions')
    course_percent = fields.Float(string='Course %')
    students_ids = fields.Many2many('res.partner', required=1)
    accrual_total = fields.Integer(string='Accrual')
    accrual_ids = fields.One2many('teacher.accrual', 'course_id', string='Accrual')
    accrual_cnt = fields.Integer(string='Accrual Cnt')
    sales_person = fields.Many2one('hr.employee', string='Admin')
    extra_profit = fields.Float()
    invoice_count = fields.Integer()
    invoice_ids = fields.Many2many('account.move')
    note = fields.Text()
    session_ids = fields.One2many('session', 'course_id')
    no_invoice_sessions = fields.Char(string='no sessions')
    no_sessions_in = fields.Integer(string='no. invoiced sessions')
    no_sessions = fields.Integer(string='no. sessions')

    state = fields.Selection([('draft', 'Draft'),
                              ('progress', 'Progress'),
                              ('done', 'Done'),
                              ('invoiced', 'Invoiced'),
                              ('cancel', 'Rejected')], string='Status')

    # invoice_line_ids = fields.One2many('account.move.line', 'course_id', store=1)

    @api.model
    def create(self, vals):
        res = super(Course, self).create(vals)
        if res.name == 'New':
            res.name = self.env['ir.sequence'].next_by_code('course_seq')
        return res

    def action_draft(self):
        for rec in self:
            pass
            # rec.create_history_record(rec.state, 'undetermined')
            # rec.state = 'undetermined'

    def action_progress(self):
        for rec in self:
            pass
            # rec.create_history_record(rec.state, 'good')
            # rec.state = 'good'

    def action_done(self):
        for rec in self:
            pass
            # rec.create_history_record(rec.state, 'serious')
            # rec.state = 'serious'

    def action_invoiced(self):
        for rec in self:
            pass
            # rec.create_history_record(rec.state, 'serious')
            # rec.state = 'serious'

    def action_cancel(self):
        for rec in self:
            pass
            # rec.create_history_record(rec.state, 'serious')
            # rec.state = 'serious'
