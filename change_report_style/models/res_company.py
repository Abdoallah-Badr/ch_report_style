from odoo import models,fields,api,exceptions,_

class ChangeStyle(models.Model):
    _inherit='res.company'

    second_logo_bool=fields.Boolean(string='Add another image',default=False)
    second_logo=fields.Binary(string='upload an image')

    arabic_layout = fields.Boolean(default=False)

    @api.constrains('second_logo_bool','second_logo')
    def _check_second_logo(self):
        for rec in self:
            if (rec.second_logo_bool == True) and (not rec.second_logo) :
                raise exceptions.ValidationError(_('Add another image or uncheck second image box'))


    # delete second image when uncheck boolean box
    @api.onchange('second_logo_bool')
    def _unlink_second_logo(self):
        for rec in self:
            if rec.second_logo_bool == False and rec.second_logo:
                rec.second_logo = 0