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
                file.close()

            print(f"created important items file at {self.important_path}")

        #for general:
        if os.path.exists(self.general_path):
            print(f"identified general items file at {self.general_path}")
        else:
            #creates the file and initializes it!
            with open(self.general_path,'a') as file:
                file.close()

            print(f"created genreal items file at {self.general_path}")
        
        #for completed:
        if os.path.exists(self.completed_path):
            print(f"identified completed items file at {self.completed_path}")
        else:
            #creates the file and initializes it!
            with open(self.completed_path,'a') as file:
                file.close()

            print(f"created completed items file at {self.completed_path}")
       

       #for now, we set the number of completed tasks to show at 3. The user can change this preference later on if they want.
        self.completed_tasks_to_show = 3
        #let the user know we have finished setting up and are ready to go
        print("initialized successfully! \n")

        #we will print the overview and get actions whenever we are not currently in an action. We also keep the files clear of whitespace.
        while True:
            #self.remove_whitespace(self.important_path)
            #self.remove_whitespace(self.general_path)
            #self.remove_whitespace(self.completed_path)
            self.overview()
            self.get_action()


    
    def overview(self):
        print("Below is an overview of your current tasks.")

        #first the important tasks
        print("\nYour important tasks:")
        with open(self.important_path,'r') as file:
            important_items = list(csv.reader(file))
            
            #we print out each item in the list, excluding the headers (hence we start at 1)
            for i in range(len(important_items)):
                print(" ".join(important_items[i]))
        
        #then the general tasks
        print("\nYour general tasks:")
        with open(self.general_path,'r') as file:
            general_items = list(csv.reader(file))
            
            #we print out each item in the list, excluding the headers (hence we start at 1)
            for i in range(len(general_items)):
                print(" ".join(general_items[i]))

        #then the completed tasks (only as many as we intend to show)
        print(f"\nYour completed tasks (first {self.completed_tasks_to_show}):")

        with open(self.completed_path,'r') as file:
            completed_items = list(csv.reader(file))
            #we figure out how many items to show, the smallest of either the total number or the max number of items to show
            items_to_show = min(self.completed_tasks_to_show, len(completed_items))
            #we print out each item in the list, excluding the headers (hence we start at 1)
            for i in range(items_to_show):
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
        
        #once we have a valid action, let's call the method the user wants.
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
        task_name = input("What is the name of the task you would like to create?\n")

        #if the task name is blank. keep asking for a valid one.
        while task_name == '':
            print("invalid name. just enter something, anything")
            return self.add_task()
        
        #if we have some task name, we ask for a priority:
        task_priority = input('''
        What is the priority of this task?
        i - important
        g - general\n
        ''')

        #screen for a valid input
        while task_priority not in ['i','g']:
            print("Invalid priority level. Let's start over.")
            return self.add_task()
        
        #now we will map this priority to the correct file
        if task_priority == 'i':
            file_to_open = self.important_path
        if task_priority == 'g':
            file_to_open = self.general_path

        #we still need to find the index of item in the file we will be adding to.
        with open(file_to_open,'r') as file:
            items = list(csv.reader(file))
            #in the case that this is the first item
            if items == []:
                index_to_add = 1
            else: #in the case that there are already items, we need to find the max index
                max_index = 0
                #only include actual items in this search, in case we have whitespace (but we shouldn't anymore)
                for item in items:
                    if len(item) == 0:
                        continue
                    elif int(item[0]) > max_index:
                        max_index = int(item[0])
                #whatever the max index is, the index for the added item will be 1 more.
                index_to_add = max_index + 1
        
        #now we have found the index, we will add the items to the file
        with open(file_to_open,'a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow([str(index_to_add), task_name])
            print(f"added {task_name} to {file_to_open}!")
            
        
    def move_task(self, index_to_move, source_file, dest_file):
        #iterate through the source_file and look for the item that is associated with the index provided
        with open(source_file,'r') as source:
            items = list(csv.reader(source))
            print(items)
            #error handling for if there are no items
            if items == []:
                print("the source file is empty, nothing to move!")
                return False
            
            #otherwise, we look for and capture the item with the index_to_move:
            item_to_move = ''
            for item in items:
                #like before, ignore items that aren't valid entries (although this should no longer be an issue)
                if len(item) == 0:
                    print(f"{item} is blank, moving on...")
                    continue
                #assign the actual item as item_to_move if we found it
                elif int(item[0]) == index_to_move:
                    print(f"found the item {item}, storing it...")
                    item_to_move = item[1]
            
        #now suppose the item_to_move has not been found.
        if item_to_move == '':
            print(f"couldn't find any item at index {index_to_move}!")
            return False
            
        #if we've reached this point we have found the item that needs moving. Now we first have to find a place for it in the destination before dropping it in.
        #sounds familar, let's just recycle some existing code.
        with open(dest_file,'r') as dest:
            items = list(csv.reader(dest))
            #in the case that this is the first item
            if items == []:
                index_to_add = 1
            else: #in the case that there are already items, we need to find the max index
                max_index = 0
                #only include actual items in this search, although this should not be a problem anymore
                for item in items:
                    if len(item) == 0:
                        continue
                    elif int(item[0]) > max_index:
                        max_index = int(item[0])
                #whatever the max index is, the index for the added item will be 1 more.
                index_to_add = max_index + 1
        
        #now we have found the index, we will add the items to the file
        with open(dest_file,'a',newline='') as dest:
            writer = csv.writer(dest)
            writer.writerow([str(index_to_add), item_to_move])
            print(f"added {item_to_move} to {dest_file}!")

        #now that the item has been copied over, we need to delete the original (ugh)
        #first copy each line of the source file
        lines = []
        with open(source_file,'r') as original_source:
            reader = csv.reader(original_source)
            for row in reader:
                lines.append(row)
        
        #now overwrite the source file with every line except the one we are removing
        with open(source_file,'w',newline='') as new_source:
            writer = csv.writer(new_source)
            for item in lines:
                #ignore whitespace, although this should no longer be an issue
                if len(item) == 0:
                    continue
                elif item[0] != index_to_move:
                    writer.writerow(item)

        #finally, let the user know it's done
        print(f"removed {item_to_move} from {source_file}!")
        return True
        

    def complete_task(self):
        #this will be used for completing tasks
            #ask the user for the priority of the task they want to complete (this will be source_file)
            #ask the user for the index of the task within the approrpiate list (index_to_move)
            #set dest_file to self.completed_path
            #use these arguments with self.move_task()
            #while self.move_task() returns False, we will call self.complete_task() recursively
        pass 
        
    def uncomplete_task(self):
        #similar method to self.complete_task(), this time we will move back to a list based on input from the user.
        pass

    def change_priority(self):
        #this will have a similar approach as self.complete_task() but this time we move it to the other priority list
        pass

    def clear_backlog(self):
        #literally all we have to do here is ask for confirmation, then either:
            #access the completed file in write mode and write nothing (more elegant, idk if this works)
            #delete the completed file entirely and make a new one (will definitely work)
        pass

    def change_number_of_tasks_to_show(self):
        #ask for a new number, if n>0 we update self.completed_tasks_to_show to be the new number.
        pass