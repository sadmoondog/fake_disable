# -*- coding: utf-8 -*-
from openerp import http

# class DisableOpenerpOnline(http.Controller):
#     @http.route('/disable_openerp_online/disable_openerp_online/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/disable_openerp_online/disable_openerp_online/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('disable_openerp_online.listing', {
#             'root': '/disable_openerp_online/disable_openerp_online',
#             'objects': http.request.env['disable_openerp_online.disable_openerp_online'].search([]),
#         })

#     @http.route('/disable_openerp_online/disable_openerp_online/objects/<model("disable_openerp_online.disable_openerp_online"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('disable_openerp_online.object', {
#             'object': obj
#         })