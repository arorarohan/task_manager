# task manager python application
yooooo

## features

### user interaction
1. The user can create tasks, and assign them priority (important/not important)
2. the user can move tasks to "completed" - these can be stored in a csv file which the user can use a command to clear
3. the user can set a number of "completed" tasks to show: default can be 3?

### display
1. on startup and after every interaction, an "overview" will be printed, showing the important tasks, followed by general tasks, followed by last n completed tasks.
2. There will also be a list of commands the user can enter with short explanations.    

## plan
- Object-oriented structure
- TaskManager will be a class
- On initialization, we will assign instance variables to the filepath of each list file if it exists, if it does not exist, create it!

### class methods
- self.overview(): show the overview
- self.add_task(): add a task to either "important" or "general"
- self.complete_task(): select a task (based on index) and move it to "completed"
- self.uncomplete_task(): select a completed task (based on index) and move it to its original location
- self.change_priority(): select a task (based on index) and change its priority
- self.clear_backlog(): clear "completed" (delete all info in the file) --> ask the user for confirmation first!
- self.get_action(): ask a user what they want to do!

### helper functions