#בס"ד
import psutil
import time
import subprocess
import os
import getpass


def is_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False


def start(process_path):
    try:
        subprocess.Popen([process_path])
    except Exception as e:
        print(f"An error occurred while starting the process: {e}")


def terminate(process_name):
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                os.kill(process.info['pid'], psutil.signal.SIGTERM)
                return
    except Exception as e:
        print(f"An error occurred while terminating the process: {e}")



def guard(process_name, process_path,closetaskmanger,interval=5):

    while True:
        if closetaskmanger and  is_running("Taskmgr.exe"):
            terminate("Taskmgr.exe")
        if not is_running(process_name):
            start(process_path)


        time.sleep(interval)
def list_running():
    for process in psutil.process_iter(['pid', 'name']):
        print(f"PID: {process.info['pid']}, Name: {process.info['name']}")


def get_memory_usage(process_name):
    for process in psutil.process_iter(['pid', 'name', 'memory_info']):
        if process.info['name'] == process_name:
            memory_usage = process.info['memory_info'].rss / (1024 * 1024)  # Convert to MB
            return memory_usage
    return None


def get_cpu_usage(process_name):
    for process in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        if process.info['name'] == process_name:
            cpu_usage = process.info['cpu_percent']
            return cpu_usage
    return None


def kill_all(process_name):
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                os.kill(process.info['pid'], psutil.signal.SIGTERM)
    except Exception as e:
        print(f"An error occurred while terminating processes: {e}")


def restart(process_name, process_path):
    terminate(process_name)
    start(process_path)


def count_running():
    count = 0
    for process in psutil.process_iter(['name']):
        count += 1
    return count

def get_process(process_name):
    for process in psutil.process_iter(['pid', 'name', 'memory_info', 'cpu_percent']):
        if process.info['name'] == process_name:
            return {
                'pid': process.info['pid'],
                'memory_usage': process.info['memory_info'].rss / (1024 * 1024),  # MB
                'cpu_usage': process.info['cpu_percent']
            }
    return None


def monitor_process(process_name, interval=5):
    while True:
        if is_running(process_name):
            print(f"Process '{process_name}' is running.")
        else:
            print(f"Process '{process_name}' is not running.")
        time.sleep(interval)


def start_with_arguments(process_path, arguments):
    try:
        subprocess.Popen([process_path, *arguments])
        print(f"Started the process at '{process_path}' with arguments {arguments}.")
    except Exception as e:
        print(f"An error occurred while starting the process: {e}")

