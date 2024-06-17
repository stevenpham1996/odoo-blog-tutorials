# -*- coding: utf-8 -*-
# from odoo import http


# class Cattery-fostering(http.Controller):
#     @http.route('/cattery-fostering/cattery-fostering', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cattery-fostering/cattery-fostering/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cattery-fostering.listing', {
#             'root': '/cattery-fostering/cattery-fostering',
#             'objects': http.request.env['cattery-fostering.cattery-fostering'].search([]),
#         })

#     @http.route('/cattery-fostering/cattery-fostering/objects/<model("cattery-fostering.cattery-fostering"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cattery-fostering.object', {
#             'object': obj
#         })

