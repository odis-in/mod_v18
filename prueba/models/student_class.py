# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StudentClass(models.Model):
    _name = 'prueba.student.class'
    # _description = 'prueba.student'

    name = fields.Char(string='Nombre de la clase')
    
    student_id = fields.Many2one('prueba.student', string='Estudiante')
    class_id = fields.Many2one('prueba.class', string='Clase')
    career_id = fields.Many2one('prueba.career', related="student_id.career_id", string='Carrera')

    avg_score = fields.Float(string='Promedio de calificaciones')
    



