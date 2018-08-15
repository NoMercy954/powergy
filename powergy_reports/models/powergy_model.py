from odoo import api, _, tools, fields, models, exceptions
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from datetime import datetime
from . import amount_to_text


class ReportPurchase(models.Model):
	"""docstring for ReportPurchase"""
	_inherit = 'purchase.order'

	observations= fields.Text(string='Observaciones')
	amount_to_text = fields.Char(compute='_get_amount_to_text', string='Monto en Texto', readonly=True,
                                 help='Amount of the invoice in letter')
	@api.one
	@api.depends('amount_total')
	def _get_amount_to_text(self):
		self.amount_to_text = amount_to_text.get_amount_to_text(self, self.amount_total)


class ReportFactura(models.Model):

	_inherit = 'account.invoice'

	observations= fields.Text(string='Observaciones')


class ReportPago(models.Model):

	_inherit = 'account.payment'

	cambio = fields.Float(string='Tipo Cambio')
