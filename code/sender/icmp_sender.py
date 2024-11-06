import scapy

from scapy.all import ICMP, IP, send

packet = IP(dst="receiver", ttl=1) / ICMP()
send(packet)