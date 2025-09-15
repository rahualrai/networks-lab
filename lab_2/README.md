# Lab 2 Testing Instructions

## How to Test the Persistent Client-Server Communication

### Method 1: Manual Testing (Recommended)
1. Open two terminal windows
2. In Terminal 1, run the server:
   ```bash
   python3 basic_server.py
   ```
   You should see: `Server listening on 127.0.0.1:65432`

3. In Terminal 2, run the client:
   ```bash
   python3 basic_client.py
   ```
   - Send multiple messages when prompted
   - Type `disconnect` to terminate both client and server

### Method 2: Automated Demo
```bash
python3 test_demo.py
```

## Expected Output

**Server Output:**
```
Server listening on 127.0.0.1:65432
Connected by ('127.0.0.1', [random_port])
Received: [message1]
Sent: Echo from server: '[message1]'
Received: [message2]
Sent: Echo from server: '[message2]'
Received: disconnect
Sent: Server: Disconnecting...
Connection closed
```

**Client Output:**
```
Connecting to 127.0.0.1:65432
Connected to server
Type 'disconnect' to exit
Enter message to send: [message1]
Sent: [message1]
Received: Echo from server: '[message1]'
Enter message to send: [message2]
Sent: [message2]
Received: Echo from server: '[message2]'
Enter message to send: disconnect
Sent: disconnect
Received: Server: Disconnecting...
Disconnected from server
```

## Files Included
- `basic_server.py` - TCP server implementation
- `basic_client.py` - TCP client implementation
- `test_demo.py` - Automated testing script