# -*- coding: utf-8 -*-
# from odoo import http


# class ControlSaleComplements(http.Controller):
#     @http.route('/control_sale_complements/control_sale_complements', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/control_sale_complements/control_sale_complements/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('control_sale_complements.listing', {
#             'root': '/control_sale_complements/control_sale_complements',
#             'objects': http.request.env['control_sale_complements.control_sale_complements'].search([]),
#         })

#     @http.route('/control_sale_complements/control_sale_complements/objects/<model("control_sale_complements.control_sale_complements"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('control_sale_complements.object', {
#             'object': obj
#         })
