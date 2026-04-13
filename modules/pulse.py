import os
import time
from rich.console import Console
from rich.progress import Progress

console = Console()

def run_pulse():
    os.system('clear')
    console.print("[bold yellow]P U L S E  -  DEEP PACKET INSPECTION[/bold yellow]\n", justify="center")
    
    with Progress() as progress:
        task = progress.add_task("[cyan]Intercepting packets...", total=100)
        while not progress.finished:
            progress.update(task, advance=20)
            time.sleep(0.4)
            
    console.print("\n[bold white]TRAFFIC LOG (RECENT):[/bold white]")
    console.print("[grey50]192.168.1.15 -> 8.8.8.8  | TCP:443[/grey50]")
    console.print("[grey50]192.168.1.15 -> 1.1.1.1  | UDP:53[/grey50]")
    
    input("\n [PRESS ENTER TO EXIT]")
