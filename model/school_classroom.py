from odoo import models, fields

class SchoolClassroom(models.Model):
    _name = 'school.classroom'
    _description = 'School Classroom'

    name = fields.Char(string="نام کلاس",required=True)