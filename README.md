# Python Port Scanner (cmd_full_scan.py)

A simple, fast, and reliable port scanner written in Python, designed to be run in a Linux/Termux environment.

## Features
- Scans a single target IP address.
- Checks ports 1 through 100.
- Reports open ports.

## Installation

This tool requires Python 3.

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Termuxcmd/CMD-python-port-scanner-.git
   cd CMD-python-port-scanner-
2. **Make the script executable:**
       ```bash
       chmod +x full_scan.py
       ```

    ## Usage

    Run the script directly and enter the target IP when prompted.

    ```bash
    ./full_scan.py
    ```

    ## Example Output

    ```
    Enter the target IP address: 192.168.1.1
    --------------------------------------------------
    Scanning target: 192.168.1.1
    Time started: 2025-11-16 10:01:02.585412
    --------------------------------------------------
    Port 22: Open
    Port 80: Open
    Scan finished at: 2025-11-16 10:01:03.123456
    ```
    ```

3.  **Save and Exit:** (Ctrl+O, Enter, Ctrl+X)