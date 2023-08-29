
# ProcessGuard Library

The **ProcessGuard** library provides a set of functions to manage, monitor, and guard processes on your system.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install the ProcessGuard library, you can use `pip`:

```bash
pip install ProcessGuard
```

## Usage

Import the functions you need from `ProcessGuard` in your Python script:

```python
from ProcessGuard import *

# Use the functions from the library
# ...
```
1. Check if Notepad is running:
   ```python
   if is_running("notepad.exe"):
       print("Notepad is running.")
   else:
       print("Notepad is not running.")
   ```

2. Start a process with arguments (Notepad with a text file):
   ```python
   start_with_arguments("notepad.exe", ["path/to/textfile.txt"])
   ```

3. Monitor a process:
   ```python
   monitored_process = "chrome.exe"
   monitor_process(monitored_process, interval=10)
   ```

4. "Run Always" for a process:
   ```python
   process_name = "notepad.exe"
   process_path = r"C:\Windows\System32\notepad.exe"
   guard(process_name, process_path, True, 0.1)
   ```
## Functions

- `is_running(process_name)`: Check if a process is currently running.
- `start(process_path)`: Start a process.
- `terminate(process_name)`: Terminate a process.
- `guard(process_name, process_path, closetaskmanager, interval)`: Guard and monitor a process.
- `list_running()`: List all currently running processes.
- `get_memory_usage(process_name)`: Get memory usage of a process.
- `get_cpu_usage(process_name)`: Get CPU usage of a process.
- `kill_all(process_name)`: Terminate all instances of a process.
- `restart(process_name, process_path)`: Restart a process.
- `count_running()`: Count the number of running processes.
- `get_process(process_name)`: Get details of a specific process.
- `monitor_process(process_name, interval)`: Monitor the status of a process.
- `start_with_arguments(process_path, arguments)`: Start a process with arguments.


For more examples, check the `examples` directory in this repository.

## Contributing

Contributions to the ProcessGuard library are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

