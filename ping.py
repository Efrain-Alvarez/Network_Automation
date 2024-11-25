import subprocess
import re

# Function to ping a list of IP addresses
def ping_ips(ip_list):
    results = []  # To store the results for all IPs
    for ip in ip_list:
        try:
            # Execute the ping command
            result = subprocess.run(
                ["ping", "-c", "4", ip],  # For Windows, use "-n" instead of "-c"
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                avg_time = extract_average_time(result.stdout)
                results.append((ip, "Success", avg_time))
            else:
                results.append((ip, "Failed", None))
        except subprocess.TimeoutExpired:
            results.append((ip, "Timeout", None))
    return results

# Function to extract the average round-trip time from ping output
def extract_average_time(output):
    # Match the part with avg round-trip times (e.g., "min/avg/max/mdev = 10.4/15.2/20.1/1.2 ms")
    match = re.search(r"min/avg/max/(?:mdev|stddev) = .*?/(.*?)/", output)
    if match:
        return float(match.group(1))  # Return the average time as a float
    return None

# Function to process the results for the list of IPs
def process_ping_results(results):
    for ip, status, avg_time in results:
        if status == "Success":
            print(f"{ip}: {status}, Average time: {avg_time} ms")
        else:
            print(f"{ip}: {status}")

# List of IP addresses to ping
ip_addresses = ["8.8.8.8", "1.1.1.1", "192.168.1.1"]

# Ping all IPs and process the results
ping_results = ping_ips(ip_addresses)
process_ping_results(ping_results)
