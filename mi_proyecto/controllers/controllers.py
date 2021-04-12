# -*- coding: utf-8 -*-
# from odoo import http


# class MiProyecto(http.Controller):
#     @http.route('/mi_proyecto/mi_proyecto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mi_proyecto/mi_proyecto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mi_proyecto.listing', {
#             'root': '/mi_proyecto/mi_proyecto',
#             'objects': http.request.env['mi_proyecto.mi_proyecto'].search([]),
#         })

#     @http.route('/mi_proyecto/mi_proyecto/objects/<model("mi_proyecto.mi_proyecto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mi_proyecto.object', {
#             'object': obj
#         })
