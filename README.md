## Description
TERMINUS is a modular terminal-based security and system optimization suite developed for Linux environments. It provides a centralized interface for process monitoring, network analysis, android bridge debugging, and kernel-level memory management.

## Installation
The following dependencies are required for full functionality on Arch Linux:
- python-rich
- python-psutil
- android-tools
- macchanger

Install dependencies using pacman:
sudo pacman -S python-rich python-psutil android-tools macchanger

## Setup and Launch
Navigate to the project directory and run the main engine:
cd ~/TERMINUS
python main.py

## Global Alias Setup
To launch TERMINUS from any terminal session, add the following alias to your shell configuration:
echo 'alias terminus="python ~/TERMINUS/main.py"' >> ~/.bashrc
source ~/.bashrc

## Modules Overview

01 SENTRY: Real-time process behavior monitor and thread analysis.
   Usage: View active PIDs, CPU/Memory consumption, and process status.

02 GHOST: Network interface manager and anonymization tool.
   Usage: Scan local interfaces and prepare for MAC/DNS shifting.

03 VAULT: Secure file shredder using Gutmann/DoD standards.
   Usage: Overwrite sensitive files to prevent forensic recovery.

04 BRIDGE: Android Debug Bridge (ADB) commander.
   Usage: Identify connected devices and deploy testing payloads.

05 BOOST: Kernel resource optimizer and memory cache flusher.
   Usage: Requires sudo to clear /proc/sys/vm/drop_caches.

06 PULSE: Network traffic monitoring and packet inspection.
   Usage: Intercept and log local network traffic for analysis.

07 VOID: Metadata stripper for privacy-preserving file sharing.
   Usage: Scrub EXIF and identifying data from documents and images.

08 CORTEX: OSINT identity correlation engine.
   Usage: Search for target identifiers across known database leaks.

09 PHANTOM: Process hollowing and memory injection tester.
   Usage: Target a specific PID to test memory map acquisition and injection.

10 AURA: Wireless spectrum audit and signal analysis.
   Usage: Requires monitor mode support to audit wireless frequencies.

11 KRONOS: Temporal forensics and residual string recovery.
   Usage: Scan swap and /tmp directories for sensitive string remnants.

## Disclaimer
This software is provided strictly for educational and authorized security auditing purposes. The developer assumes no liability for misuse, unauthorized access to systems, or damages caused by this suite. Users are responsible for complying with local laws and regulations regarding cybersecurity testing.

Developed by OCY.
EOF
