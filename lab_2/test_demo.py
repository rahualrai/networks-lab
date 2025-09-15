#!/usr/bin/env python3

import subprocess
import time
import threading

def run_server():
    """Run the server in a separate process"""
    return subprocess.Popen(['python3', 'basic_server.py'], 
                          stdout=subprocess.PIPE, 
                          stderr=subprocess.PIPE, 
                          text=True)

def run_client_with_messages(messages):
    """Run the client with multiple predefined messages"""
    message_input = '\n'.join(messages)
    return subprocess.run(['python3', 'basic_client.py'], 
                         input=message_input, 
                         text=True, 
                         capture_output=True)

def main():
    print("=== Lab 2 TCP Socket Demo - Persistent Connection ===\n")
    
    # Start server
    print("Starting server...")
    server_process = run_server()
    time.sleep(1)  # Give server time to start
    
    # Run client with multiple messages
    print("Running client with multiple test messages...")
    test_messages = [
        "Hello from automated test!",
        "This is message 2",
        "Testing persistent connection",
        "disconnect"
    ]
    client_result = run_client_with_messages(test_messages)
    
    # Wait for server to finish
    server_output, server_error = server_process.communicate(timeout=10)
    
    # Display results
    print("\n--- SERVER OUTPUT ---")
    print(server_output)
    
    print("--- CLIENT OUTPUT ---")
    print(client_result.stdout)
    
    if client_result.stderr:
        print("--- CLIENT ERRORS ---")
        print(client_result.stderr)
    
    print("=== Demo Complete ===")

if __name__ == "__main__":
    main()