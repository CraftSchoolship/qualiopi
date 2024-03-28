from odoo import http
from odoo.http import request

class Main(http.Controller):
     @http.route('/courses', type='http', auth='public', website=True)
     def index(self, **kw):
        op_courses = request.env['op.course'].sudo().search([])

        
        return request.render('qualiopi.index', {'op_courses': op_courses})
     
     @http.route('/course/<model("op.course"):course>', type='http', auth="user", website=True)
     def product_details(self, course):
        values = {
            'course': course,
        }
        return request.render('qualiopi.course_details', values)