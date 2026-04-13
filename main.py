import sys
import os
import time
from core.engine import animar
from core.menu import display_menu
from rich.console import Console

console = Console()

def main():
    current_lang = 'EN'
    animar()
    
    while True:
        display_menu(current_lang)
        prompt = "\n[bold cyan]TERMINUS@OCY[/][bold white]:[/][bold blue]~#[/] "
        
        try:
            choice = console.input(prompt).strip()
        except EOFError:
            break

        choice_upper = choice.upper()
        
        try:
            val = int(choice)
        except ValueError:
            val = None

        if choice_upper == 'LN':
            current_lang = 'ES' if current_lang == 'EN' else 'EN'
        elif val == 1:
            from modules.sentry import run_sentry
            run_sentry()
        elif val == 2:
            from modules.ghost import run_ghost
            run_ghost()
        elif val == 3:
            from modules.vault import run_vault
            run_vault()
        elif val == 4:
            from modules.bridge import run_bridge
            run_bridge()
        elif val == 5:
            from modules.boost import run_boost
            run_boost()
        elif val == 6:
            from modules.pulse import run_pulse
            run_pulse()
        elif val == 7:
            from modules.void import run_void
            run_void()
        elif val == 8:
            from modules.cortex import run_cortex
            run_cortex()
        elif val == 9:
            from modules.phantom import run_phantom
            run_phantom()
        elif val == 10:
            from modules.aura import run_aura
            run_aura()
        elif val == 11:
            from modules.kronos import run_kronos
            run_kronos()
        elif choice_upper in ['EXIT', 'QUIT', '00'] or val == 0:
            os.system('clear')
            sys.exit(0)
        else:
            console.print(f"\n[bold red][!] INVALID OPTION: '{choice}'[/]")
            time.sleep(1.5)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        console.print(f"\n[bold red][FATAL ERROR]: {e}[/]")
        input("\nPress Enter to close...")
