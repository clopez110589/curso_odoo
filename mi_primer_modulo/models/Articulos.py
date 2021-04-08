# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Articulos(models.Model):
    
    _name='primer.modulo'
    _description='curso odoo primer modulo'
    
    name=fields.Char(string ='name',store=True)
    description=fields.Text(string ='description',store=True)
    
#     nivel = fields.Selection(string = 'Level',
#                             selection  = [('verde', 'VERDE'),
#                                           ('amarillo', 'AMARILLO'),
#                                          ('rojo', 'ROJO')],
#                                          copy= False, store=True)
    
#     estatus = fields.Boolean(string='Active', default = True, store=True)