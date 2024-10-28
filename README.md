ERPNext Custom App to generate timesheet based on Employee check-ins.
=======
A custom app to create timesheets based on employee check-in and checkout
#### License

mit
>>>>>>> 17d5593 (feat: Initialize App)


# Timesheet Generator

This project provides a custom ERPNext doctype `Settings_TS` that includes functionality for generating timesheets based on employee check-in and check-out logs. It allows users to generate timesheets for a specific date record timestamps of each employee's check-in and calculate the employee's total working hours based on that.

## Features
- Custom `Settings_TS` doctype with a "Generate Timesheet" button.
- Timesheet generation based on check-in and check-out data for each employee.
- Log grouping by "IN" and "OUT" entries within a single timesheet for easy tracking.

## Requirements
- ERPNext version 15.39.3 or higher
- Frappe version 15.45.1 or higher

# Note
Please ignore the "Timesheet is not created" message. The timesheet will be created if there are even number of check-ins. I am working on the error now.
