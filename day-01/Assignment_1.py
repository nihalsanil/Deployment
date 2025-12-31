import psutil
def get_cpu_threshold():
    user_cpu_threshold = float(input("Enter the CPU threshold percentage (e.g., 75 for 75%): "))
    current_cpu_usage = psutil.cpu_percent(interval=1)
    if current_cpu_usage > user_cpu_threshold:
        print(f"Warning: CPU usage is at {current_cpu_usage}%, which exceeds the threshold of {user_cpu_threshold}%!")
    else:
        print(f"CPU usage is at {current_cpu_usage}%, which is within the threshold of {user_cpu_threshold}%.")

def get_memory_threshold():
    user_memory_threshold = float(input("Enter the Memory threshold percentage (e.g., 75 for 75%): "))
    current_memory_usage = psutil.virtual_memory().percent
    if current_memory_usage > user_memory_threshold:
        print(f"Warning: Memory usage is at {current_memory_usage}%, which exceeds the threshold of {user_memory_threshold}%!")
    else:
        print(f"Memory usage is at {current_memory_usage}%, which is within the threshold of {user_memory_threshold}%.")  

def get_disk_threshold():
    user_disk_threshold = float(input("Enter the Disk threshold percentage (e.g., 75 for 75%): "))
    current_disk_usage = psutil.disk_usage('/').percent
    if current_disk_usage > user_disk_threshold:
        print(f"Warning: Disk usage is at {current_disk_usage}%, which exceeds the threshold of {user_disk_threshold}%!")
    else:
        print(f"Disk usage is at {current_disk_usage}%, which is within the threshold of {user_disk_threshold}%.")

get_cpu_threshold()
get_memory_threshold()  
get_disk_threshold()