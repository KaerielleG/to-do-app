class TodoApp:
    def __init__(self):
        self.tasks = []
#create an array
##list/view task fuction, to print all tasks that live in the array
    def add_task(self, title):
        self.tasks.append({"title": title, "status": "Incomplete"})
        print(f"Task '{title}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task['title']} - {task['status']}")

    def mark_task_complete(self, task_number):
        try:
            self.tasks[task_number - 1]["status"] = "Complete"
            print(f"Task {task_number} marked as complete.")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, task_number):
        try:
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['title']}' deleted.")
        except IndexError:
            print("Invalid task number.")

    def quit_app(self):
        print("Thank you for using the To-Do List App. Goodbye 👋🏽 👋🏽!")
        exit()
#create a main method
#Create a lopp to run the app
    def run(self):
        print("Welcome to the To-Do List App!")
        while True:
            print("\nMenu:")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Mark a task as complete")
            print("4. Delete a task")
            print("5. Quit")

            try:
                choice = int(input("Select an option (1-5): "))
                if choice == 1:
                    title = input("Enter the task title: ")
                    self.add_task(title)
                elif choice == 2:
                    self.view_tasks()
                elif choice == 3:
                    task_number = int(input("Enter the task number to mark as complete: "))
                    self.mark_task_complete(task_number)
                elif choice == 4:
                    task_number = int(input("Enter the task number to delete: "))
                    self.delete_task(task_number)
                elif choice == 5:
                    self.quit_app()
                else:
                    print("Please select a valid option (1-5).")
            except ValueError:
                print("Invalid input. Please enter a number (1-5).")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            finally:
                print("Returning to menu...")

if __name__ == "__main__":
    app = TodoApp()
    app.run()
