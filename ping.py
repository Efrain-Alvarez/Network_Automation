import subprocess
import re
import csv

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
    match = re.search(r"min/avg/max/(?:mdev|stddev) = .*?/(.*?)/", output)
    if match:
        return float(match.group(1))  # Return the average time as a float
    return None

# Function to export results to a CSV file
def export_to_csv(results, filename="ping_results.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["IP Address", "Status", "Average Time (ms)"])
        # Write each result
        for ip, status, avg_time in results:
            writer.writerow([ip, status, avg_time])

# List of IP addresses to ping
ip_addresses = ["8.8.8.8", "1.1.1.1", "192.168.1.1"]

# Ping all IPs and get the results
ping_results = ping_ips(ip_addresses)

# Export results to a CSV file
export_to_csv(ping_results)

print("Ping results have been exported to 'ping_results.csv'.")
