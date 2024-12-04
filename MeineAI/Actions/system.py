import os
import datetime as dt
import shutil as sl
from pathlib import Path
from time import ctime
import psutil
from rich.console import Console
import platform
from tabulate import tabulate
from datetime import datetime
import pywifi

console = Console()

from Actions import other

class System:

    def Time(self) -> None :
        print(dt.datetime.now())
    
    def DiskSpace(self, Destination: Path =Path('/')) -> None: 
        total , used , free = sl.disk_usage(Destination)
        data ={
            'FREE' : free / total * 100,
            'USED' : used / total * 100
        }
        other.display_progress(data,'Disk Space')
        print("Total :",other.SizeHelper(total))
        print("Used  :",other.SizeHelper(used))
        print("Free  :",other.SizeHelper(free))
    
    def GetCurrentDir(self) -> None:
        path:Path = Path('.')
        print(f"{path.resolve()}")


    def CD(self, Destination: Path) -> None:
        if (Destination.exists() and Destination.is_dir()):
            try:
                os.chdir(Path)
            except PermissionError:
                print(f"Permission Denied")            
            except Exception:
                print(f"Can't Change directory to {Destination.name}")
        elif (Destination.is_file()):
            print(f"Cant Change {Destination.name} Is File.")
        else:
            print(f"{Destination.name} Not Found.")
    def Info(self, Name : Path) -> None:
        if (not Name.exists()):
            print(f"{Name.name} Not Found")
            return
        size = other.SizeHelper(Name.stat().st_size) 
        stats = Name.stat()
        info : dict =[
            ['Name' , Name.name],
            ['Path' , str(Name.resolve())],
            ['size' , size],
            ['Type' , "File" if (not Name.is_dir()) else "Directory"],
            ['Created' , ctime(stats.st_ctime)],
            ['Last Modified' , ctime(stats.st_mtime)],
            ['Last Accessed' , ctime(stats.st_atime)],
            ['Mode' , stats.st_mode]
        ]
        console.print(tabulate(info,headers=['Attribute','Value'],floatfmt='fancy_grid'))
    
    def IP(self):
        import socket
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        net_info = [
            ["Hostname", hostname],
            ["IP Address", ip_address],
        ]
        console.print(tabulate(net_info, headers=["Attribute", "Value"], tablefmt="fancy_grid"))

    
    def HomeDir(self):
        console.print(f"Home Directory :  ",Path.home())

    def RAMInfo(self):
        memory = psutil.virtual_memory()
        Total = memory.total
        Avail = memory.available
        Used = memory.used
        data: dict = { 
                'AVAILABLE': Avail/Total * 100,
                'USED' : Used/Total * 100
        }
        other.display_progress(data,'Ram Info')
        print(f"Total Memory : {other.SizeHelper(Total)}")
        print(f"Memory Available : {other.SizeHelper(Avail)}")
        print(f"Memory Used : {other.SizeHelper(Used)}")

    def SYSTEM(self):
        os_info = [
        ["System", platform.system()],
        ["Node Name", platform.node()],
        ["Release", platform.release()],
        ["Version", platform.version()],
        ["Machine", platform.machine()],
        ["Processor", platform.processor()],
        ]
        console.print("\n[OS Information]")
        console.print(tabulate(os_info, headers=["NAME", "INFO"], tablefmt="fancy_grid"))

    def Battery(self):
        battery = psutil.sensors_battery()
        if battery:
            other.display_progress({'BATTERY %': round(battery.percent)},'BATTERY')
            console.print(f"[blue]Battery Status: {'Charging' if battery.power_plugged else "Not Charging"}")
        else:
            console.print(f"[blue]No battery information available.")


    def NetWork(self):
        net_info = psutil.net_if_addrs()
        for interface, addresses in net_info.items():
            console.print(f"[blue]Interface: {interface}")
            for address in addresses:
                console.print(f" [blue]Address: {address.address}, Family: {address.family.name}")
            
    def ENV(self):
        env_vars = os.environ
        for key, value in env_vars.items():
            console.print(f"{key}: {value}")

                

    def CPU(self):
        console.print(f"[blue]CPU Count: {psutil.cpu_count(logical=True)}")
        console.print(f"[blue]CPU Usage: {psutil.cpu_percent(interval=1)}%")

    def USER(self):
        import getpass
        console.print(f"[blue]Current User: {getpass.getuser()}")

    def DiskInfo(self):
        disk_info = []
         
        for partition in psutil.disk_partitions():
             
                usage = psutil.disk_usage(partition.mountpoint)
                disk_info.append([
                    partition.device,
                    f"{usage.total / (1024 ** 3):.2f} GB",
                    f"{usage.used / (1024 ** 3):.2f} GB",
                    f"{usage.free / (1024 ** 3):.2f} GB",
                    f"{usage.percent}%",
                ]) 
        console.print(tabulate(disk_info, headers=["Device", "Total Size", "Used", "Free", "Usage"], tablefmt="fancy_grid"))          

    def Processes(self):
        process_list = []

        # Iterate over all running processes
        for proc in psutil.process_iter(attrs=['pid', 'name', 'status', 'memory_info', 'create_time']):
            try:
                pid = proc.info['pid']
                name = proc.info['name']
                status = proc.info['status']
                memory = proc.info['memory_info'].rss / (1024 * 1024)  
                start_time = datetime.fromtimestamp(proc.info['create_time']).strftime("%Y-%m-%d %H:%M:%S")
                cpu_usage = proc.cpu_percent(interval=0.1) 
                process_list.append([pid, name, status, f"{memory:.2f} MB", start_time, f"{cpu_usage:.2f}%"])
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        # Define headers
        headers = ["PID", "Name", "Status", "Memory (RAM)", "Start Time", "CPU Usage (%)"]

        # Print table
        console.print(tabulate(process_list, headers=headers, tablefmt="fancy_grid"))
    
    def ProcessKill(self,pid):
        try:
            process = psutil.Process(pid)
            process.kill()
            print(f"Process with PID {pid} has been terminated.")
        except psutil.NoSuchProcess:
            print(f"No process with PID {pid} exists.")
        except psutil.AccessDenied:
            print(f"Permission denied to terminate the process {pid}.")
        except Exception:
            print(f"Permission denied to terminate the process {pid}")
        
    
    def Scan_Wifi_Window(self) -> None:                                                #window 
        wifi = pywifi.PyWiFi()  
        iface = wifi.interfaces()[0]  

        iface.scan() 
        scan_results = iface.scan_results() 

        wifi_data = []
        for network in scan_results:
            encryption_status = "Locked" if network.akm else "Open"
            wifi_data.append([network.ssid, network.signal, encryption_status])

        headers = ["SSID", "Signal Strength", "Encryption"]
        console.print(tabulate(wifi_data, headers=headers, tablefmt="fancy_grid"))



    def scan_wifi_linux(self) -> None:
        import subprocess
        result = subprocess.run(['nmcli', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            result = subprocess.run(['nmcli', '-t', '-f', 'SSID,SECURITY', 'dev', 'wifi'], stdout=subprocess.PIPE)
            networks = result.stdout.decode('utf-8').strip().split('\n')

            wifi_data = []
            for network in networks:
                if network.strip():  
                    ssid, security = network.split(':', 1)
                    status = "Locked" if security else "Open"
                    wifi_data.append([ssid, status])
            headers = ["SSID", "Security"]
            print(tabulate(wifi_data, headers=headers, tablefmt="fancy_grid"))
        else:
            print("This script requires 'nmcli' for managing Wi-Fi.")
            print("To install it, run:")
            print("  sudo apt install network-manager  # For Debian/Ubuntu")
            print("  sudo yum install NetworkManager  # For RHEL/Fedora")
            print("  sudo pacman -S networkmanager    # For Arch Linux")




    

