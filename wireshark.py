# Import pyshark
import pyshark
import numpy as np
import matplotlib.pyplot as plt

# Open pcapng file at new_startup.pcapng

cap = pyshark.FileCapture('new_startup.pcapng')

tcp_conversations = {}

src_ports = [52312, 52313, 52314, 52321, 52322, 52323] # manually extracted from wireshark

#for each src port, init the dictionary with an empty list

for src_port in src_ports:
    tcp_conversations[src_port] = []

# Cloudflare -> Me (B->A)
for pkt in cap:
    #if it's IPv4, ignore
    if 'IPv6' not in pkt or pkt.ipv6.src != '2606:4700:3035::6815:161a': #Cloudflare
        continue
    if 'TCP' in pkt:
        conversation_key = pkt.tcp.srcport, pkt.tcp.dstport
        tcp_conversations[int(pkt.tcp.dstport)].append(pkt)

# Me -> Cloudflare (A->B)
for pkt in cap:
    #if it's IPv4, ignore
    if 'IPv6' not in pkt or pkt.ipv6.src != '2001:6a8:3081:6f23:38d1:eaf0:fc:f351': #Me
        continue
    if 'TCP' in pkt:
        conversation_key = pkt.tcp.srcport, pkt.tcp.dstport
        print(conversation_key)
        if int(pkt.tcp.srcport) in tcp_conversations:
            tcp_conversations[int(pkt.tcp.srcport)].append(pkt)

for src_port in src_ports:
    print(f"Number of packets in conversation with src port {src_port}: {len(tcp_conversations[src_port])}")

#Create a pie chart where the labels are the src ports and the values are the number of packets in the conversation
labels = []
sizes = []

for src_port in src_ports:
    labels.append(src_port)
    sizes.append(len(tcp_conversations[src_port]))

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.savefig('ports_tcp.png')

