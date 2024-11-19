# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student(models.Model):
    _name = 'prueba.student'
    _description = 'prueba.student'

    name = fields.Char(string='Nombre')
    last_name = fields.Char(string='Apellido')
    age = fields.Integer(string='Edad')

    account_number = fields.Char(string='Número de cuenta')

    career_id = fields.Many2one('prueba.career', string='Carrera')

    class_ids = fields.One2many('prueba.student.class', 'student_id', string='Clases')
    

    avg_score = fields.Float(string='Promedio de calificaciones', compute='_compute_avg_score', store=True)

    @api.depends('class_ids')
    def _compute_avg_score(self):
        for record in self:
            if record.class_ids:
                record.avg_score = sum([x.avg_score for x in record.class_ids]) / len(record.class_ids)
            else:
                record.avg_score = 0.0


