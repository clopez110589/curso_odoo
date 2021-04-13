from odoo import models,fields, api

class session(models.Model):
    _name: "academy.session"
    _description: "Session info"    
    

    #course_id = fields.Many2one(comodel_name="curso.odoo", string="Course", ondelete="cascade" requided="True"
    #name = field.char(string="Title", related="course_id.name")
                          