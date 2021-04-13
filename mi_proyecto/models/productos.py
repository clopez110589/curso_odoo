#-*- coding: utf-8 -*-

from odoo import models, fields, api


class mi_modulo(models.Model):
    _name = 'curso.odoo'
    _description = 'curso.odoo'

    name = fields.Char(string="Nombre producto")
    description = fields.Text(string="Descripcion larga")
   # session_ids = fields.One2many(comodel_name="academy.session", inverse_name="course_id" string="sessions")
    proveedor_id = fields.Many2one(comodel_name="res.partner", string="proveedor")
    industria_id = fields.Many2one(comodel_name="res.partner.industry", string ="tipo de giro")	
    
    
