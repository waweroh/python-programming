import os
import sys

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)

    print("Everything is ok.")
    sys.exit(0)

main()