#this will be the script run by the user
from taskmanager import TaskManager



#constants, you can choose the relative filepaths (to this file) of the lists you want here.
IMPORTANT_PATH = "lists\important.csv"
GENERAL_PATH = "lists\general.csv"
COMPLETED_PATH = "lists\completed.csv"


#runs the program only if this script was run directly
if __name__ == "__main__":
    manager = TaskManager(IMPORTANT_PATH,GENERAL_PATH,COMPLETED_PATH)