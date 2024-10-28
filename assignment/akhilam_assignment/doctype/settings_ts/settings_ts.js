// Copyright (c) 2024, Alfiya Hussain and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Settings_TS", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Settings_TS', {
    refresh: function(frm) {
        frm.add_custom_button(__('Generate Timesheet'), function() {
            // Perform the desired action: call the Python method to generate the timesheet
            frappe.call({
                method: "assignment.akhilam_assignment.doctype.settings_ts.settings_ts.generate_timesheet",  // Update with the correct method path
                args: {
                    activity_type: frm.doc.activity_type,
                    date: frm.doc.date
                },
                callback: function(r) {
                    if (r.message) {
                        frappe.msgprint(__('Timesheet created successfully.'));
                    } else {
                        frappe.msgprint(__('No timesheet was created.'));
                    }
                }
            });
        });
    }
});
