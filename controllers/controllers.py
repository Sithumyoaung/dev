# -*- coding: utf-8 -*-
# from odoo import http


# class CherryLandDevelopment(http.Controller):
#     @http.route('/cherry_land_development/cherry_land_development', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cherry_land_development/cherry_land_development/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cherry_land_development.listing', {
#             'root': '/cherry_land_development/cherry_land_development',
#             'objects': http.request.env['cherry_land_development.cherry_land_development'].search([]),
#         })

#     @http.route('/cherry_land_development/cherry_land_development/objects/<model("cherry_land_development.cherry_land_development"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cherry_land_development.object', {
#             'object': obj
#         })

