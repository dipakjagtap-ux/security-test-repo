# vulnerable_sample.py - File created for security scan and vulnerability testing

import os
import sqlite3

# Vulnerability 1: SQL Injection (Unsafe query construction)
def get_user_data(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Unsafe query directly concatenating user input
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    
    result = cursor.fetchall()
    conn.close()
    return result

# Vulnerability 2: Command Injection (Unsafe system command execution)
def ping_host(host_address):
    # Directly passing user input into os.system without sanitization
    command = "ping -c 1 " + host_address
    os.system(command)

if __name__ == "__main__":
    print("Vulnerable sample file loaded for testing.")
