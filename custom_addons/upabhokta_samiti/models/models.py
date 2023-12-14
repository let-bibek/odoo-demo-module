# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Upabhokta_samiti(models.Model):
    _name = 'upabhokta.samiti'
    _description = 'upabhokta_samiti.upabhokta_samiti'

    name=fields.Char()
    registered_date=fields.Date()
    ticket_ids=fields.One2many("tickets.model",'event_id',string="Tickets")