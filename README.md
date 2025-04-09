# 🖧 MacAddress_changer_linux

This is a simple Python script for Linux systems that allows users to change the MAC (Media Access Control) address of a network interface using the `ifconfig` command.

> ⚠️ **Note:** This script is intended for educational purposes only. Changing MAC addresses can affect your network connectivity. Use responsibly and always with permission.

---

## 📌 Features

- Takes user input to select a network interface and a new MAC address.
- Uses `subprocess` to run system-level `ifconfig` commands.
- Compares before and after states to confirm the MAC address was changed.

---

## 🛠️ Requirements

- Linux-based system (Ubuntu, Kali, etc.)
- Python 3.x
- Root privileges to run the script
- `ifconfig` must be installed (`net-tools` package)

Install `ifconfig` if missing:

```bash
sudo apt install net-tools
