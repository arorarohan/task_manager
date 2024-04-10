#this is to house the task manager class.
import os
import csv


class TaskManager:
    

    def __init__(self, important_path, general_path, completed_path):
        print("initializing...")
        #ensure we are in the correct directory so it doesn't matter where we run the file from!
        os.chdir(os.path.dirname(__file__))
        wd = os.getcwd()

        #creating instance variables for the full paths of each file
        self.important_path = os.path.join(wd, important_path)
        self.general_path = os.path.join(wd, general_path)
        self.completed_path = os.path.join(wd, completed_path)
        
        #creating files if they do not already exist

        #for important:
        if os.path.exists(self.important_path):
            print(f"identified important items file at {self.important_path}")
        else:
            #creates the file and initializes it!
            with open(self.important_path,'a') as file:
                writer = csv.writer(file)
                writer.writerow(['index','item'])

            print(f"created important items file at {self.important_path}")

        #for general:
        if os.path.exists(self.general_path):
            print(f"identified general items file at {self.general_path}")
        else:
            #creates the file and initializes it!
            with open(self.general_path,'a') as file:
                writer = csv.writer(file)
                writer.writerow(['index','item'])

            print(f"created genreal items file at {self.general_path}")
        
        #for completed:
        if os.path.exists(self.completed_path):
            print(f"identified completed items file at {self.completed_path}")
        else:
            #creates the file and initializes it!
            with open(self.completed_path,'a') as file:
                writer = csv.writer(file)
                writer.writerow(['index','item'])

            print(f"created completed items file at {self.completed_path}")
       

       #for now, we set the number of completed tasks to show at 3. The user can change this preference later on if they want.
        self.completed_tasks_to_show = 3
        #let the user know we have finished setting up and are ready to go
        print("initialized successfully! \n")
        self.overview()
        self.get_action()

    
    def overview(self):
        print("Below is an overview of your current tasks.")

        #first the important tasks
        print("\nYour important tasks:")
        with open(self.important_path,'r') as file:
            important_items = list(csv.reader(file))
            
            #we print out each item in the list, excluding the headers (hence we start at 1)
            for i in range(1,len(important_items)):
                print(" ".join(important_items[i]))
        
        #then the general tasks
        print("\nYour general tasks:")
        with open(self.general_path,'r') as file:
            general_items = list(csv.reader(file))
            
            #we print out each item in the list, excluding the headers (hence we start at 1)
            for i in range(1,len(general_items)):
                print(" ".join(general_items[i]))

        #then the completed tasks (only as many as we intend to show)
        print("\nYour completed tasks:")
        with open(self.completed_path,'r') as file:
            completed_items = list(csv.reader(file))
            
            #we figure out how many items to show, the smallest of either the total number or the max number of items to show
            items_to_show = min(self.completed_tasks_to_show, len(completed_items))
            #we print out each item in the list, excluding the headers (hence we start at 1)
            for i in range(1,items_to_show):
                print(" ".join(completed_items[i]))

    def get_action(self):
        action = input('''
        What would you like to do now? 
        a - add a task to the list 
        c - complete a task 
        p - change the priority of a task 
        u - uncomplete a task 
        x - clear backlog of completed tasks 
        n - change number of tasks to show   
        ''')
        #keep asking for an action until we get a proper action
        while action not in ['a','c','p','u','x','n',]:
            print('invalid action! try again...')
            return self.get_action()
        
        if action == 'a':
            return self.add_task()
        if action == 'c':
            return self.complete_task()
        if action == 'p':
            return self.change_priority()
        if action == 'u':
            return self.uncomplete_task()
        if action == 'x':
            return self.clear_backlog()
        if action == 'n':
            return self.change_number_of_tasks_to_show()

    def add_task(self):
        #this will be used for adding tasks to the list
        pass

    def complete_task(self):
        #this will be used for completing tasks
        pass

    def uncomplete_task(self):
        pass

    def change_priority(self):
        pass

    def clear_backlog(self):
        pass

    def change_number_of_tasks_to_show(self):
        pass