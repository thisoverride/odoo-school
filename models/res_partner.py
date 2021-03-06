from odoo import api, fields, models


class ResPartner(models.Model):

    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'Gestion des professeurs'

    name = fields.Char('Nom du professeur', required=True)
    class_id = fields.One2many('iut.class', 'teacher_id')
