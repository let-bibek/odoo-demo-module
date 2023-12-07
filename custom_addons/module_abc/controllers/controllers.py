# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleAbc(http.Controller):
#     @http.route('/module_abc/module_abc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_abc/module_abc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_abc.listing', {
#             'root': '/module_abc/module_abc',
#             'objects': http.request.env['module_abc.module_abc'].search([]),
#         })

#     @http.route('/module_abc/module_abc/objects/<model("module_abc.module_abc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_abc.object', {
#             'object': obj
#         })
