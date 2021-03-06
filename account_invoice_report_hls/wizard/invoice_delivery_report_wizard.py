# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class InvoiceDeliveryReportWizard(models.TransientModel):
    _name = "invoice.delivery.report.wizard"

    def print_invoice_delivery_report(self):
        context = dict(self.env.context)
        # here we only handle one invoice record
        invoice = self.env["account.invoice"].browse(context.get("active_ids"))[0]
        report_ref = "account_invoice_report_hls.invoice_delivery_report"
        if context.get("format") == "odt":
            report_ref = "account_invoice_report_hls." "invoice_delivery_report_odt"
        report_id = self.env["invoice.delivery.report"]._create_invoice_delivery_report(
            invoice
        )
        return self.env.ref(report_ref).report_action([report_id])
