import os
import sys

def main():
    if check_reboot():
        pass
        print("Pending Reboot.")
        sys.exit(1)

    print("Everything is ok.")
    sys.exit(1)

main()