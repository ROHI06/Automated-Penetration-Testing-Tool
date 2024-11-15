import nmap

def scan_network(target_ip):
    nm = nmap.PortScanner()
    nm.scan(target_ip, arguments='-sV')
    return nm[target_ip]