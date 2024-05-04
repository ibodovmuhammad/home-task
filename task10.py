def add_task():
    task = {
        "Usarname": input("Usarname-->"),
        "Name": input("Name_task-->"),
        "Time": input("Time-->"),
        "Is_completed ": False
    }
    task_lists.append(task)
task_lists=[]

def get_task():
    for t in task_lists:
        for k,v in t.items():
            print(f"{k}: {v}")


while True:
    choose = input("--->")
    match choose:
        case "add":
            add_task()
        case "get":
            get_task()