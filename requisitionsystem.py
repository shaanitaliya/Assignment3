class RequisitionSystem:
    requisition_id = 10000 
    requisition_submitted = 0 
    approved = 0
    pending = 0
    not_approved = 0

    def __init__(self):
        global requisition_submitted
        self.staff_name = input("Enter the staff name: ")
        self.date = input("Enter the date (DD-MM-YYYY): ")
        self.staff_id = input("Enter the staff ID: ")

        RequisitionSystem.requisition_id += 1
        self.requisition_id = RequisitionSystem.requisition_id
        self.items = []  
        print ("Requisition ID:", self.requisition_id)

        self.requisition_data = {
            "name": self.staff_name,
            "date": self.date,
            "staff_id": self.staff_id,
            "requisition_id": self.requisition_id
        }

    def requisitions_detail(self):

        total = 0
        while True:
            item = input("Enter the food item (type 'done' to finish): ")
            if item.lower() == "done":
                print("THE END")
                break
            else:
                price = int(input(f"Enter the price for '{item}': "))
                total += price
                self.items.append((item, price))
        return total

    def requisition_approval(self):
        global approved, pending, not_approved
        total = self.requisitions_detail()
        reference_id = self.staff_id + str(self.requisition_id)[-3:]

        if total == 0:
            status = "Not Approved"
            RequisitionSystem.not_approved += 1
        elif total < 500:
            status = "Approved"
            RequisitionSystem.approved += 1
        else:
            def respond_requsition():
                response = input("the request is pending Do you want to approve the request? (yes or no): ")
                if response.lower() == "yes":
                    RequisitionSystem.approved += 1
                elif response.lower() == "no":
                    RequisitionSystem.not_approved += 1
                else:
                    status = "Pending"
                    RequisitionSystem.pending += 1
            respond_requsition()

        print("Total:", total)
        print("Status:", status)

        return {
            "status": status,
            "refference_id": reference_id,
            "total": total
        }

    def display_requisitions(self):
        info = self.requisition_approval()

        print("\n-------------------\n  ***************\n-------------------\n")
        print("Printing Requisition Details:")
        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("\nItems Requested:")
        for item, price in self.items:
            print(f"{item}: ${price}")
        print("Total:", info["total"])
        print("Status:", info["status"])
        print("Approval Reference Number:", info["refference_id"])
        print("\n-------------------\n  **THANK YOU**\n-------------------\n")
        # It is for counting the number of requisitions
        RequisitionSystem.requisition_submitted += 1

        # For another input of data I just Reusing the code
        more_info = input("Do you want to add another data 'yes or 'no':")
        if more_info == "yes":
            self.__init__()
            self.requisition_approval()
        elif more_info == "no":
            print("The total number of requisitions submitted:", RequisitionSystem.requisition_submitted)
            print("The total number of approved requisitions:", RequisitionSystem.approved)
            print("The total number of pending requisitions:", RequisitionSystem.pending)
            print("The total number of not approved requisitions:", RequisitionSystem.not_approved)
            print("Thank you for using the Requisition System.")

info = RequisitionSystem()
info.display_requisitions()

