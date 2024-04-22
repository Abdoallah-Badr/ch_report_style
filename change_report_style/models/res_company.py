from odoo import models,fields,api,exceptions,_

class ChangeStyle(models.Model):
    _inherit = 'res.company'

    second_logo_bool = fields.Boolean(string='Add another image', default=False)
    second_logo = fields.Binary(string='upload an image')
    name_ar = fields.Char(string='Name Ar', )
    street_ar = fields.Char(string='Street Ar', )
    street2_ar = fields.Char(string='Street2 Ar', )
    city_ar = fields.Char(string='City Ar', )

    arabic_layout = fields.Boolean(default=False)

    @api.constrains('second_image_bool', 'second_image')
    def _check_second_image(self):
        for rec in self:
            if (rec.second_image_bool == True) and (not rec.second_image):
                raise exceptions.ValidationError(_('Add another image or uncheck second image box'))

    @api.onchange('second_image')
    def _replace_original_image(self):
        for rec in self:
            if rec.second_image:
                rec.logo = rec.second_image

    # delete second image when uncheck boolean box
    @api.onchange('second_image_bool')
    def _unlink_second_image(self):
        for rec in self:
            if rec.second_image_bool == False and rec.second_image:
                rec.second_image = 0
