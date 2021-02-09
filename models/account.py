# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


from odoo import api
from odoo import exceptions
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

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

    @api.constrains('begin_balance_timestamp')
    def _check_begin_balance_timestamp(self):
        date_today = fields.Date.today()
        for r in self:
            if r.begin_balance_timestamp <= date_today:
                raise exceptions.ValidationError("Fecha must be before today")
                
    @api.onchange('credit_line', 'begin_balance')
    def _verify_credit_line(self):
        if self.credit_line < 0:
            return {
                'warning': {
                    'title': "Incorrect credit",
                    'message': "Cantidad Total cant be less than begin balance",
                },
        }
        elif self.credit_line > self.begin_balance:
            return {
                'warning': {
                    'title': "Incorrect value",
                    'message': "The balance cant be superior",
                },
            }
            
    @api.constrains('descripcion')
    def _check_descripcion_length(self):
        for account in self:
            if len(account.descripcion)<3:
                raise ValidationError('descripcion es muy corto, debe tener al menos 3 caracteres')
            elif len(account.descripcion)>20:
                raise ValidationError('descripcion es muy largo, debe tener menos de 20 caracteres')
            

    