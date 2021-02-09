# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models

class Movement(models.Model):
    
    _name = 'banco.movement'

    timestamp = fields.Datetime(string = "Timestamp")
    amount = fields.Float(string="Amount")
    balance = fields.Float(string = "Balance")
    description = fields.Char(string = "Descripcion")
    
    accounts = fields.Many2one('banco.account', ondelete='cascade', string="Movimientos")
  
