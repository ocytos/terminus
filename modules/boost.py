import os
import time
from rich.console import Console

console = Console()

def run_boost():
    os.system('clear')
    console.print("[bold magenta]B O O S T  -  KERNEL OPTIMIZER[/bold magenta]\n", justify="center")
    
    # Ver estado antes
    console.print("[bold white]Current Memory State:[/bold white]")
    os.system("free -h")
    
    action = input("\n[?] Attempt Deep RAM Flush? (y/n): ")
    if action.lower() == 'y':
        with console.status("[bold white]Writing to /proc/sys/vm/drop_caches...") as status:
            time.sleep(1)
            # Intentar limpiar caché (requiere sudo)
            ret = os.system("sudo sync; echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null")
            
            if ret == 0:
                console.print("\n[bold green][+][/bold green] Cache cleared and RAM optimized.")
            else:
                console.print("\n[bold red][!][/bold red] Error: Boost requires SUDO to flush Kernel cache.")
    
    input("\n [PRESS ENTER TO EXIT]")
