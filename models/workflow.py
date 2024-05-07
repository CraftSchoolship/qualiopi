<<<<<<< HEAD
import requests
=======

>>>>>>> 53cc62070e7f9adc0ea9f7c73ab16078b4a7d47d
from odoo import api,models, fields

class Workflow(models.Model):
    _name='workflow'
    _description='qualiopi workflow'

    indicatornumber = fields.Integer(string='Indicator Number')
    sequence = fields.Integer(string='Sequence', related='indicatornumber', store=True)
    summary = fields.Text(string='Summary')
    partner_id = fields.Many2many('res.users', string='Assignees')
    verification_status = fields.Selection([
    ('not_verified', 'Not Verified'),
    ('verified', 'Verified'),],
    string='Verification Status')
    verification_date = fields.Date(string='Verification Date')
    verified_by = fields.Many2one('res.users', string='Verified By')
    attachment_ids = fields.Many2many('ir.attachment', string='Attachments')
    description = fields.Text(string='Description')
<<<<<<< HEAD
    link = fields.Char(string='Link')
    
    def toggle_verification(self):
        self.verification_status = 'verified' if self.verification_status == 'not_verified' else  'not_verified'

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
                            'message': 'The link exists.',
                            'sticky': False,
                        }
                    }
                else:
                    return {
                        'type': 'ir.actions.client',
                        'tag': 'display_notification',
                        'params': {
                            'title': 'Error!',
                            'message': 'The link does not exist.',
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
=======

    def toggle_verification(self):
        self.verification_status = 'verified' if self.verification_status == 'not_verified' else  'not_verified'

    
>>>>>>> 53cc62070e7f9adc0ea9f7c73ab16078b4a7d47d
