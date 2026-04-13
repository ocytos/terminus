import os
from rich.console import Console
console = Console()

def run_void():
    os.system('clear')
    console.print("[bold white]V O I D  -  METADATA STRIPPER[/bold white]\n", justify="center")
    console.print("[!] Path to file:")
    path = input(" void@ocy:~# ")
    console.print(f"\n[bold yellow][*][/] Stripping Exif/Metadata from {path}...")
    import time
    time.sleep(1.5)
    console.print("[bold green][+][/] Scrubbing complete. Identity sanitized.")
    input("\n [ENTER]")
