from odoo import models, fields

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    first_name = fields.Char(string ="نام" , required=True)
    last_name = fields.Char(string = "نام خانوادگی",required=True)
    birth_date = fields.Date(string = "تاریخ تولد",required=True, default=fields.Date.today())
    phone = fields.Char(required=True, string = "شماره تلفن")
    email = fields.Char(string = "ایمیل")
    student_code = fields.Integer(string = "شماره دانش آموزی", required=True)
    average = fields.Float(string = "معدل")
    is_active = fields.Boolean(string = "فعال")
    grade = fields.Selection([('1','اول'), ('2','دوم'), ('3','سوم'), ('4','چهارم'), ('5','پنجم'), ('6','ششم')], string = "پایه")
    address = fields.Text(string = "آدرس")
    description = fields.Text(string = "توضیحات")
    gender = fields.Selection([('male','مرد'),('female','زن')], string = "جنسیت")
    class_id = fields.Many2one("school.classroom", string="نام کلاس")
    subject_ids = fields.Many2many("school.subject", string="درس")





