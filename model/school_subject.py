from odoo import models, fields

class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'School subject'

    name = fields.Char(string="درس",required=True)