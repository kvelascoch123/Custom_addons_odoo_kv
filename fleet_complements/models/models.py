# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class FleetComplements(models.Model):
    _name = 'fleet.daily.works.log'

    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehicle", required=True,  default=lambda self: self.env.context.get('vehicle_id'))
    driver_id = fields.Many2one('res.partner', string="Driver", required=True,  default=lambda self: self.env.context.get('driver_id'))
    date_start = fields.Date(string="Start Date", default=lambda self: self.env.context.get('acquisition_date'))
    date_end = fields.Date(string="End Date",  default=lambda self: self.env.context.get('acquisition_date'))
    description = fields.Char(string='Description', size=30)
    base_revenue = fields.Float(string='Base by Revenue',default=0) # Base de ganancia
    qty_dispatched = fields.Float(string='Qty Dispatched')
    qty_returned = fields.Float(string='Qty Returned')
    total_expected = fields.Float(string='Total Expected', compute="_compute_total_expected", default=0) # total esperado
    total_income = fields.Float(string='Total Income', compute="_compute_total_income", default=0) # total ingresos
    total_daily_work = fields.Float(string='Total Daily Work', compute="_compute_total_daily_work", default=0) # total ingresos

    def _compute_total_daily_work(self):
        """ This calculate the  total daily works by qty dispached"""
        for rec in self:
            rec.total_daily_work = (rec.base_revenue * rec.qty_dispatched) - (rec.base_revenue * rec.qty_returned)


    def _compute_total_expected(self):
        for rec in self:
            rec.total_expected = (rec.base_revenue * rec.qty_dispatched)


    def _compute_total_income(self):
        for rec in self:
            rec.total_income = (rec.base_revenue * rec.qty_dispatched) - (rec.base_revenue * rec.qty_returned)

    
class InhFleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    daily_works = fields.Integer(compute="_compute_count_all_complements", string='Odometer')

    def _compute_count_all_complements(self):
        for record in self:
            record.daily_works = 0

    def return_action__daily_works(self):
        """ This opens the xml view specified in xml_id """
        self.ensure_one()
        model_id = self.env.context.get('model_id')
        # raise UserError("KEY CONTEXT" + str(xml_id))
        if model_id:
            return {
            'name': 'Daily Works',
            'type': 'ir.actions.act_window',
            'res_model': model_id , #'fleet.daily.works.log',
            'view_mode': 'tree,form',
            'context': {'vehicle_id': self.id , 'driver_id': self.driver_id.id , 'acquisition_date': self.acquisition_date },
            'domain': [('vehicle_id', '=', self.id) , ('driver_id', '=', self.driver_id.id)],
           
        }
