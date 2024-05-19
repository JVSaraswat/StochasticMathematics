# Turning the display dark turns the pc into a more friendly scheduling system.
import datetime
import subprocess


def schedule_task(starting_time, task):
    current_time = datetime.datetime.now()

    while current_time < starting_time:
        current_time = datetime.datetime.now()

    execute(task)


class Task:
    name = ""
    script_path = ""


def execute(task):
    try:
        subprocess.run(task, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing the task: nadir {e}")


#Task printDirectory = "Print the name of the directory",


# Example usage:
# Set the starting time in the future and provide the batch script command
start_time = datetime.datetime.now()  # Replace with your desired starting time
batch_script = r"C:\Users\khush\PycharmProjects\webscrapping\venv\openTextinNotepad++.bat"  # Replace with the actual name of your batch script

# Schedule the task
schedule_task(start_time, batch_script)

#result = subprocess.check_output('dir', text=True)
#print(result)