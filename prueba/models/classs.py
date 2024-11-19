# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Class(models.Model):
    _name = 'prueba.class'
    # _description = 'prueba.student'

    name = fields.Char(string='Nombre de la clase')
    code = fields.Char(string='Código de la clase')    
    
    



