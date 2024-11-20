# Copyright (c) 2023, smart solution and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class FinalSettlementEntitlements(Document):
    def before_save(self):
        # Fetch Employee data based on employee field
        employee = frappe.get_doc("Employee", self.employee)

        # Check if the employee has a clearance form
        if employee.clearance_form:
            # If there is a clearance form, fetch from clearance_form
            clearance_doc = frappe.get_doc("Clearance Form", employee.clearance_form)
            
            # Example: Fetch necessary data from the clearance form
            self.entitlements = clearance_doc.entitlements if clearance_doc.entitlements else None
            self.amount = clearance_doc.amount if clearance_doc.amount else None
            self.description = clearance_doc.description if clearance_doc.description else None
            self.from_date = clearance_doc.from_date if clearance_doc.from_date else None
            self.to = clearance_doc.to_date if clearance_doc.to_date else None
        else:
            # If no clearance form, fetch directly from Employee
            self.entitlements = employee.entitlements if employee.entitlements else None
            self.amount = employee.amount if employee.amount else None
            self.description = employee.description if employee.description else None
            self.from = employee.from_date if employee.from_date else None
            self.to = employee.to_date if employee.to_date else None
