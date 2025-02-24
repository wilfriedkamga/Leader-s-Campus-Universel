from odoo import http
from odoo.http import request

class CampusDashboardController(http.Controller):

    @http.route('/campus/dashboard', type='http', auth='user', website=True)
    def campus_dashboard(self, **kwargs):
        students_count = request.env['campus.student'].search_count([])
        teachers_count = request.env['campus.teacher'].search_count([])
        courses_count = request.env['campus.course'].search_count([])

        return request.render('ton_module_campus_universel.dashboard_template', {
            'students_count': students_count,
            'teachers_count': teachers_count,
            'courses_count': courses_count
        })
