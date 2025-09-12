import socket
import time

HOST = "ctf.idi.ntnu.no"  # Replace with actual host
PORT = 5009        # Replace with actual port
for length in range(39, 60):
    payload = "A" * length
    print(f"Testing length {length}")

    try:
        s = socket.socket()
        s.connect((HOST, PORT))
        s.sendall(payload.encode() + b"\n")
        
        time.sleep(1)
        response = s.recv(1024).decode(errors="ignore")
        print(response)
        s.close()

        # If service dies or closes abruptly, response may be empty
        if not response:
            print(f"Possible crash at length {length}")
            break
    except Exception as e:
        print(f"Connection error at length {length}: {e}")
        break
