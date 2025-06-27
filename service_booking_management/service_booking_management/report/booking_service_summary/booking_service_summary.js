// Copyright (c) 2025, Meghwin Dave and contributors
// For license information, please see license.txt

frappe.query_reports["Booking Service Summary"] = {
	"filters": [
		{
			fieldname: "service_type",
			label: "Service Type",
			fieldtype: "Select",
			options: [
				"",
				"Therapy",
				"Spa",
				"Others"
			],
			default: ""
		},
		{
			fieldname: "status",
			label: "Status",
			fieldtype: "Select",
			options: [
				"",
				"Requested",
				"Approved",
				"Completed"
			],
			default: ""
		}
	],
	formatter: function(value, row, column, data, default_formatter) {
		if(column.fieldname === "workflow_state" && value) {
			let color = "gray";
			if(value === "Draft") color = "orange";
			else if(value === "Approved") color = "blue";
			else if(value === "Completed") color = "green";
			return `<span class=\"badge\" style=\"background:${color};color:white;padding:3px 10px;border-radius:8px;\">${value}</span>`;
		}
		return default_formatter(value, row, column, data);
	},
	get_chart_data: function(columns, results) {
		const counts = {};
		results.forEach(row => {
			const type = row[2]; // service_type
			counts[type] = (counts[type] || 0) + 1;
		});
		return {
			labels: Object.keys(counts),
			datasets: [
				{
					name: "Bookings",
					values: Object.values(counts)
				}
			]
		};
	},
	chart: {
		type: 'bar',
		height: 240
	}
};
