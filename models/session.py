from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date


class Session(models.Model):
    _name = "session"
    _description = 'Session'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    display_name = fields.Char()
    name = fields.Char(required=1, default="New", string='Reference')
    course_id = fields.Many2one('course')
    subject_id = fields.Many2one('subject', store=1)
    stage_id = fields.Many2one('stage')
    price = fields.Float()
    sales_person = fields.Many2one('hr.employee', string='Admin')
    teacher_id = fields.Many2one('hr.employee')
    session_percent = fields.Float(string='Session %')
    session_accrual = fields.Float()
    session_type = fields.Selection([('online', 'Online'),
                                     ('offline', 'Offline')],
                                    default='offline',
                                    string='Session Type')
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    duration = fields.Float()
    note = fields.Text()
    student_ids = fields.Many2many('res.partner', store=1)
    accrual_cnt = fields.Integer()
    accrual_ids = fields.One2many('teacher.accrual', 'session_id')
    color = fields.Integer()
    extra_profit = fields.Float()
    invoice_count = fields.Integer()
    invoice_ids = fields.Many2many('account.move', string='Invoices', store=1)
    product_id = fields.Many2one('product.product')
    state = fields.Selection([('draft', 'Draft'),
                              ('progress', 'Progress'),
                              ('done', 'Done'),
                              ('invoiced', 'Invoiced'),
                              ('cancel', 'Rejected')],
                             default='draft', string='Status')

    invoice_line_ids = fields.Many2many('account.move.line', string='Invoices Line', store=1)
    payment_type = fields.Char()

    @api.onchange('start_date', 'duration')
    def _compute_end_date(self):
        for rec in self:
            start_date = fields.Datetime.today(rec.start_date).hour
            end_date = start_date + rec.duration
            rec.end_date = end_date

    # @api.onchange('duration')
    # def _onchange_end_date(self):
    #     for rec in self:
    #         start_date = fields.Datetime.today(rec.start_date).hour
    #         end_date = start_date + rec.duration
    #         rec.end_date = end_date
            # return {'warning': {'title': 'warning',
            #                     'message': 'PCR has been checked due to age below 30'}
            #         }

    @api.model
    def create(self, vals):
        res = super(Session, self).create(vals)
        if res.name == 'New':
            res.name = self.env['ir.sequence'].next_by_code('session_seq')
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

    def action_view_invoice(self):
        action = self.env['ir.actions.actions']._for_xml_id('account.account_move')
        view_id = self.env.ref('account.view_move_form').id
        action['res_id'] = self.invoice_ids.id
        action['views'] = [[view_id, 'form']]
        return action

    def action_view_accrual(self):
        action = self.env['ir.actions.actions']._for_xml_id('course.teacher_accrual_action')
        view_id = self.env.ref('course.teacher_accrual_form_view').id
        action['res_id'] = self.teacher_id.id
        action['views'] = [[view_id, 'form']]
        return action
