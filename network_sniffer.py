from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        
        # Identify the protocol layer and extract payload
        payload = b""
        if TCP in packet:
            proto_name = "TCP"
            payload = bytes(packet[TCP].payload)
        elif UDP in packet:
            proto_name = "UDP"
            payload = bytes(packet[UDP].payload)
        elif ICMP in packet:
            proto_name = "ICMP"
            payload = bytes(packet[ICMP].payload)
        else:
            proto_name = f"Other ({protocol})"
            payload = bytes(packet[IP].payload)
        
        # Display the extracted information
        print(f"[*] Source: {ip_src} -> Destination: {ip_dst} | Protocol: {proto_name}")
        
        if payload:
        
            print(f"    Payload: {payload[:50]}\n")

print("Starting the network sniffer... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=False)