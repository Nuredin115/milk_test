from odoo import fields, models, Command, api
import logging
_logger = logging.getLogger(__name__)


class PosPreparationDisplayOrder(models.Model):
    _inherit = 'pos_preparation_display.order'
    _description = "Preparation orders"
    def _export_for_ui(self, preparation_display):
        preparation_display_orderlines = []

        for orderline in self.preparation_display_order_line_ids:
            if preparation_display._should_include(orderline):
                preparation_display_orderlines.append({
                    'id': orderline.id,
                    'todo': orderline.todo,
                    'internal_note': orderline.internal_note,
                    'attribute_ids': orderline.attribute_value_ids.ids,
                    'product_id': orderline.product_id.id,
                    'product_name': orderline.product_id.display_name,
                    'product_quantity': orderline.product_quantity,
                    'product_cancelled': orderline.product_cancelled,
                    'product_category_ids': orderline.product_id.pos_categ_ids.ids,
                })

        if preparation_display_orderlines:
            current_order_stage = None

            if self.order_stage_ids:
                filtered_stages = self.order_stage_ids.filtered(lambda stage: stage.preparation_display_id.id == preparation_display.id)
                if filtered_stages:
                    current_order_stage = filtered_stages[-1]
            _logger.info("5555555555555555555555555555555")
            _logger.info(self.pos_order_id.employee_id.name)

            return {
                'id': self.id,
                'pos_order_id': self.pos_order_id.id,
                'create_date': self.create_date,
                # 'responsible': self.create_uid.display_name, 
                'responsible':  self.pos_order_id.employee_id.name,

                'stage_id': current_order_stage.stage_id.id if current_order_stage else None,
                'last_stage_change': current_order_stage.write_date if current_order_stage else self.create_date,
                'displayed': self.displayed,
                'orderlines': preparation_display_orderlines,
                'tracking_number': self.pos_order_id.tracking_number,
            }


