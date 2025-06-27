# Copyright (c) 2025, Meghwin Dave and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests

class ServiceBooking(Document):
    def on_update(self):

        webhook_url = "https://httpbin.org/post"  # Replace with your webhook.site URL if needed
        payload = {
            "booking_id": self.name,
            "customer_name": self.customer_name,
            "service_type": self.service_type,
            "preferred_datetime": str(self.preferred_datetime),
            "status": getattr(self, "workflow_state", None) or getattr(self, "status", None),
        }
        try:
            response = requests.post(webhook_url, json=payload, timeout=5)
            if response.status_code == 200:
                frappe.logger().info(f"Webhook sent successfully: {response.json()}")
            else:
                frappe.logger().warning(f"Webhook failed: {response.status_code} {response.text}")
        except Exception as e:
            frappe.logger().error(f"Webhook error: {e}")
            
            
        # Check if workflow_state field exists and is set to 'Approved'
        if hasattr(self, 'workflow_state') and self.workflow_state == "Approved":
            # Get customer email (assuming customer is a link to Customer doctype with an email field)
            customer_email = None
            if hasattr(self, 'customer') and self.customer:
                customer_doc = frappe.get_doc("Customer", self.customer)
                customer_email = getattr(customer_doc, 'email_id', None) or "meghwindave04@gmail.com"
            # Fallback: try to get email from a field on this doc
            if not customer_email and hasattr(self, 'email_id'):
                customer_email = self.email_id
            if customer_email:
                frappe.sendmail(
                    recipients=[customer_email],
                    subject="Your Service Booking is Approved!",
                    message="""
                        <p>Dear Customer,</p>
                        <p>Your service booking (ID: {name}) has been <b>approved</b>.</p>
                        <p>Thank you for choosing us!</p>
                        <p>--<br>Service Booking Team</p>
                    """.format(name=self.name),
                )

            frappe.msgprint("Email sent to customer & Data sent to dummy webhook endpoint")
