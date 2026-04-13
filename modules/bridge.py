import os
import time
from rich.console import Console

console = Console()

def run_bridge():
    os.system('clear')
    console.print("[bold green]B R I D G E  -  ANDROID PAYLOAD COMMANDER[/bold green]\n", justify="center")
    
    console.print("[bold white]Detecting connected devices (ADB)...[/bold white]")
    # Ejecuta adb devices de forma silenciosa
    devices = os.popen("adb devices").read().strip().split('\n')[1:]
    
    if not devices or devices[0] == "":
        console.print("[bold red][!] NO DEVICES FOUND.[/bold red] Connect via USB/TCP.")
    else:
        for dev in devices:
            console.print(f"[bold green][+][/bold green] DEVICE FOUND: {dev}")

    console.print("\n[1] Generate Payload (msfvenom)")
    console.print("[2] Start ADB Shell")
    console.print("[3] Push/Install APK")
    console.print("[0] Return")
    
    input("\n bridge@ocy:~# ")
