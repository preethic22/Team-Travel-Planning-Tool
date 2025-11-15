from datetime import datetime

print("Hi! Welcome to the Sports Team Travel Plan Agency")


class TravelPlan:
    def __init__(self, plan_id, destination, start_date, end_date, transport_mode):
        self.plan_id = plan_id
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.transport_mode = transport_mode
        self.expenses = {}  # Dictionary to hold expenses

    def add_expense(self, expense_type, amount):
        """Add an expense to the travel plan."""
        if expense_type in self.expenses:
            self.expenses[expense_type] += amount
        else:
            self.expenses[expense_type] = amount
        print(f"Added {amount} to {expense_type} expenses.")

    def view_expenses(self):
        """View all expenses for the travel plan."""
        if not self.expenses:
            print("No expenses recorded for this travel plan.")
            return
        print("Expenses for Travel Plan ID:", self.plan_id)
        for expense_type, amount in self.expenses.items():
            print(f"{expense_type}: {amount}")

    def _str_(self):
        return (f"Plan ID: {self.plan_id}, "
                f"Destination: {self.destination}, "
                f"Start Date: {self.start_date}, "
                f"End Date: {self.end_date}, "
                f"Transport Mode: {self.transport_mode}")


class Team:
    def __init__(self, team_id, team_name):
        self.team_id = team_id
        self.team_name = team_name
        self.travel_plans = []

    def add_travel_plan(self, travel_plan):
        self.travel_plans.append(travel_plan)

    def _str_(self):
        return f"Team ID: {self.team_id}, Team Name: {self.team_name}, Travel Plans: {len(self.travel_plans)}"


class Admin:
    def __init__(self):
        self.teams = {}

    def create_team(self, team_id, team_name):
        """Create a new team."""
        if team_id not in self.teams:
            self.teams[team_id] = Team(team_id, team_name)
            print(f"Team '{team_name}' created successfully.")
        else:
            print(f"Team ID {team_id} already exists.")

    def read_team(self, team_id):
        """View details of a team."""
        team = self.teams.get(team_id)
        if team:
            print(team)
            for plan in team.travel_plans:
                print(plan)
                plan.view_expenses()  # Show expenses for each travel plan
        else:
            print(f"Team ID {team_id} not found.")

    def update_team(self, team_id, new_name):
        """Update an existing team's name."""
        team = self.teams.get(team_id)
        if team:
            if team.team_name != new_name:
                team.team_name = new_name
                print(f"Team ID {team_id} updated to '{new_name}'.")
            else:
                print(f"Team ID {team_id} already has the name '{new_name}'.")
        else:
            print(f"Team ID {team_id} not found.")

    def remove_team(self, team_id):
        """Remove a team."""
        if team_id in self.teams:
            del self.teams[team_id]
            print(f"Team ID {team_id} removed successfully.")
        else:
            print(f"Team ID {team_id} not found.")

    def add_travel_plan(self, team_id, plan_id, destination, start_date, end_date, transport_mode):
        """Add a travel plan to a team."""
        team = self.teams.get(team_id)
        if team:
            travel_plan = TravelPlan(plan_id, destination, start_date, end_date, transport_mode)
            team.add_travel_plan(travel_plan)
            print(f"Travel plan added to Team ID {team_id}.")
        else:
            print(f"Team ID {team_id} not found.")

    def update_travel_plan(self, team_id, plan_id, new_destination, new_start_date, new_end_date, new_transport_mode):
        """Update a specific travel plan for a team."""
        team = self.teams.get(team_id)
        if team:
            for plan in team.travel_plans:
                if plan.plan_id == plan_id:
                    plan.destination = new_destination
                    plan.start_date = new_start_date
                    plan.end_date = new_end_date
                    plan.transport_mode = new_transport_mode
                    print(f"Travel plan ID {plan_id} for Team ID {team_id} updated.")
                    return
            print(f"Travel plan ID {plan_id} not found for Team ID {team_id}.")
        else:
            print(f"Team ID {team_id} not found.")


class TeamMember:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def view_team_details(self, admin, team_id):
        team = admin.teams.get(team_id)
        if team:
            print(f"Details for Team '{team.team_name}':")
            print(team)
            for plan in team.travel_plans:
                print(plan)
                plan.view_expenses()  # Show expenses for each travel plan
        else:
            print(f"Team ID {team_id} not found.")


class SportsTeamTravelAgency:
    def __init__(self):
        self.admin = Admin()
        self.team_members = {}

    def register_team_member(self, user_id, name):
        if user_id not in self.team_members:
            self.team_members[user_id] = TeamMember(user_id, name)
            print(f"Team Member '{name}' registered successfully.")
        else:
            print("User  ID already exists.")

    def show_menu(self):
        print("\n--- Sports Team Travel Plan Agency ---")
        print("1. Admin Operations")
        print("2. Team Member Operations")
        print("3. Exit")

    def admin_menu(self):
        print("\n1. Create Team")
        print("2. Read Team")
        print("3. Update Team Name")
        print("4. Remove Team")
        print("5. Add Travel Plan")
        print("6. Update Travel Plan")
        print("7. Add Expense to Travel Plan")
        print("8. Go Back")

    def team_member_menu(self):
        print("\n1. View Team Details by Team ID")
        print("2. Go Back")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")

            if choice == '1':  # Admin Operations
                while True:
                    self.admin_menu()
                    choice = input("Enter your choice: ")

                    if choice == '1':  # Create Team
                        team_id = input("Enter team ID: ")
                        team_name = input("Enter team name: ")
                        self.admin.create_team(team_id, team_name)
                    elif choice == '2':  # Read Team
                        team_id = input("Enter team ID to view: ")
                        self.admin.read_team(team_id)
                    elif choice == '3':  # Update Team Name
                        team_id = input("Enter team ID to update: ")
                        new_name = input("Enter new team name: ")
                        self.admin.update_team(team_id, new_name)
                    elif choice == '4':  # Remove Team
                        team_id = input("Enter team ID to remove: ")
                        self.admin.remove_team(team_id)
                    elif choice == '5':  # Add Travel Plan
                        team_id = input("Enter team ID to add travel plan: ")
                        plan_id = input("Enter travel plan ID: ")
                        destination = input("Enter destination: ")
                        start_date = input("Enter start date (YYYY-MM-DD): ")
                        end_date = input("Enter end date (YYYY-MM-DD): ")
                        transport_mode = input("Enter transport mode: ")
                        self.admin.add_travel_plan(team_id, plan_id, destination, start_date, end_date, transport_mode)
                    elif choice == '6':  # Update Travel Plan
                        team_id = input("Enter team ID to update travel plan: ")
                        plan_id = input("Enter travel plan ID to update: ")
                        new_destination = input("Enter new destination: ")
                        new_start_date = input("Enter new start date (YYYY-MM-DD): ")
                        new_end_date = input("Enter new end date (YYYY-MM-DD): ")
                        new_transport_mode = input("Enter new transport mode: ")
                        self.admin.update_travel_plan(team_id, plan_id, new_destination, new_start_date, new_end_date, new_transport_mode)
                    elif choice == '7':  # Add Expense to Travel Plan
                        team_id = input("Enter team ID to add expense: ")
                        plan_id = input("Enter travel plan ID to add expense: ")
                        expense_type = input("Enter expense type (e.g., accommodation, food, transport): ")
                        amount = float(input("Enter amount: "))
                        team = self.admin.teams.get(team_id)
                        if team:
                            for plan in team.travel_plans:
                                if plan.plan_id == plan_id:
                                    plan.add_expense(expense_type, amount)
                                    break
                            else:
                                print(f"Travel plan ID {plan_id} not found for Team ID {team_id}.")
                        else:
                            print(f"Team ID {team_id} not found.")
                    elif choice == '8':  # Go Back
                        break
                    else:
                        print("Invalid choice. Please try again.")

            elif choice == '2':  # Team Member Operations
                user_id = input("Enter your user ID: ")
                if user_id not in self.team_members:
                    names=[0,0,0,0]
                    for i in range(4):
                        names[i] = input(f"Enter your name {i+1}: ")
                    self.register_team_member(user_id, names)

                team_member = self.team_members[user_id]
                while True:
                    self.team_member_menu()
                    choice = input("Enter your choice: ")

                    if choice == '1':  # View Team Details by Team ID
                        team_id = input("Enter team ID to view travel details: ")
                        team_member.view_team_details(self.admin, team_id)
                    elif choice == '2':  # Go Back
                        break
                    else:
                        print("Invalid choice. Please try again.")

            elif choice == '3':  # Exit
                print("Exiting Sports Team Travel Plan Agency.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    agency = SportsTeamTravelAgency()
    agency.run()

