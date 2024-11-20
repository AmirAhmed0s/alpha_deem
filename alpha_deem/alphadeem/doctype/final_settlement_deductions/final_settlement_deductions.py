# Copyright (c) 2023, smart solution and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FinalSettlementDeductions(Document):
    def before_save(self):
        # Fetch Employee data based on employee field
        employee = frappe.get_doc("Employee", self.employee)

        # Check if the employee has a clearance form
        if employee.clearance_form:
            # If there is a clearance form, fetch from clearance_form
            clearance_doc = frappe.get_doc("Clearance Form", employee.clearance_form)
            
            # Example: Fetch necessary data from the clearance form
            self.deductions = clearance_doc.deductions  # Assuming `deductions` exists on Clearance Form
            self.amount = clearance_doc.amount  # Assuming `amount` exists on Clearance Form
            self.description = clearance_doc.description  # Assuming `description` exists on Clearance Form
        else:
            # If no clearance form, fetch directly from Employee
            self.deductions = employee.deductions  # Assuming `deductions` exists on Employee
            self.amount = employee.amount  # Assuming `amount` exists on Employee
            self.description = employee.description  # Assuming `description` exists on Employee
