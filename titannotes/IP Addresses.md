commands

ifconfig![[Pasted image 20260311171500.png|328]]

inet - IPV4 address
inet6 - IPv6 address
NAT - Network address translation

The **OSI model (Open Systems Interconnection model)** is a way to **explain how data travels from one computer to another over a network**.
1️⃣ Physical Layer
This layer is the **actual hardware** that carries the signal.

Examples:

- Ethernet cables
    
- Wi-Fi signals
    
- Fiber optics
2️⃣ Data Link Layer
This layer helps devices **communicate within the same network** and identifies devices using **MAC addresses**.

Examples:

- Switches
    
- MAC (Media Access Control) addresses
3️⃣ Network Layer
This layer determines **where the data should go across different networks** using **IP addresses**.

Examples:

- Routers
    
- IP addressing
4️⃣ Transport Layer
This layer ensures the **data arrives correctly and completely**.

Two common protocols:

- **Transmission Control Protocol (TCP)** – reliable delivery - connection oriented, websites, ssh
- works on a three way handshake
    
- **User Datagram Protocol (UDP)** – faster but less reliable - streaming services, voice over IP
5️⃣ Session Layer
This layer **starts, maintains, and ends communication sessions** between devices.

6️⃣ Presentation Layer
This layer **translates and encrypts data** so both systems understand it.

Examples:

- Encryption
    
- Data formatting
7️⃣ Application Layer
This is the layer where **users interact with the network**.

Examples:

- Web browsers
    
- Email
    
- File transfers
    

Protocols like:

- **Hypertext Transfer Protocol (HTTP)**
    
- **File Transfer Protocol (FTP)


TCP
FTP - File Transfer Protocol(21) - put a file and get a file off the server
SSH - The encrypted version of Telnet (22)
Telnet - Ability to log into a machine remotely(23)
SMTP -  Mail servers (25)
DNS - Resolving IP addresses to names (53)
HTTP(80) / HTTPS (443) - Websites
POP3 (110) - 
SMB (139 + 445) - File shares/ Samba
IMAP (143)

UDP
DNS - Resolving IP addresses to names (53)
DHCP - (67, 68)
TFTP - (69)
SNMP - (161) - Simple Network Management Protocol