# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class mi_proyecto(models.Model):
#     _name = 'mi_proyecto.mi_proyecto'
#     _description = 'mi_proyecto.mi_proyecto'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
