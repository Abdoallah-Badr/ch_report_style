from odoo import models,fields
class ChangeStyle(models.Model):
    _inherit='res.company'

    second_image_bool=fields.Boolean(string='Add another image',default=False)
    second_image=fields.Binary(string='upload an image')
