# 🔥 Firewall Traffic Simulator
A Python-based Firewall Traffic Simulator that emulates core firewall functionalities by dynamically filtering simulated network traffic using user-defined access control rules. This project demonstrates fundamental concepts in network security, traffic filtering, and control logic applicable to real-world firewall systems.

# 🧩 Features
- Dynamic Firewall Rules: Add, remove, and view rules in real-time via a command-line interface (CLI).

- Wildcard Rule Matching: Support for flexible rule definitions using any to match all IPs, ports, or protocols.

- Traffic Simulation Engine: Generates randomized IP addresses, ports, and protocols to simulate incoming network traffic.

- Rule-Based Decision Logic: Determines whether to allow or block traffic based on defined rules.

- Traffic Logging & Statistics: Logs every traffic attempt and provides a summary report of blocked and allowed packets.

- Modular & Extensible Design: Easily adaptable for further enhancements like CIDR range matching, persistent logs, or advanced attack simulations.

# 🚀 How It Works
1 Define Firewall Rules: Start with a base set of rules (IP, Port, Protocol, Action).

2 Simulate Network Traffic: The simulator randomly generates traffic with varying IPs, ports, and protocols.

3 Apply Rule Matching Logic: Each packet is evaluated against the firewall rules to determine if it's allowed or blocked.

4 Log & Summarize Results: Actions are logged, and at the end of the simulation, a summary of allowed vs blocked attempts is displayed.

5 Interactive CLI: Manage firewall rules dynamically while the program is running.

# Installation & Usage

### Clone the repository:
```bash
git clone https://github.com/your-username/firewall-simulator.git
cd firewall-simulator
```
### Run the Simulator:
```bash
python firewall_simulator.py
```
### Use the Menu Options:
* View current rules.
* Add new firewall rules (IP, Port, Protocol, Action).
* Remove existing rules.
* Run the traffic simulation.
* Exit the program.

# 📄 Example Rule Definitions
| IP           | Port | Protocol | Action |
| ------------ | ---- | -------- | ------ |
| 192.168.1.1  | 80   | TCP      | block  |
| 192.168.1.27 | any  | any      | block  |
| any          | 22   | any      | block  |
* ```any```: Wildcard match for IP, Port, or Protocol.

# 🛠️ Technologies Used
- Python 3.x
- Command-Line Interface (CLI)
- Core Networking Concepts (IP, Port, Protocol Filtering)

# 📚 Learning Objectives
+ Reinforce understanding of basic firewall operations and access control logic.
+ Hands-on scripting experience simulating real-world firewall scenarios.
+ Develop modular and extensible code design patterns for security-related tools.

# 📈 Possible Enhancements
+ CIDR Subnet Matching (e.g., 192.168.1.0/24
+ Persistent Log Files (write to .log files)
+ Port Scan & Anomaly Detection Simulation
+ Rule Prioritization (First-Match-Wins Logic)



