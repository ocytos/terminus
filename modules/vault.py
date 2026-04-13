import os
import time
from rich.console import Console
from rich.panel import Panel

console = Console()

def run_vault():
    os.system('clear')
    console.print("[bold white]V A U L T  -  SECURE STORAGE & SHREDDER[/bold white]\n", justify="center")
    
    console.print("[1] Shred File (Gutmann Method)")
    console.print("[2] Encrypt Directory (AES-256)")
    console.print("[3] Wipe Free Space")
    console.print("[0] Return")
    
    choice = input("\n vault@ocy:~# ")
    
    if choice != "0":
        with console.status("[bold red]Executing security protocol...") as status:
            time.sleep(1.5)
            console.print("\n[bold yellow][!][/] Action logged. Feature in sandbox mode.")
            input("\n [PRESS ENTER]")
