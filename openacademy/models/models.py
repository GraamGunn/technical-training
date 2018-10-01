from odoo import api, fields, models

'''The citadel of the seven kingdoms, located in Oldtown would like to use Odoo to manage the training of its future maesters. In this system, the citadel wants to create and edit classes, with different levels. They would like to handle different sessions given by different maesters at different moments. It would be nice to register the attendees of those sessions. Maester Aemon thinks it would be a good idea to differentiate the sessions in preparation from the ones that will actually be given, as well as having a way to archive the sessions, so they can find what they need as quickly as you can find a book in the Citadel's Library, which is the largest in Westeros.'''

class Citadel(models.Model):

    _description = 'Citadel'
    _name = 'openacademy.citadel' #pick not too much of an easy name
    _order = 'name'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.partner', string = 'Responsible')
    level = fields.Selection([(0, "Beginner"), (1, "Intermediate")])
    session_ids = fields.One2many('openacademy.session', 'citadel_id', string= 'Session')
    master_id = fields.Selection([(0, "Fred"), (1, "John"), (1, "Ann")])
    #my_moment = fields.Many2one('res.country.state', 'Fed. State', domain="[('country_id', '=', country)]")

class Session(models.Model):

    _description = 'My List of Sessions'
    _name = "openacademy.session"
    _order = 'name'

    name = fields.Char(string='Name')
    session = fields.Char(string='session')
    start_datetime = fields.Date(string='Date n Time')
    course_ids = fields.One2many('openacademy.course', 'course_id')
    citadel_id = fields.Many2one('opoenacademy.citadel')


class Course(models.Model):

    _description = 'My List of Courses'
    _name = "openacademy.course"
    _order = 'name'

    name = fields.Char(string='Course Name')
    course_id = fields.Many2one('openacademy.session')
