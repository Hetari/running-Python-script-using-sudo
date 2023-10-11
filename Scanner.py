import nmap


def welcome_message():
    print("Welcome, this is a simple nmap automation tool")
    print("<----------------------------------------------------->")


def get_ip_address():
    ip_addr = input("Please enter the IP address you want to scan: ")
    print("The IP you entered is: ", ip_addr)
    return ip_addr


def get_scan_type():
    resp = input("""\nPlease enter the type of scan you want to run
                    1)SYN ACK Scan
                    2)UDP Scan
                    3)Comprehensive Scan \n""")
    print("You have selected option: ", resp)
    return resp


def perform_scan(ip_addr, resp):
    resp_dict = {'1': ['-v -sS', 'tcp'], '2': ['-v -sU', 'udp'],
                 '3': ['-v -sS -sV -sC -A -O', 'tcp']}

    try:
        scanner = nmap.PortScanner()
        if resp not in resp_dict.keys():
            print("Enter a valid option")
        else:
            print("nmap version:", scanner.nmap_version())

            scanner.scan(ip_addr, "1-1024", resp_dict[resp][0])
            print(scanner.scaninfo())

            if scanner[ip_addr].state() == 'up':
                print("Scanner Status: ", scanner[ip_addr].state())
                print(scanner[ip_addr].all_protocols())
                print("Open Ports: ", scanner[ip_addr]
                      [resp_dict[resp][1]].keys())

    except Exception as e:
        print("An error occurred:", str(e))


def main():
    welcome_message()
    ip_addr = get_ip_address()
    resp = get_scan_type()
    perform_scan(ip_addr, resp)


if __name__ == "__main__":
    main()
