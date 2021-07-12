# -*- coding: utf-8 -*-

from odoo import api, fields, models
from ast import literal_eval as e

class SkrtCrmLead(models.Model):
    _inherit = 'crm.lead'

    def action_sale_quotations_new(self):
    	action = super(SkrtCrmLead, self).action_sale_quotations_new()
    	context = action.get('context', {})
    	context = e(context) if isinstance(context, str) else context
    	context.update({'default_user_id': self.user_id.id or False})
    	action['context'] = context
    	print("\n\n\n action: %s \n\n\n\n"%context)
    	return action