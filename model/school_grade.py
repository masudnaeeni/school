from odoo import models, fields

class SchoolGrade(models.Model):
    _name = 'school.grade'
    _description = 'School Grade'

    subject_id = fields.Many2one("school.subject",string='درس')
    grade = fields.Float(string='نمره')
    student_id = fields.Many2one("school.student", string='دانش آموز')



