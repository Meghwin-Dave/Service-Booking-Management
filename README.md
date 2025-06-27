# Service Booking Management

A Frappe app to manage service bookings with workflow, notifications, reporting, and custom print formats.

---

## Features

- **Service Booking DocType**: Manage customer bookings for services (Therapy, Spa, Others).
- **Workflow & Status**: Bookings can be approved, completed, etc. (uses `workflow_state`).
- **Automatic Email Notification**: When a booking is approved, a confirmation email is sent to the customer.
- **Custom Print Format**: Stylish, modern print format for bookings (Jinja/HTML, ready for PDF/print).
- **Script Report**: "Booking Service Summary" report with filters for Service Type and Status, colored status badges, and a bar chart of bookings by service type.
- **REST API/Webhook Integration**: (Optional) Send booking details to any webhook endpoint on update/approval.

---

## Installation

Repo : https://github.com/Meghwin-Dave/Service-Booking-Management

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app service_booking_management
```

---

## Usage & Customizations

### 1. Service Booking DocType
- Fields: Customer, Customer Name, Service Type, Preferred Datetime, Status (workflow_state), etc.
- Service Type options: Therapy, Spa, Others (with custom field for 'Others').

### 2. Workflow & Status
- Status is managed via the `workflow_state` field (e.g., Draft, Approved, Completed).
- You can customize workflow states in the DocType or Workflow settings.

### 3. Automatic Email Notification
- When a booking is approved (`workflow_state` = Approved), a confirmation email is sent to the customer (uses the email from the linked Customer or a direct email field).
- The email uses a simple HTML template (customizable in the Python code).

### 4. Custom Print Format
- A modern, stylish print format is available (Jinja/HTML).
- Includes all key booking details and branding.
- To use: Go to Service Booking > Print Format > New, set type to Jinja, and paste the provided template.

### 5. Booking Service Summary Report
- Script Report with columns: Booking ID, Customer Name, Service Type, Preferred Datetime, Status.
- Filters: Service Type, Status (dropdowns).
- Status column uses colored badges for visual clarity.
- Includes a bar chart showing the count of bookings by Service Type.

### 6. REST API / Webhook Integration (Optional)
- On update/approval, booking details can be sent to any webhook endpoint (e.g., https://httpbin.org/post or webhook.site).
- Example code (in ServiceBooking Python class):

```python
import requests
# ...
if getattr(self, "workflow_state", None) == "Approved":
    webhook_url = "https://httpbin.org/post"
    payload = {
        "booking_id": self.name,
        "customer_name": self.customer_name,
        "service_type": self.service_type,
        "preferred_datetime": str(self.preferred_datetime),
        "status": self.workflow_state,
    }
    requests.post(webhook_url, json=payload, timeout=5)
```

---

## Developer & Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/service_booking_management
pre-commit install
```

Pre-commit is configured to use:
- ruff
- eslint
- prettier
- pyupgrade

---

## License

MIT

---

## Support
For issues, suggestions, or contributions, please open an issue or pull request on GitHub.
