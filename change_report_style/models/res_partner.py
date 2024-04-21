from odoo import models, fields, api
from datetime import date, datetime, timedelta


class upward_sale_support(models.Model):
    _name = 'res.partner'
    _description = ''
    _inherit = 'res.partner'


    name_ar = fields.Char(string='Name Ar',)
    street_ar = fields.Char(string='Street Ar',)
    street2_ar = fields.Char(string='Street2 Ar',)
    city_ar = fields.Char(string='City Ar',)



