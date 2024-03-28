from odoo import models, fields

class Qualiopi(models.Model):
    _inherit = 'op.course'

    course_image = fields.Image(String='Course Image')
    pricing = fields.Char(string='Pricing')
    duration_hours = fields.Integer(string='Duration (Hours)')
    description = fields.Text(string='Description')
    objectives = fields.Text(string='objectives')
    prerequisites = fields.Text(string='Prerequisites')
    accessibility = fields.Text(string='Accessibility')
    assessment_methods = fields.Text(string='Assessment_methods')
    access = fields.Text(string='Access') 
    deadline = fields.Text(string='Deadline')
    educational_means = fields.Text(string='Educational_means')
    priority = fields.Selection([ ('0', '0'),('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'), ], string='Priority')
    
    certification_image = fields.Image(String='Certification Image')
    certification_pass_rates = fields.Char(string='Certification Pass Rates')
    validate_specific_skills = fields.Text(string='How to Validate Specific Skills')
    equivalent_certifications = fields.Text(string='Equivalent Certifications')
    switch_between_certifications = fields.Text(string='Ways to Switch Between Certifications')
    further_training_options = fields.Text(string='Further Training Options')
    job_opportunities = fields.Text(string='Job Opportunities')
