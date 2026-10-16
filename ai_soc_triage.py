
alert = {
    "event": "Failed Login",
    "source_ip": "192.168.1.50",
    "failed_attempts": 12
}

if alert["failed_attempts"] >= 10:
    severity = "High"
else:
    severity = "Low"

print("Event:", alert["event"])
print("Source IP:", alert["source_ip"])
print("Failed Attempts:", alert["failed_attempts"])
print("Severity:", severity)
