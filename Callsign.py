#https://www.reddit.com/user/zaplembahuw

import pyperclip

def run():
    callsign = input("Callsign: ")
    location = input("Location: ")
    date = input("Date(YYYYMMDD): ")


    done = callsign.upper().strip() + "@K-" + location.strip() + "-" + date.strip() + ".adi"

    print(done)
    pyperclip.copy(done)
    print("Copied to clipboard.")

do = "y"

while do == "y":
    run()
    do = input("Run again? (y/n): ")