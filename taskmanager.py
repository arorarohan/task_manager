#this is to house the task manager class.
import os



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
            print(f"identified  important items file at {self.important_path}")
        else:
            #creates the file!
            with open(self.important_path,'a') as file:
                file.close
            print(f"created important items file at {self.important_path}")

        #for general:
        if os.path.exists(self.general_path):
            print(f"identified  general items file at {self.general_path}")
        else:
            #creates the file!
            with open(self.general_path,'a') as file:
                file.close
            print(f"created general items file at {self.general_path}")
        
        #for completed:
        if os.path.exists(self.completed_path):
            print(f"identified  completed items file at {self.completed_path}")
        else:
            #creates the file!
            with open(self.completed_path,'a') as file:
                file.close
            print(f"created completed items file at {self.completed_path}")
       
        #self.overview
        #self.get_action

    
    def overview(self):
        #this will be used for generating the overview of tasks that the user sees
        pass

    def get_action(self):
        #this will be used to ask the user for inputs in the main overview screen
        pass

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