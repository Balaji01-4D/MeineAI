# MEINE AI

**MEINE AI** is a OFFLINE NLP based CLI application designed for file and system management. It allows users to execute operations like file creation, deletion, moving, copying, and more, while also providing detailed system information. Utilizing NLP, MEINEAI can understand and interpret user commands to perform tasks such as identifying file names and specific operations.

## Features

- **NLP Integration**: Understands user commands and extracts relevant information for seamless task execution.
- **File Operations**: Create, delete, move,details ,rename,hide and copy files with ease.
- **System Information**: Displays detailed information about CPU, GPU, memory, disk partitions, network, environmental variables, and more.
- **User-Friendly Interface**: Provides a clean, tabulated display with the help of `tabulate` and `rich` modules.



## Dependencies

Ensure you have the following Python libraries installed:

- `rich`
- `spacy`
- `psutil`
- `os` (builtin)
- `tabulate`
- `pathlib` (builtin)
- `subprocess`




## Contributing

Contributions are welcome! If you'd like to contribute to MEINEAI, please fork the repository and submit a pull request. You can also open issues for feature requests or bug reports.

Here's an updated **Commands** section based on your examples with varied names and paths:  

---

Here’s the updated **Commands** section with system-related commands:  

---

## Basic Usage  

### File Operations  

- **Delete a file**:  
  ```bash
  >>> delete (or) del the Downloads/report.docx
  ```  

- **Create a new file**:  
  ```bash
  >>> create (or) mk the home/user/notes.txt
  ```  

- **Move a file to another directory**:  
  ```bash
  >>> move (or) mv the photo.jpg to Pictures
  ```  

- **Copy a file to a new location**:  
  ```bash
  >>> copy (or) cp the data.csv to Documents
  ```  

---

### System Information Commands  

- **Retrieve IP address**:  
  ```bash
  >>> my ip? (or) ip
  ```  
  **Output**:  
  ```
  ╒═════════════╤═══════════╕
  │ Hostname    │ MEINEAI   │
  ├─────────────┼───────────┤
  │ IP Address  │ 127.0.1.1 │
  ╘═════════════╧═══════════╛
  ```  

- **Check RAM usage**:  
  ```bash
  >>> ram
  ```  
  **Output**:  
  ```
  Used RAM:   [███████████████████      ] 75% (6 GB)
  Free RAM:   [██████                  ] 25% (2 GB)
  ```



- **Get PC details**:  
  ```bash
  >>> pc (or) sys
  ```  
  **Output**:  
  ```
  [OS Information]
  ╒═══════════╤═════════════════════════════════════════════════════════════╕
  │ NAME      │ INFO                                                        │
  ╞═══════════╪═════════════════════════════════════════════════════════════╡
  │ System    │ Linux                                                       │
  ├───────────┼─────────────────────────────────────────────────────────────┤
  │ Node Name │ balaji-pc                                                   │
  ├───────────┼─────────────────────────────────────────────────────────────┤
  │ Release   │ 6.8.0-31-generic                                            │
  ├───────────┼─────────────────────────────────────────────────────────────┤
  │ Version   │ #31-Ubuntu SMP PREEMPT_DYNAMIC Sat Apr 20 00:40:06 UTC 2024 │
  ├───────────┼─────────────────────────────────────────────────────────────┤
  │ Machine   │ x86_64                                                      │
  ├───────────┼─────────────────────────────────────────────────────────────┤
  │ Processor │ x86_64                                                      │
  ╘═══════════╧═════════════════════════════════════════════════════════════╛
  ```
- **Get Battery info**:
  ```bash
    >>> battery (or) bt 
  ```
  **Output**:  
  ```
    BATTERY % ━━━━━━━━━━━━━━━━━━━━━━━━━━╺━━━  87%
    Battery Status: Not Charging
  ```
  - **Get Battery info**:
  ```bash
    >>> Disk (or) Storage

  ```
  **Output**:  
  ```
    ╒════════════╤══════════════╤══════════╤═══════════╤═════════╕
    │ Device     │ Total Size   │ Used     │ Free      │ Usage   │
    ╞════════════╪══════════════╪══════════╪═══════════╪═════════╡
    │ /dev/sda2  │ 291.31 GB    │ 86.96 GB │ 189.49 GB │ 31.5%   │
    ├────────────┼──────────────┼──────────┼───────────┼─────────┤
    │ /dev/sda1  │ 1.05 GB      │ 0.01 GB  │ 1.04 GB   │ 0.6%    │
    ╘════════════╧══════════════╧══════════╧═══════════╧═════════╛
  ```
---  



## Acknowledgments

- **`rich`**: For enhancing the CLI interface with beautiful formatting and color support.
- **`tabulate`**: For presenting data in a structured table format.
- **`spaCy`**: For natural language processing capabilities.
- **`Pathlib`**: For File Path handling.
- **`shutil`**: For File and directory processing.
- **`os`**: For File,system and directory processing.
- **`subprocess`**: For creating a new Subprocesses for complex shell command.

