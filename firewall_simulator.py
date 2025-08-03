import random  # Importing random module to generate random IPs, Ports, and Protocols

# Function to generate a random IP address within the 192.168.1.0/24 subnet
def generateRandomIP():
    return f"192.168.1.{random.randint(0,50)}"

# Function to randomly select a port from commonly used ports
def generateRandomPort():
    return random.choice([22, 80, 443, 8080, 3306])

# Function to randomly select a protocol (TCP or UDP)
def generateRandomProtocol():
    return random.choice(["TCP", "UDP"])

# Function to check if a given traffic packet (IP, Port, Protocol) matches any firewall rule
def checkFirewallRules(ip, port, protocol, rules, default_policy="allow"):
    for rule in rules:
        # Check if IP, Port, and Protocol match the rule or use 'any' wildcard
        ip_match = (rule["ip"] == ip or rule["ip"] == "any")
        port_match = (rule["port"] == port or rule["port"] == "any")
        protocol_match = (rule["protocol"] == protocol or rule["protocol"] == "any")

        # If all conditions match, return the rule's action (block/allow)
        if ip_match and port_match and protocol_match:
            return rule["action"]
    # If no rule matches, apply the default policy (allow)
    return default_policy

# Function to add a new firewall rule via user input
def addRule(rules):
    ip = input("Enter IP (or 'any'): ")
    port_input = input("Enter Port (or 'any'): ")
    port = int(port_input) if port_input != "any" else "any"
    protocol = input("Enter Protocol (TCP/UDP/any): ").upper()
    action = input("Enter Action (block/allow): ").lower()

    new_rule = {"ip": ip, "port": port, "protocol": protocol, "action": action}
    rules.append(new_rule)  # Add the new rule to the rules list
    print(f"Rule added: {new_rule}")

# Function to remove a firewall rule by selecting its index
def removeRule(rules):
    if not rules:
        print("No rules to remove.")
        return

    # Display current rules with their index
    print("\nCurrent Rules:")
    for idx, rule in enumerate(rules):
        print(f"{idx}: {rule}")

    try:
        index = int(input("Enter the index of the rule to remove: "))
        if 0 <= index < len(rules):
            removed = rules.pop(index)  # Remove the rule by index
            print(f"Removed rule: {removed}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

# Function to display all current firewall rules
def viewRules(rules):
    if not rules:
        print("No firewall rules defined.")
    else:
        print("\nCurrent Firewall Rules:")
        for idx, rule in enumerate(rules):
            print(f"{idx}: {rule}")

# Function to simulate network traffic and apply firewall rules
def runSimulation(rules):
    log = []  # List to store log entries
    blocked_count = 0
    allowed_count = 0

    print("\n--- Running Traffic Simulation ---\n")
    for _ in range(20):  # Simulate 20 random traffic attempts
        ip = generateRandomIP()
        port = generateRandomPort()
        protocol = generateRandomProtocol()

        # Check if the traffic should be allowed or blocked
        action = checkFirewallRules(ip, port, protocol, rules, default_policy="allow")

        log_entry = f"IP: {ip}, Port: {port}, Protocol: {protocol}, Action: {action}"
        log.append(log_entry)  # Add log entry to the log list

        # Update statistics counters
        if action == "block":
            blocked_count += 1
        else:
            allowed_count += 1

        print(log_entry)  # Display each traffic attempt result

    # Display simulation summary stats
    print("\n=== Firewall Stats ===")
    print(f"Total Attempts: {len(log)}")
    print(f"Blocked: {blocked_count}")
    print(f"Allowed: {allowed_count}")
    print("\n--- End of Simulation ---\n")

# Main function to run the Firewall Simulator CLI
def main():
    # Predefined firewall rules at startup
    firewallRules = [
        {"ip": "192.168.1.1", "port": 80, "protocol": "TCP", "action": "block"},
        {"ip": "192.168.1.27", "port": "any", "protocol": "any", "action": "block"},
        {"ip": "192.168.1.14", "port": 22, "protocol": "TCP", "action": "block"},
        {"ip": "192.168.1.37", "port": 443, "protocol": "TCP", "action": "block"},
    ]

    # CLI Menu Loop
    while True:
        print("\n=== Firewall Simulator Menu ===")
        print("1. View Current Rules")
        print("2. Add New Rule")
        print("3. Remove Existing Rule")
        print("4. Run Traffic Simulation")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        # Handle user menu choice
        if choice == '1':
            viewRules(firewallRules)
        elif choice == '2':
            addRule(firewallRules)
        elif choice == '3':
            removeRule(firewallRules)
        elif choice == '4':
            runSimulation(firewallRules)
        elif choice == '5':
            print("Exiting Firewall Simulator. Goodbye!")
            break
        else:
            print("Invalid option. Please select a number between 1-5.")

# Entry point of the program
if __name__ == "__main__":
    main()
