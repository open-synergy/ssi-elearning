# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

from odoo import models


class SlideChannel(models.Model):
    _inherit = [
        "slide.channel",
        "mixin.task",
    ]
    _task_create_page = True
    _task_page_xpath = "//page[1]"
    _task_template_position = "after"
