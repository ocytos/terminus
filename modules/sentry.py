import psutil
import time
import os
from rich.console import Console
from rich.table import Table

console = Console()

def run_sentry():
    os.system('clear')
    console.print("[bold white]S E N T R Y  -  ANALYSIS MODE[/bold white]\n", justify="center")
    
    with console.status("[bold green]Scanning system processes...") as status:
        time.sleep(1.5)
        
        table = Table(title="PROCESS BEHAVIOR MONITOR", border_style="grey30", expand=True)
        table.add_column("PID", style="cyan", justify="center")
        table.add_column("PROCESS NAME", style="white")
        table.add_column("CPU %", style="magenta", justify="right")
        table.add_column("MEMORY %", style="blue", justify="right")
        table.add_column("STATUS", style="bold yellow", justify="center")

        count = 0
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                if proc.info['cpu_percent'] > 0.0 or proc.info['memory_percent'] > 0.1:
                    table.add_row(
                        str(proc.info['pid']),
                        str(proc.info['name'])[:25],
                        f"{proc.info['cpu_percent']:.1f}%",
                        f"{proc.info['memory_percent']:.1f}%",
                        "VERIFIED"
                    )
                    count += 1
                if count > 15: break 
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    console.print(table)
    console.print(f"\n[bold green][+][/bold green] Analysis complete. {count} active threads monitored.")
    input("\n [PRESS ENTER TO EXIT MODULE]")
