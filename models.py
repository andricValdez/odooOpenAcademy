# -*- coding: utf-8 -*-


from openerp import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course' #Nombre del módulo

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    # active = fields.Boolean('Activo')

    #*** Many2one relations
    # responsible_id = fields.Many2one('res.users',
    #     ondelete='set null', string="Responsible", index=True)

    #*** one2many relations
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")


class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)

    #*** Multiple many2many relations
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    
