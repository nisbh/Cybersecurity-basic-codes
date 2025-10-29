#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 00:35:34 2025

@author: nb
"""

import socket
import struct

print("Initialising packet sniffer(Needs sudo")
print("Press Ctrl+C to stop")

try:
    s=socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(3))
    while True:
        raw_packet,address=s.recvfrom(65535)
        ip_header_raw=raw_packet[0:20]
        ip_header_unpacked=struct.unpack('!8xBB2x4s4s', ip_header_raw)
        protocol=ip_header_unpacked[1]
        source_ip = socket.inet_ntoa(ip_header_unpacked[2])
        dest_ip = socket.inet_ntoa(ip_header_unpacked[3])
        print(f"IP Packet: Protocol={protocol}, Source={source_ip}, Destination={dest_ip}")       
except KeyboardInterrupt:
    print("\nSniffer stopped.")
except socket.error as msg:
    print(f"Socket Error: {msg}")
    print("This script must be run with sudo privileges.")
