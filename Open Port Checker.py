#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 23:39:41 2025

@author: nb
"""

import socket
target_ip='127.0.0.1'
port_range_start=1
port_range_end=1024
print(f"Scanning target: {target_ip}")

for port in range(port_range_start,port_range_end+1):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result=s.connect_ex((target_ip,port))
    if result ==0:
        print(f"Port {port} is open")
    s.close()
    
print("Scan complete.")