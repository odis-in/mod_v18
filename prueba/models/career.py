# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Career(models.Model):
    _name = 'prueba.career'
    # _description = 'prueba.student'

    name = fields.Char(string='Nombre de la carrera')
    code = fields.Char(string='Código de la carrera')    
    
    



