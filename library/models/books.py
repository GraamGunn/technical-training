# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Books(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title')
    authors_ids = fields.Many2many('library.partner', string="Authors")
    edition_date =  fields.Date(string='Edition date',)
    isbn = fields.Char(string='ISBN')
    publisher_id = fields.Many2one('library.publisher', string='Publisher')
    rental_ids = fields.One2many('library.rental', 'book_id', string='Rentals')
    cost = fields.Float(default = 1.0)
    qty = fields.Float(default = 1.0 )
    total = fields.Float()
    pub_name = fields.Char(related='publisher_id.name', store=True)

    all_info = fields.Char(compute='_compute_all_info', string='All Info')
    
    @api.depends('name', 'publisher_id', 'isbn', 'rental_ids')
    def _compute_all_info(self):
        for line in self:
            line.all_info = '%s (%s) [%s]' % (line.name, line.isbn, line.publisher_id.name)
            
    @api.onchange('cost', 'qty')
    def _onchange_costqty(self):
        self.total = self.cost * self.qty
        
    @api.constrains('qty')
    def _check_qty(self):
        for record in self:
            if record.qty > 20:
                raise ValidationError("No more than 20 allowed! (You said %s)" % record.qty)
     