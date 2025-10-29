# Python Cybersecurity Scripts

A collection of beginner Python scripts for learning basic cybersecurity concepts. This repository contains several small projects created to explore different areas of security, from network analysis to file forensics.

## Overview

This repository is a toolkit of the following scripts:

* **File Metadata Extractor:** Extracts EXIF data from image files.
* **Linux Network Packet Sniffer:** A simple sniffer to capture and analyze IP packet headers.
* **Open Port Checker:** A basic TCP port scanner to find open ports on a target.
* **Password Hash Cracker:** A dictionary-based cracker for SHA-256 hashes.

## Getting Started

### Prerequisites

* Python 3.x
* `pip` (Python package installer)

### Installation

1.  Clone this repository to your local machine:
    ```bash
    git clone [https://github.com/YOUR-USERNAME/cybersecurity-basic-codes.git](https://github.com/YOUR-USERNAME/cybersecurity-basic-codes.git)
    ```
    *(Remember to replace `YOUR-USERNAME` with your actual GitHub username!)*

2.  Navigate to the project directory:
    ```bash
    cd "cybersecurity basic codes"
    ```

3.  Install the required Python libraries (only `Pillow` is needed):
    ```bash
    # Pillow is used for the metadata extractor
    pip install Pillow
    ```

4.  For the `Password Hash Cracker.py` script, you must create a wordlist file.
    ```bash
    # On Linux/macOS
    touch wordlist.txt

    # On Windows
    echo. > wordlist.txt
    ```
    Then, add some common passwords to `wordlist.txt` (e.g., `password`, `123456`, `admin`).

---
## 🛠️ Scripts Included

### 1. File Metadata Extractor

* **File:** `File Metadata Extractor.py`
* **Description:** Extracts and displays EXIF (Exchangeable Image File Format) metadata from a given image file. This can reveal information like the camera model, date taken, and more.
* **Usage:**
    1.  Open the script and change the `image_path` variable (default: `'test.jpg'`) to point to your image file.
    2.  Run the script:
        ```bash
        python "File Metadata Extractor.py"
        ```

### 2. Linux Network Packet Sniffer

* **File:** `Linux Network Packet Sniffer.py`
* **Description:** A simple packet sniffer that captures network traffic and displays the Protocol, Source IP, and Destination IP for each IP packet.
* **Note:** This script uses `socket.AF_PACKET` and is **for Linux only**.
* **Usage:**
    * This script must be run with superuser privileges to access raw network sockets.
    * Press `Ctrl+C` to stop the sniffer.
    * ```bash
        sudo python "Linux Network Packet Sniffer.py"
        ```

### 3. Open Port Checker

* **File:** `Open Port Checker.py`
* **Description:** A basic TCP port scanner that checks a range of ports on a target IP address to see which ones are open.
* **Usage:**
    1.  Open the script and set the `target_ip`, `port_range_start`, and `port_range_end` variables.
    2.  Run the script:
        ```bash
        python "Open Port Checker.py"
        ```

### 4. Password Hash Cracker

* **File:** `Password Hash Cracker.py`
* **Description:** A simple hash cracker that attempts to find a password by comparing its SHA-256 hash against a wordlist.
* **Usage:**
    1.  Make sure you have a `wordlist.txt` file in the same directory (or update the `wordlist_path` variable in the script).
    2.  Open the script and set the `target_hash` variable to the SHA-256 hash you want to crack.
    3.  Run the script:
        ```bash
        python "Password Hash Cracker.py"
        ```