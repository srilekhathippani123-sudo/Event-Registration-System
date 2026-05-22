# Event Registration System

class Event:
    def __init__(self, event_name, max_participants):
        self.event_name = event_name
        self.max_participants = max_participants
        self.participants = []

    def register_participant(self, name):
        if len(self.participants) < self.max_participants:
            self.participants.append(name)
            print(f"{name} registered successfully for {self.event_name}.")
        else:
            print("Registration full!")

    def cancel_registration(self, name):
        if name in self.participants:
            self.participants.remove(name)
            print(f"{name}'s registration cancelled.")
        else:
            print(f"{name} is not registered.")

    def show_participants(self):
        print(f"\nParticipants for {self.event_name}:")
        if self.participants:
            for idx, participant in enumerate(self.participants, start=1):
                print(f"{idx}. {participant}")
        else:
            print("No participants registered yet.")

    def available_slots(self):
        slots = self.max_participants - len(self.participants)
        print(f"Available slots: {slots}")


# Main Program
def main():
    event = Event("Python Workshop", 5)

    while True:
        print("\n--- Event Registration System ---")
        print("1. Register Participant")
        print("2. Cancel Registration")
        print("3. Show Participants")
        print("4. Show Available Slots")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter participant name: ")
            event.register_participant(name)

        elif choice == "2":
            name = input("Enter participant name to cancel: ")
            event.cancel_registration(name)

        elif choice == "3":
            event.show_participants()

        elif choice == "4":
            event.available_slots()

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
