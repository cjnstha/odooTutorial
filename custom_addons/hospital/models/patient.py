# -*- coding: utf-8 -*-
# import odoo
from odoo import api, fields, models, _

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    #defining fields for the models#

    name = fields.Char(string='Name')
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female','Female')], string="Gender")

