# -*- coding: utf-8 -*-
# from odoo import http


# class DevelopTestJs(http.Controller):
#     @http.route('/develop__test_js/develop__test_js', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/develop__test_js/develop__test_js/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('develop__test_js.listing', {
#             'root': '/develop__test_js/develop__test_js',
#             'objects': http.request.env['develop__test_js.develop__test_js'].search([]),
#         })

#     @http.route('/develop__test_js/develop__test_js/objects/<model("develop__test_js.develop__test_js"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('develop__test_js.object', {
#             'object': obj
#         })
