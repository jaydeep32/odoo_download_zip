from odoo import models


class HrPayslipRun(models.Model):
    _inherit = "hr.payslip.run"

    def download_zip(self):
        return {
            'type': 'ir.actions.act_url',
            'url': f'/payroll/download_document?id={self.id}',
            'target': 'new',
        }
