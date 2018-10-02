# -*- coding: utf-8 -*-
from odoo import models, fields

class BookCopy(models.Model):
    _name = 'library.bookcopy'
    _inherits = {
        'library.book': 'book_id',
    }
    _description = 'Book Copy'
    
    bookcopyref = fields.Char(string='Book Copy Ref')
    book_id = fields.Many2one('library.book', required=True)