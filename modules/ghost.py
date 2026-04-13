import os
import time
from rich.console import Console
from rich.table import Table

console = Console()

def run_ghost():
    os.system('clear')
    console.print("[bold white]G H O S T  -  NETWORK ANONYMIZER[/bold white]\n", justify="center")
    
    with console.status("[bold cyan]Scanning network interfaces...") as status:
        time.sleep(1.5)
        # En Arch Linux usamos ip link
        interfaces = os.popen("ip -br link show").read().splitlines()
        
        table = Table(title="NETWORK INTERFACES", border_style="cyan")
        table.add_column("INTERFACE", style="bold white")
        table.add_column("STATE", style="bold yellow")
        table.add_column("MAC ADDRESS", style="magenta")

        for line in interfaces:
            parts = line.split()
            if len(parts) >= 3:
                table.add_row(parts[0], parts[1], parts[2])

    console.print(table)
    console.print("\n[bold yellow][!][/bold yellow] Ready to shift MAC/DNS. Select sub-option...")
    input("\n [PRESS ENTER TO EXIT]")
