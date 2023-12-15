# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class develop__test_js(models.Model):
#     _name = 'develop__test_js.develop__test_js'
#     _description = 'develop__test_js.develop__test_js'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
