#this is to house the task manager class.
import os #we need this for filepaths
import csv #we need this to interact with our files


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
            self.overview()
            self.get_action()


    
    def overview(self):
        print("Below is an overview of your current tasks.")

        #first the important tasks
        print("\nYour important tasks:")
        with open(self.important_path,'r') as file:
            important_items = list(csv.reader(file))
            
            #we print out each item in the list
            for i in range(len(important_items)):
                print(" ".join(important_items[i]))
        
        #then the general tasks
        print("\nYour general tasks:")
        with open(self.general_path,'r') as file:
            general_items = list(csv.reader(file))
            
            #we print out each item in the list
            for i in range(len(general_items)):
                print(" ".join(general_items[i]))

        #then the completed tasks (only as many as we intend to show)
        if self.completed_tasks_to_show == 10000:
            print("\nYour completed tasks:")
        else:
            print(f"\nYour completed tasks (first {self.completed_tasks_to_show}):")

        with open(self.completed_path,'r') as file:
            completed_items = list(csv.reader(file))
            #we figure out how many items to show, the smallest of either the total number or the max number of items to show
            items_to_show = min(self.completed_tasks_to_show, len(completed_items))
            #we print out each item in the list
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
        elif action == 'c':
            return self.complete_task()
        elif action == 'p':
            return self.change_priority()
        elif action == 'u':
            return self.uncomplete_task()
        elif action == 'x':
            return self.clear_backlog()
        elif action == 'n':
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
            source_items = list(csv.reader(source))

            #error handling for if there are no items
        if source_items == []:
            print("the source file is empty, nothing to move!")
            return False
            
            #otherwise, we look for and capture the item with the index_to_move:
        item_to_move = ''
        for idx in range(len(source_items)):
            if int(source_items[idx][0]) == index_to_move:
                #we are also removing the item from the list so we can write the new one later!
                item_to_move = source_items.pop(idx)
                break

            
        #now suppose the item_to_move has not been found.
        if item_to_move == '':
            print(f"couldn't find any item at index {index_to_move}!")
            return False
            
        #if we've reached this point we have found the item that needs moving. Now we first have to find a place for it in the destination before dropping it in.
        #sounds familar, let's just recycle some existing code.
        with open(dest_file,'r') as dest:
            dest_items = list(csv.reader(dest))

            #in the case that this is the first item
        if dest_items == []:
            index_to_add = 1
        else: #in the case that there are already items, we need to find the max index
            max_index = 0
            #only include actual items in this search, although this should not be a problem anymore
            for item in dest_items:
                if len(item) == 0:
                    continue
                elif int(item[0]) > max_index:
                    max_index = int(item[0])
            #whatever the max index is, the index for the added item will be 1 more.
            index_to_add = max_index + 1
        
        #now we have found the index, we will add the items to the file
        with open(dest_file,'a',newline='') as dest:
            writer = csv.writer(dest)
            writer.writerow([str(index_to_add), item_to_move[1]])

        #now that the item has been copied over, we need to delete the original (ugh)
        #we already have the lines we need, but their numbering is bad, so let's fix it first
        for idx in range(len(source_items)):
            #ignore whitespace, although this should no longer be an issue
            if len(source_items[idx]) == 0:
                continue
            else:
                #renumber the items
                source_items[idx][0] = str(idx+1)

        #now overwrite the source file with our new items
        with open(source_file,'w',newline='') as new_source:
            writer = csv.writer(new_source)
            
            for item in source_items:
                writer.writerow(item)


        #finally, if we've reached this point the operation should be successful. So we return a positive result.
        print(f"moved {item_to_move[1]} successfully!")
        return True
        

    def complete_task(self):
        #by default, our destination file here is our completed file
        dest_file = self.completed_path
        #ask the user for the priority of the task they want to complete (this will be source_file)
        source = input('''
        which priority level are you completing the task from?
        i - important
        g - general
        ''')

        #check the validity of the input
        while source not in ['i','g']:
            print("invalid response, please enter i or g")
            return self.complete_task()
            
        #once we have a valid input, assign the appropriate file to give our mover
        if source == 'i':
            source_file = self.important_path
        elif source == 'g':
            source_file = self.general_path

        #ask the user for the index of the task within the approrpiate list (index_to_move)
        index = input("Enter the index of the task you want to complete:\n")

        #check for valid integer index, the rest will be handled by the mover method
        try:
            index = int(index)
        except ValueError:
            print("please enter a valid integer index!")
            return self.complete_task()

        #use these arguments with self.move_task()
        moved = self.move_task(index, source_file, dest_file)
        #while self.move_task() returns False, we will call self.complete_task() recursively
        while not moved:
            return self.complete_task()
        #if it doesn't return false then it returned true, and our job is done
        return
        
    def uncomplete_task(self):
        #by definition, the source is the completed file
        source_file = self.completed_path
        #give the user the full list of completed tasks, since the one in overview is small
        print("Here is your full list of completed tasks:")
        with open(self.completed_path,'r') as file:
            completed_items = list(csv.reader(file))
            #we print out each item in the list
            for i in range(len(completed_items)):
                print(" ".join(completed_items[i]))

        #now we check which task the user wants to uncomplete
        index = input("Enter the index of the task you want to uncomplete:\n")
        #check for valid integer index, the rest will be handled by the mover method
        try:
            index = int(index)
        except ValueError:
            print("please enter a valid integer index!")
            return self.uncomplete_task()
        
        #now check where this item is meant to go
        dest = input('''
                Which list do you want to move this item back to?
                i - important
                g - general
                ''')
        #check the validity of the input
        while dest not in ['i','g']:
            print("invalid response, please enter i or g")
            return self.uncomplete_task()
        
        #assign a destination file accordingly
        if dest == 'i':
            dest_file = self.important_path
        elif dest == 'g':
            dest_file = self.general_path
        
        #move the task!
        moved = self.move_task(index, source_file, dest_file)
        while not moved:
            return self.uncomplete_task()
        return
        

    def change_priority(self):
        #ask the user for the priority of the task they want to move (this will be source_file)
        source = input('''
        which priority level is the task currently in?
        i - important
        g - general
        ''')

        #check the validity of the input
        while source not in ['i','g']:
            print("invalid response, please enter i or g")
            return self.change_priority()
            
        #once we have a valid input, assign the appropriate files to give our mover
        if source == 'i':
            source_file, dest_file = self.important_path, self.general_path
        elif source == 'g':
            source_file, dest_file = self.general_path, self.important_path

        #ask the user for the index of the task within the approrpiate list (index_to_move)
        index = input("Enter the index of the task you want to move:\n")

        #check for valid integer index, the rest will be handled by the mover method
        try:
            index = int(index)
        except ValueError:
            print("please enter a valid integer index!")
            return self.change_priority()
        
        #the priority level to move to has to be the other list. So we just ask the user for confirmation.
        confirm = input(f"you are moving the item at index {index} in {source_file} to {dest_file}.\nPress y to confirm, or any other button to cancel.\n")
        #return from the method safely if the user does not enter y.
        if confirm != 'y':
            print("Operation cancelled.")
            return

        #if the user confirms, we move on and use the collected arguments with self.move_task()
        moved = self.move_task(index, source_file, dest_file)
        #while self.move_task() returns False, we will call our method again recursively to allow the user to change their input based on the error message given by move_task()
        while not moved:
            return self.change_priority()
        #if it doesn't return false then it returned true, and our job is done
        return

    def clear_backlog(self):
        #first we ask for confirmation.
        confirm = input("This will irreversibly delete all completed tasks! Are you sure? (y/n)\n")
        if confirm != 'y':
            print("Operation cancelled.")
            return
    
        #now with confirmation, we simply open the file in write mode and close it, thus making it empty.
        with open(self.completed_path,'w') as file:
            file.close()
        print("backlog cleared!")
        return
        

    def change_number_of_tasks_to_show(self):
        #ask for a new number, if n>0 we update self.completed_tasks_to_show to be the new number.
        n = input("Enter the maximum number of completed tasks you want to show. Enter 0 to show all of them.\n")

        #now check for a valid input.
        try:
            n = int(n)
        except ValueError:
            print("please enter a valid integer!")
            return self.change_number_of_tasks_to_show()
        
        if n < 0:
            print("How am I supposed to show you a negative number of tasks? Try with a number >= 0")
            return self.change_number_of_tasks_to_show()
        
        #if our input is 0, change the number of tasks to show to be an arbitrarily large number that nobody will reach unless they just have too much going on in thier life, in which case we can't really help them anyway and they ought to be using a better app for this.
        if n == 0:
            self.completed_tasks_to_show = 10000
            print("Got it, all completed tasks will be shown.")
            return

        #if our input is greater than 0, change the number accordingly.
        self.completed_tasks_to_show = n
        print(f"Got it, will show a maximum of {n} tasks from now on.")
        return