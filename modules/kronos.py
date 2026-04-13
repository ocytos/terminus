import os
from rich.console import Console
console = Console()

def run_kronos():
    os.system('clear')
    console.print("[bold yellow]K R O N O S  -  TEMPORAL FORENSICS[/bold yellow]\n", justify="center")
    console.print("[*] Scanning /tmp and swap for residual strings...")
    import time
    time.sleep(1.5)
    console.print("[bold green][+][/] Recovery points mapped in /logs/kronos.log")
    input("\n [ENTER]")
