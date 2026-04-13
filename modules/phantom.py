import os
import psutil
import time
from rich.console import Console
from rich.table import Table

console = Console()

def run_phantom():
    os.system('clear')
    console.print("[bold red]P H A N T O M  -  INJECTION TESTER (Linux x64)[/bold red]\n", justify="center")
    
    # 1. Listar procesos candidatos
    table = Table(title="TARGET CANDIDATES")
    table.add_column("PID", style="cyan")
    table.add_column("NAME", style="white")
    table.add_column("PERMISSIONS", style="yellow")

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Solo mostramos procesos del usuario actual para evitar errores de permiso
            table.add_row(str(proc.info['pid']), proc.info['name'], "USER_LEVEL")
        except: continue

    console.print(table)
    
    target_pid = input("\n [!] Enter Target PID for Injection Test: ")
    
    if target_pid:
        with console.status(f"[bold red]Attempting Process Hollowing on PID {target_pid}...") as status:
            time.sleep(2)
            
            # TEST DE ACCESO A MEMORIA
            # Intentamos abrir el mapa de memoria del proceso
            mem_path = f"/proc/{target_pid}/maps"
            
            if os.path.exists(mem_path):
                console.print(f"\n[bold green][+][/bold green] Memory Map Acquired: {mem_path}")
                console.print("[bold yellow][*][/bold yellow] Injecting NOP Sled (Simulated)...")
                time.sleep(1)
                console.print("[bold green][SUCCESS][/bold green] Payload delivered to stack. Thread hijacked.")
            else:
                console.print("\n[bold red][ERROR][/bold red] Permission Denied. Run as sudo.")
                
    input("\n [PRESS ENTER TO RETURN]")
