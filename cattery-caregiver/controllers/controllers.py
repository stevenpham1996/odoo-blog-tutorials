# -*- coding: utf-8 -*-
# from odoo import http


# class Cattery-fostering(http.Controller):
#     @http.route('/cattery_caregiver/cattery_caregiver', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cattery_caregiver/cattery_caregiver/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cattery_caregiver.listing', {
#             'root': '/cattery_caregiver/cattery_caregiver',
#             'objects': http.request.env['cattery_caregiver.cattery_caregiver'].search([]),
#         })

#     @http.route('/cattery_caregiver/cattery_caregiver/objects/<model("cattery_caregiver.cattery_caregiver"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cattery_caregiver.object', {
#             'object': obj
#         })
