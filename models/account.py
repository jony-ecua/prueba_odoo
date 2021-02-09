# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


from odoo import api
from odoo import fields
from odoo import models

class Account(models.Model):
    _name = 'banco.account'
    
    descripcion = fields.Text()
    balance = fields.Float(string="Balance")
    credit_line = fields.Float(string="Credit line")
    begin_balance = fields.Float(string="Begin balance")
    begin_balance_timestamp = fields.Datetime(string="Balance Timestamp")
    
    accountType = fields.Selection(
                                   selection=[('1', 'STANDAR'),
                                   ('2', 'CREDIT')],
                                   string="Selecione cuenta",
                                   default='1',
                                   requeried=True)
                                                
    customer_ids = fields.Many2many('banco.customers', string="Customers")
    movement = fields.One2many('banco.movement', 'accounts', string="Movement")
