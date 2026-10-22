class Patient:
    __name = ""
    __bill_amount = ""

    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_bill_amount(self):
        return self.__bill_amount
    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount
    def calculate_bill(self):
        final_bill = self.bill_amount
        print(f"Patient Name: {self.name}")
        print(f"Original Bill: ₱{self.bill_amount:,.2f}")
        print(f"Final Bill: ₱{final_bill:,.2f}\n")
        
class SeniorPatient(Patient):
    def calculate_bill(self):
        final_bill = self.bill_amount - self.bill_amount*0.20
        print(f"Patient Name: {self.name}")
        print(f"Original Bill: ₱{self.bill_amount:,.2f}")
        print(f"Final Bill: ₱{final_bill:,.2f}\n")
        

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        final_bill = self.bill_amount - self.bill_amount*0.15
        print(f"Patient Name: {self.name}")
        print(f"Original Bill: ₱{self.bill_amount:,.2f}")
        print(f"Final Bill: ₱{final_bill:,.2f}\n")
        
print("Hospital Billing System")
print("-----------------------")
regular_patient = Patient("Juan Dela Cruz", 15000)
regular_patient.calculate_bill()
senior_patient = SeniorPatient("Maria Santos", 15000)
senior_patient.calculate_bill()
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)
philhealth_patient.calculate_bill()

