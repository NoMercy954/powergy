from odoo import api, _, tools, fields, models, exceptions
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from datetime import datetime
from . import amount_to_text

class FieldsResPartner(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'
	
	clabe_banco = fields.Char(string='CLABE', help='Aqui puedes ingresar tu CLABE de tu cuenta bancaria')