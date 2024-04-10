#this will be the script run by the user
from taskmanager import TaskManager



#constants
IMPORTANT_PATH = "lists\important.csv"
GENERAL_PATH = "lists\general.csv"
COMPLETED_PATH = "lists\completed.csv"



if __name__ == "__main__":
    manager = TaskManager(IMPORTANT_PATH,GENERAL_PATH,COMPLETED_PATH)
    