import os
import sys
from pyfiglet import Figlet
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.align import Align

console = Console()

def clear():
    sys.stdout.write('\033[H\033[2J')
    sys.stdout.flush()

def display_menu(lang='EN'):
    clear()
    f = Figlet(font='slant')
    title_text = f.renderText('TERMINUS')
    console.print(Align.center(title_text), style="bold white")
    info_cols = Columns([
        "[bold white]SESSION:[/bold white] ACTIVE",
        "[bold white]OPERATOR:[/bold white] OCY",
        "[bold white]ENDPOINT:[/bold white] github.com/ocytos",
        f"[bold cyan]LANG:[/bold cyan] {lang}"
    ], equal=True, expand=True)
    console.print(Panel(info_cols, border_style="grey30"))
    table = Table(show_header=True, header_style="bold white", border_style="grey30", box=None, expand=True, row_styles=["", "dim"])
    if lang == 'EN':
        cols, prompt = ["ID", "MODULE", "FUNCTION", "STATUS"], "Select module ID to initialize"
        rows = [
            ("01", "SENTRY", "Behavioral Spyware Analyst & Persistence Scan", "[bold green]ONLINE[/bold green]"),
            ("02", "GHOST", "Network Anonymizer & MAC/DNS Shifter", "[bold green]ONLINE[/bold green]"),
            ("03", "VAULT", "Encrypted File Shredder & Shadow Stash", "[bold green]ONLINE[/bold green]"),
            ("04", "BRIDGE", "Android Payload Injector & ADB Commander", "[bold green]ONLINE[/bold green]"),
            ("05", "BOOST", "Kernel Resource Optimizer & RAM Purge", "[bold green]ONLINE[/bold green]"),
            ("06", "PULSE", "Deep Packet Inspection & Traffic Intercept", "[bold yellow]STANDBY[/bold yellow]"),
            ("07", "VOID", "Secure Metadata Stripper & Exif Wiper", "[bold yellow]STANDBY[/bold yellow]"),
            ("08", "CORTEX", "Automated OSINT & Identity Correlation", "[bold yellow]STANDBY[/bold yellow]"),
            ("09", "PHANTOM", "Remote Process Hollowing & Injection Test", "[bold red]LOCKED[/bold red]"),
            ("10", "AURA", "Wireless Spectrum Audit & Signal Jammer", "[bold red]LOCKED[/bold red]"),
            ("11", "KRONOS", "Temporal File Forensic & Recovery Engine", "[bold yellow]STANDBY[/bold yellow]"),
            ("LN", "LANG", "Switch Interface Language (ES/EN)", "[bold blue]SYSTEM[/bold blue]")
        ]
    else:
        cols, prompt = ["ID", "MÓDULO", "FUNCIÓN", "ESTADO"], "Seleccione ID de módulo para iniciar"
        rows = [
            ("01", "SENTRY", "Analista de Spyware Comportamental y Persistencia", "[bold green]EN LÍNEA[/bold green]"),
            ("02", "GHOST", "Anonimizador de Red y Cambio de MAC/DNS", "[bold green]EN LÍNEA[/bold green]"),
            ("03", "VAULT", "Destructor de Archivos y Almacén Cifrado", "[bold green]EN LÍNEA[/bold green]"),
            ("04", "BRIDGE", "Inyector de Payload Android y Mando ADB", "[bold green]EN LÍNEA[/bold green]"),
            ("05", "BOOST", "Optimizador de Kernel y Purga de RAM", "[bold green]EN LÍNEA[/bold green]"),
            ("06", "PULSE", "Inspección de Paquetes e Intercepción de Tráfico", "[bold yellow]ESPERA[/bold yellow]"),
            ("07", "VOID", "Eliminador de Metadatos y Limpieza Exif", "[bold yellow]ESPERA[/bold yellow]"),
            ("08", "CORTEX", "OSINT Automatizado y Correlación de Identidad", "[bold yellow]ESPERA[/bold yellow]"),
            ("09", "PHANTOM", "Hollowing de Procesos y Test de Inyección", "[bold red]BLOQUEADO[/bold red]"),
            ("10", "AURA", "Auditoría de Espectro Inalámbrico y Jammer", "[bold red]BLOQUEADO[/bold red]"),
            ("11", "KRONOS", "Forense de Archivos Temporales y Recuperación", "[bold yellow]ESPERA[/bold yellow]"),
            ("LN", "LANG", "Cambiar Idioma de Interfaz (ES/EN)", "[bold blue]SISTEMA[/bold blue]")
        ]
    for col in cols: table.add_column(col, justify="left" if col not in ["ID", "STATUS"] else "center")
    for row in rows: table.add_row(*row)
    console.print(table)
    console.print(Panel(f"[bold cyan]TERMINUS@OCY[/bold cyan]:[bold white]~#[/bold white] {prompt}", border_style="grey30"))
