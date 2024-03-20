import queue

class PatientScheduler:
    def __init__(self):
        self.patient_queue = queue.Queue()

    def register_patient(self):
        patient_name = input("Enter patient name: ")
        self.patient_queue.put(patient_name)
        print(f"Patient '{patient_name}' registered successfully.")

    def remove_patient(self):
        if not self.patient_queue.empty():
            removed_patient = self.patient_queue.get()
            print(f"Patient '{removed_patient}' has met the doctor and is removed from the queue.")
        else:
            print("No patients in the queue.")

    def display_patient_queue(self):
        if not self.patient_queue.empty():
            print("Current patient queue:")
            for patient in list(self.patient_queue.queue):
                print(f"- {patient}")
        else:
            print("No patients in the queue.")

def main():
    scheduler = PatientScheduler()

    while True:
        print("\nMenu:")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            scheduler.register_patient()
        elif choice == '2':
            scheduler.remove_patient()
        elif choice == '3':
            scheduler.display_patient_queue()
        elif choice == '4':
            print("Exiting the program. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
