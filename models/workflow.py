import requests
from odoo import api,models, fields

class Workflow(models.Model):
    _name='workflow'
    _description='Qualiopi Workflow'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    indicator_number = fields.Integer(string='Indicator Number')
    sequence = fields.Integer(string='Sequence', related='indicator_number', store=True)
    summary = fields.Text(string='Summary')
    partner_id = fields.Many2many('res.users', string='Assignees')
    verification_status = fields.Selection([
    ('not_verified', 'Not Verified'),
    ('verified', 'Verified'),],
    string='Verification Status')
    description = fields.Text(string='Description')
    link = fields.Char(string='Link')
    
    def toggle_verification(self):
        for record in self:
            if record.verification_status == 'not_verified':
                record.verification_status = 'verified'
                message = "The record has been verified."
            else:
                record.verification_status = 'not_verified'
                message = "The record is not verified."
            
            record.message_post(body=message)


    def verify_link(self):
        for record in self:
            link = record.link
            try:
                response = requests.head(link)
                if response.status_code == 200:
                    return {
                        'type': 'ir.actions.client',
                        'tag': 'display_notification',
                        'params': {
                            'title': 'Success!',
                            'message': 'The link is valid.',
                            'sticky': False,
                        }
                    }
                else:
                    return {
                        'type': 'ir.actions.client',
                        'tag': 'display_notification',
                        'params': {
                            'title': 'Error!',
                            'message': 'The link is not valid.',
                            'sticky': False,
                        }
                    }
            except requests.ConnectionError:
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': 'Error!',
                        'message': 'The link is not valid.',
                        'sticky': False,
                    }
                }