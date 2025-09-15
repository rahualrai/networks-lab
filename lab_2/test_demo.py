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

def run_client_with_message(message):
    """Run the client with a predefined message"""
    return subprocess.run(['python3', 'basic_client.py'], 
                         input=message, 
                         text=True, 
                         capture_output=True)

def main():
    print("=== Lab 2 TCP Socket Demo ===\n")
    
    # Start server
    print("Starting server...")
    server_process = run_server()
    time.sleep(1)  # Give server time to start
    
    # Run client
    print("Running client with test message...")
    client_result = run_client_with_message("Hello from automated test!")
    
    # Wait for server to finish
    server_output, server_error = server_process.communicate(timeout=5)
    
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