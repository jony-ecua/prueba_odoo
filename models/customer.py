# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models
from odoo import exceptions

class Customer(models.Model):
    _name = 'res.users'
    _inherit ='res.users'
    
    stree = fields.Char(string = "Stree", required=True)
    city = fields.Char(string = "City")
    state = fields.Char(string="State")
    codigo_potal = fields.Integer(string="Codigo postal")
    email = fields.Char(string="Email")
    
    account_id = fields.Many2many('banco.account', string="Account")
    
    