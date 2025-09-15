# Lab 2 Testing Instructions

## How to Test the Client-Server Communication

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
   Enter a message when prompted

### Method 2: Automated Demo
```bash
python3 test_demo.py
```

## Expected Output

**Server Output:**
```
Server listening on 127.0.0.1:65432
Connected by ('127.0.0.1', [random_port])
Received: [your_message]
Sent: Echo from server: '[your_message]'
Connection closed
```

**Client Output:**
```
Connecting to 127.0.0.1:65432
Connected to server
Enter message to send: [your_message]
Sent: [your_message]
Received: Echo from server: '[your_message]'
Disconnected from server
```

## Files Included
- `basic_server.py` - TCP server implementation
- `basic_client.py` - TCP client implementation
- `test_demo.py` - Automated testing script