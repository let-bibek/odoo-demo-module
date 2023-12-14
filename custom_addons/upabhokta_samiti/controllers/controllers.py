# -*- coding: utf-8 -*-
# from odoo import http


# class UpabhoktaSamiti(http.Controller):
#     @http.route('/upabhokta_samiti/upabhokta_samiti', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upabhokta_samiti/upabhokta_samiti/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('upabhokta_samiti.listing', {
#             'root': '/upabhokta_samiti/upabhokta_samiti',
#             'objects': http.request.env['upabhokta_samiti.upabhokta_samiti'].search([]),
#         })

#     @http.route('/upabhokta_samiti/upabhokta_samiti/objects/<model("upabhokta_samiti.upabhokta_samiti"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upabhokta_samiti.object', {
#             'object': obj
#         })
