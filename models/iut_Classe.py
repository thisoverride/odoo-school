from odoo import api, fields, models


class IutClasse(models.Model):
	_name = 'iut.class'
	_description = 'Une courte description'

	name = fields.Char('Nom classe')
	level = fields.Selection([('scnd', 'Seconde'), ('prmr', 'Première'),
    ('trmn', 'Terminale'), ], 'Niveau', default='scnd', required=True)
	age = fields.Integer('Date de naissance')

	class_id = fields.Many2one()