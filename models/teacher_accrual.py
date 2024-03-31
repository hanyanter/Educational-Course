from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime, date


class TeacherAccrual(models.Model):
    _name = "teacher.accrual"
    _description = 'Teacher Accrual'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, default="New", readonly=True)
    display_name = fields.Char(required=True, default="New", readonly=True)
    employee_id = fields.Many2one('hr.employee', store=1, string='Teacher')
    subject_id = fields.Many2one('subject', store=1)
    percentage = fields.Float()
    amount = fields.Float()
    date = fields.Date()
    acc_move_id = fields.Many2one('account.move', string='Accrual Journal Entry', store=1)
    note = fields.Text()
    course_id = fields.Many2one('course', store=1)
    input_id = fields.Many2one('hr.payslip.input', store=1)
    paid_move_id = fields.Many2one('account.move', string='Payment Journal Entry', store=1)
    payslip_id = fields.Many2one('hr.payslip', string='Payslip', store=1)
    session_id = fields.Many2one('session', store=1)
    state = fields.Selection([('draft', 'Draft'),
                              ('paid', 'Paid'),
                              ('cancel', 'Rejected')], string='Status',
                             default='draft')

    # def action_draft(self):
    #     for rec in self:
    #         pass
    #         # rec.create_history_record(rec.state, 'undetermined')
    #         # rec.state = 'undetermined'
    #
    # def action_paid(self):
    #     for rec in self:
    #         pass
    #         # rec.create_history_record(rec.state, 'good')
    #         # rec.state = 'good'
    #
    # def action_cancel(self):
    #     for rec in self:
    #         pass
    #         # rec.create_history_record(rec.state, 'serious')
    #         # rec.state = 'serious'

    @api.model
    def create(self, vals):
        today_date = datetime.today().strftime('%Y-%m-%d')
        res = super(TeacherAccrual, self).create(vals)
        if res.name == 'New':
            res.name = self.env['ir.sequence'].next_by_code('teacher_accrual_seq')
        return f"{res}/{today_date}"
