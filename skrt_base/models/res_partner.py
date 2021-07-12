# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.osv import expression


class SkrtResPartner(models.Model):
    _inherit = 'res.partner'

    comercial = fields.Char('Trade name', size=128, index=True)

    @api.depends('comercial')
    def _compute_display_name(self):
        """Include dependencies of comercial"""
        super(SkrtResPartner, self)._compute_display_name()

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        """Include commercial name in direct name search."""
        args = expression.normalize_domain(args)
        for arg in args:
            if isinstance(arg, (list, tuple)):
                if arg[0] == 'name' or arg[0] == 'display_name':
                    index = args.index(arg)
                    args = (
                        args[:index] + ['|', ('comercial', arg[1], arg[2])] +
                        args[index:]
                    )
                    break
        return super(SkrtResPartner, self).search(
            args, offset=offset, limit=limit, order=order, count=count,
        )

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        """Give preference to commercial names on name search, appending
        the rest of the results after. This has to be done this way, as
        Odoo overwrites name_search on res.partner in a non inheritable way."""
        if not args:
            args = []
        partners = self.search(
            [('comercial', operator, name)] + args, limit=limit,
        )
        res = partners.name_get()
        if limit:
            limit_rest = limit - len(partners)
        else:
            # limit can be 0 or None representing infinite
            limit_rest = limit
        if limit_rest or not limit:
            args += [('id', 'not in', partners.ids)]
            res += super(SkrtResPartner, self).name_search(
                name, args=args, operator=operator, limit=limit_rest,
            )
        return res

    def name_get(self):
        result = []
        name_pattern = "%(name)s [%(comercial_name)s]"
        orig_name = dict(super(SkrtResPartner, self).name_get())
        print("\n\n%s\n\n\n"%orig_name)
        for partner in self:
            name = orig_name[partner.id]
            comercial = partner.parent_id and partner.parent_id.comercial\
            		or partner.comercial\
            		or False
            if comercial:
                name = name_pattern % {'name': name,
                                       'comercial_name': comercial}
            result.append((partner.id, name))
        return result