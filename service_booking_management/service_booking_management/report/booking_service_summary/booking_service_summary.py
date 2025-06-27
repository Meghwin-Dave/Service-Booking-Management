# Copyright (c) 2025, Meghwin Dave and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
		{"label": "Booking ID", "fieldname": "name", "fieldtype": "Link", "options": "Service Booking", "width": 120},
		{"label": "Customer Name", "fieldname": "customer_name", "fieldtype": "Data", "width": 180},
		{"label": "Service Type", "fieldname": "service_type", "fieldtype": "Data", "width": 120},
		{"label": "Preferred Datetime", "fieldname": "preferred_datetime", "fieldtype": "Datetime", "width": 160},
		{"label": "Status", "fieldname": "workflow_state", "fieldtype": "Data", "width": 100},
	]

	conditions = []
	values = {}
	if filters:
		if filters.get("service_type"):
			conditions.append("service_type = %(service_type)s")
			values["service_type"] = filters["service_type"]
		if filters.get("status"):
			conditions.append("workflow_state = %(status)s")
			values["status"] = filters["status"]

	where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""

	data = frappe.db.sql(f"""
		SELECT
			name,
			customer_name,
			service_type,
			preferred_datetime,
			workflow_state
		FROM `tabService Booking`
		{where_clause}
		ORDER BY modified DESC
	""", values, as_dict=1)
	
	return columns, data

