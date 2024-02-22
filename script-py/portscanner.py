import socket
import asyncio
from tqdm import tqdm

async def scan_port(ip, port, timeout):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = await asyncio.get_event_loop().run_in_executor(None, s.connect_ex, (ip, port))
        s.close()
        return result, port
    except socket.error as e:
        return e, port

async def port_scan(ip, port_range=(1, 1023), timeout=0.1):
    try:
        socket.inet_aton(ip)
    except socket.error:
        print("Invalid IP address. Please enter a valid IP.")
        return

    print(f'\nStarting a scan on {ip}')
    open_ports = []

    with tqdm(total=port_range[1] - port_range[0] + 1, desc="Scanning ports", bar_format="{desc}: {percentage:.2f}%") as pbar:
        tasks = [scan_port(ip, port, timeout) for port in range(*port_range)]
        for future in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Scanning Progress"):
            result, port = await future
            if isinstance(result, Exception):
                print(f"Error scanning port {port}: {result}")
            elif result == 0:
                service_name = get_service_name(port)
                open_ports.append((port, service_name))
            pbar.update(1)

    if open_ports:
        print(f'Scan complete. Open ports:')
        for port, service_name in open_ports:
            print(f'Port {port}: {service_name}')
    else:
        print('No open ports found.')

def get_service_name(port):
    try:
        service_name = socket.getservbyport(port)
        return service_name
    except OSError:
        return "Unknown"

if __name__ == "__main__":
    ip = input("Enter the target IP address: ")
    asyncio.run(port_scan(ip))
