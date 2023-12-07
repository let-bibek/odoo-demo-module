from odoo import models, fields


class Revision(models.Model):
    _name = "revision.schema"
    _description = "Revision Model Schema"

    first_name = fields.Char()
    surname = fields.Char()
    
    
