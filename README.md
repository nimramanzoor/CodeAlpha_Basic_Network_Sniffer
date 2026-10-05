# Basic Network Sniffer

This is a Python-based network packet sniffer built as part of the CodeAlpha Cybersecurity Internship (Task 1). It captures network traffic and extracts vital information such as source and destination IP addresses, protocols, and raw payload data.

## Features
- Captures live network packets using the `scapy` library.
- Identifies and inspects IPv4 traffic.
- Extracts and displays:
  - Source and Destination IP addresses
  - Protocol type (TCP, UDP, ICMP)
  - Raw packet payloads (first 50 bytes for readability)

## Prerequisites
- **Python 3.x**
- **Scapy**: Install via `pip install scapy`
- **Windows Users**: Must install [Npcap](https://npcap.com/) to enable packet capturing.
- **Linux Users**: `libpcap` is required (pre-installed on distributions like Kali Linux).

## Usage
Because packet sniffing requires low-level network access, you must run this script with elevated privileges.

**On Windows (Run Command Prompt / Terminal as Administrator):**
```bash
python network_sniffer.py