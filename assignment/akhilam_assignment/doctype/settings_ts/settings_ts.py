# Copyright (c) 2024, Alfiya Hussain and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Settings_TS(Document):
	pass


import frappe

@frappe.whitelist()
def generate_timesheet(activity_type, date):
    # Log the function call
    print(f"Generating timesheet for Activity Type: {activity_type} on Date: {date}")

    # Get the list of employees
    employees = frappe.get_all("Employee")
    if not employees:
        print("No employees found.")
        return

    for emp in employees:
        # Fetch check-in and check-out records for the employee on the specified date
        checkins = frappe.get_all("Employee Checkin",
                                   filters={"employee": emp.name, "time": ["between", [f"{date} 00:00:00", f"{date} 23:59:59"]]},
                                   order_by="time",
                                   fields=["name", "employee", "log_type", "time"])

        if not checkins:
            print(f"No check-ins found for Employee: {emp.name} on Date: {date}")
            continue

        # Create a new timesheet
        timesheet = frappe.new_doc("Timesheet")
        timesheet.employee = emp.name
        timesheet.activity_type = activity_type
        timesheet.start_date = date

        in_time = None
        for entry in checkins:
            if entry.log_type == "IN":
                in_time = entry.time
                print(f"Check-in for {emp.name}: {in_time}")
            elif entry.log_type == "OUT" and in_time:
                timesheet.append("time_logs", {
                    "from_time": in_time,
                    "to_time": entry.time,
                    "activity_type": activity_type
                })
                print(f"Check-out for {emp.name}: {entry.time}")
                in_time = None

        # Check if any time logs were added
        if timesheet.get("time_logs"):
            # Save the timesheet
            timesheet.insert()
            frappe.db.commit()
            print(f"Timesheet created for Employee: {emp.name}")
        else:
            print(f"No time logs to save for Employee: {emp.name}")

    print("Timesheet generation completed.")
