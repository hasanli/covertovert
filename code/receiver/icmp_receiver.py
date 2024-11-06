import scapy

from scapy.all import sniff, ICMP

def handle_packet(packet):
    if packet.haslayer(ICMP) and packet[ICMP].type == 8:
        packet.show()

#sniff(filter="icmp", prn=handle_packet, store=0)