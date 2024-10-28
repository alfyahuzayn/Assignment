import frappe
from frappe.utils import getdate

@frappe.whitelist()
def create_timesheet(date, activity_type):
    # Fetch employee check-in and check-out data for the selected date
    checkin_data = frappe.get_all("Employee Checkin", filters={
        "date": getdate(date)
    }, fields=["employee", "checkin", "checkout"])

    for entry in checkin_data:
        # Create a new Timesheet for each check-in and check-out
        timesheet = frappe.get_doc({
            "doctype": "Timesheet",
            "employee": entry.employee,
            "activity_type": activity_type,
            "start_time": entry.checkin,
            "end_time": entry.checkout,
        })
        timesheet.insert()

    frappe.db.commit()
