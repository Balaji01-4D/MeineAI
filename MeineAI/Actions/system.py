import os
import datetime as dt
import shutil as sl
from pathlib import Path
from time import ctime
import psutil
from rich.console import Console,Group
import platform
from tabulate import tabulate
from datetime import datetime
import pywifi
from rich.progress import Progress, BarColumn
from rich.panel import Panel
from rich.table import Table
console = Console()

import other

class System:

    def Time(self) -> None :
        date = dt.datetime.now().date()
        time = dt.datetime.now().time()
        console.print(Panel(f'[color(197)]DATE : {date}\nTIME : {time}',expand=False),style='color(105)')
        

    
    
    def DiskSpace(self, Destination: Path =Path('/')) -> None: 
        total , used , free = sl.disk_usage(Destination)
        Swap = psutil.swap_memory()
        data ={
            'AVAILABLE' : free / total * 100,
            'USED' : used / total * 100
        }
        Bar =  Progress("[progress.description]{task.description}",
        BarColumn(bar_width=30,complete_style='#2196F3',style='#F2F2F2'),
        "{task.percentage:>3.0f}%",
        console=console,
        ) 
        Available = Bar.add_task(f"[#2196F3]AVAILABLE % ", total=100, completed=data['AVAILABLE'])
        Bar.update(Available,completed=data['AVAILABLE'])
        UsedRam = Bar.add_task(f"[#2196F3]USED      % ", total=100, completed=data['USED'])
        Bar.update(UsedRam,completed=data['USED'])
        storage = Table(show_lines=True,style='#A6A6C3')
        storage.add_column('')
        storage.add_column('[#2196F3]STORAGE')
        storage.add_column('[#2196F3]SWAP MEMORY')
        storage.add_row(f'[#2196F3]TOTAL',other.SizeHelper(total),other.SizeHelper(Swap.total))
        storage.add_row(f'[#2196F3]USED',other.SizeHelper(used),other.SizeHelper(Swap.used))
        storage.add_row(f'[#2196F3]FREE',other.SizeHelper(free),other.SizeHelper(Swap.free))
        panelcollections = Group(Panel('[#2196F3] STORAGE',style='#A6A6C3'),Panel(storage,style='#FFFFFF'),Panel(Bar,style='#A6A6C3'))
        console.print(Panel(panelcollections,style='#1E1E2C',width=60))
    
    def GetCurrentDir(self) -> None:
        path:Path = str(Path('.').resolve())
        console.print(Panel(f'[#F2F2F2]CURRENT DIRECTORY: {path}',expand=False),style='#2196F3')


    def CD(self, Destination: Path) -> None:
        if (Destination.is_dir()):
            try:
                path = str(Destination)
                os.chdir(path)
                self.GetCurrentDir()
            except PermissionError:
                console.print(f"Permission Denied")            
            except Exception as e:
                console.print(f"Can't Change directory to {Destination.name}")
        elif (Destination.is_file()):
            console.print(f"Cant Change {Destination.name} Is File.")
        else:
            console.print(f"{Destination.name} Not Found.")

    def Info(self, Name : Path) -> None:
        if (not Name.exists()):
            console.print(f"{Name.name} Not Found")
            return
        stats = Name.stat()
        Fullpath = Name.resolve()
        size = other.SizeHelper(stats.st_size)
        info = Table(show_header=False,show_lines=True,style='#2196F0')
        info.add_row(f'[#F2F2F2]Name' , Fullpath.name)
        info.add_row(f'[#F2F2F2]Path' , str(Fullpath))
        info.add_row(f'[#F2F2F2]size' , size)
        info.add_row(f'[#F2F2F2]Type' , "File" if (not Name.is_dir()) else "Directory")
        info.add_row(f'[#F2F2F2]Created' , ctime(stats.st_ctime))
        info.add_row(f'[#F2F2F2]Last Modified' , ctime(stats.st_mtime))
        info.add_row(f'[#F2F2F2]Last Accessed' , ctime(stats.st_atime))
        console.print(info)
    
    def IP(self):
        import socket
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        net_info = Table(show_header=False,style='color(105)',show_lines=True)
        net_info.add_row(f"[#F2F2F2]Hostname", hostname)
        net_info.add_row(f"[#F2F2F2]IP Address", ip_address)
        console.print(net_info)

    
    def HomeDir(self):
        console.print(Panel(f'Home Directory :  {Path.home()}',expand=False,style='color(105)'))

    def RAMInfo(self):
        memory = psutil.virtual_memory()
        Total = memory.total
        Avail = memory.available
        Used = memory.used
        data: dict = { 
                'AVAILABLE': Avail/Total * 100,
                'USED' : Used/Total * 100
        }
        Rampanel =  Progress(
        "[progress.description]{task.description}",
        BarColumn(bar_width=30,complete_style='color(105)'),
        "{task.percentage:>3.0f}%",
        console=console,
        ) 
        Available = Rampanel.add_task(f"[color(167)]AVAILABLE % ", total=100, completed=data['AVAILABLE'])
        Rampanel.update(Available,completed=data['AVAILABLE'])
        UsedRam = Rampanel.add_task(f"[color(197)]USED      % ", total=100, completed=data['USED'])
        Rampanel.update(UsedRam,completed=data['USED'])
        panel_group = Group(Panel(f'      [bold cyan]RAM',width=20),Panel(Rampanel,width=70),
        Panel(f"[cyan]Total Memory      : {other.SizeHelper(Total)}\n"+
                            f"[color(167)]Memory Available  : {other.SizeHelper(Avail)}\n"+
                            f"[color(197)]Memory Used       : {other.SizeHelper(Used)}",width=70))
        console.print(Panel(panel_group,expand=False,style='color(105)'))

    def SYSTEM(self):
        systemtable = Table(show_header=False,show_lines=True)
        systemtable.add_row("SYSTEM",platform.system())
        systemtable.add_row("Node Name", platform.node())
        systemtable.add_row("Release", platform.release())
        systemtable.add_row("Version", platform.version())
        systemtable.add_row("Machine", platform.machine())
        systemtable.add_row("Processor", platform.processor())
        console.print(Panel(systemtable,border_style="blue",expand=False,title="SYSTEM INFO"))

    def Battery(self):
        battery = psutil.sensors_battery()
        if battery:
            BtPercent =  round(battery.percent)
            colour = 'green' if (BtPercent > 30) else 'red'
            with Progress(
        "[progress.description]{task.description}",
        BarColumn(bar_width=30,complete_style=colour),
        "{task.percentage:>3.0f}%",
        console=console,
        ) as progress:
                bt = progress.add_task(f"[bold cyan]BATTERY % ", total=100, completed=BtPercent)
                progress.update(bt,completed=BtPercent)

            console.print(f"[bold cyan]Battery Status: {f'[bold blue]Charging' if battery.power_plugged else f"[bold red]Not Charging"}")
        else:
            console.print(f"[bold green]No battery information available.")


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
        Usage = psutil.cpu_percent(interval=1)
        color = 'red' if (Usage > 75) else 'green'
        with Progress(
        "[progress.description]{task.description}",
        BarColumn(bar_width=30,complete_style=color),
        "{task.percentage:>3.0f}%",
        console=console,
        ) as progress:
                Task = progress.add_task(f"[bold magenta]CPU PERCENT % ", total=100, completed=Usage)
                progress.update(Task,completed=Usage)
        console.print(f"[bold magenta]CPU Count[/bold magenta]: {psutil.cpu_count(logical=True)}")
        
        console.print(f"[bold magenta]CPU FREQ RANGE:[/bold magenta] {psutil.cpu_freq().min} < {psutil.cpu_freq().current} < {psutil.cpu_freq().max}")

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

a = System()
a.RAMInfo()