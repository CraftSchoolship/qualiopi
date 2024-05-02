from odoo import api, models, fields

class Workflow(models.Model):
    _name = 'workflow'
    _description = 'qualiopi workflow'

    indicatornumber = fields.Integer(string='Indicator Number')
    sequence = fields.Integer(string='Sequence', related='indicatornumber', store=True)
    summary = fields.Text(string='Summary')
    partner_id = fields.Many2many('res.users', string='Assignee')
    verification_status = fields.Selection([
        ('not_verified', 'Not Verified'),
        ('verified', 'Verified'),
    ], default='not_verified', string='Verification Status')
    verified_by = fields.Many2one('res.users', string='Verified By')
    verification_method = fields.Char(string='Verification Method')
    attachment_ids = fields.Many2many('ir.attachment', string='Attachments')

    def toggle_verification(self):
        self.verification_status = 'verified' if self.verification_status == 'not_verified' else  'not_verified'
