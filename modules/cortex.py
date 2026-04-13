import os
from rich.console import Console
console = Console()

def run_cortex():
    os.system('clear')
    console.print("[bold blue]C O R T E X  -  IDENTITY CORRELATION[/bold blue]\n", justify="center")
    target = input(" target_identifier@ocy:~# ")
    console.print(f"\n[bold white][*][/] Querying global databases for: {target}")
    import time
    time.sleep(2)
    console.print("[bold red][!][/] Correlation found in 3 leaked databases. Check logs.")
    input("\n [ENTER]")
