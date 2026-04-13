import os
from rich.console import Console
console = Console()

def run_aura():
    os.system('clear')
    console.print("[bold cyan]A U R A  -  SPECTRUM AUDIT[/bold cyan]\n", justify="center")
    console.print("[*] Interface: wlan0mon")
    console.print("[!] Scanning frequencies (2.4Ghz / 5Ghz)...")
    import time
    time.sleep(2)
    input("\n [ENTER TO STOP SCAN]")
