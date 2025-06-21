import random

# function to generate random numbers to create IPs
def generateRandomIP():
    return f"192.168.1.{random.randint(0,50)}"

# function for "firewall", what to allow and what not to allow
def checkFirewallRules(ip, rules):
    for ruleIp, action in rules.items():
        if ip == ruleIp:
            return action
        return "allow"
    
# main
def main():
    # rules for firewall
    firewallRules = {
        "192.168.1.1": "block",
        "192.168.1.27": "block",
        "192.168.1.3": "block",
        "192.168.1.14": "block",
        "192.168.1.5": "block",
        "192.168.1.16": "block",
        "192.168.1.37": "block",
}
    # generating inputs and printing output
    for _ in range(12):
        ipAddress = generateRandomIP()
        action = checkFirewallRules(ipAddress, firewallRules)
        random_number = random.randint(0,10000)
        print(f"IP: {ipAddress}, Action: {action}, Random: {random_number}", end="\n")

# execution
if __name__ == "__main__":
    main()

