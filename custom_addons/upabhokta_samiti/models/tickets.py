from odoo import models, fields, api


class Tickets(models.Model):
    _name = "tickets.model"
    _description = "Tickets Model"

    event_name = fields.Char()
    ticket_venue = fields.Char()
    ticket_price = fields.Float()
    ticket_date = fields.Datetime()
    event_id = fields.Many2one("upabhokta.samiti")
