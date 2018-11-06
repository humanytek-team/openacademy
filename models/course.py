# -*- coding: utf-8 -*-

from odoo import models, fields


class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(
        required=True,
        string='Title',
    )
    description = fields.Text(
    )
