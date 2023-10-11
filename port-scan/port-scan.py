import socket
import sys

def scan_port(host, port):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.close()
    return True
  except socket.error:
    return False

def main():
  host = sys.argv[1]
  port_range = range(1, 65535)

  open_ports = []

  for port in port_range:
    if scan_port(host, port):
      open_ports.append(port)

  if not open_ports:
    print("All ports are closed")
  else:
    for port in open_ports:
      print("Port %d" % port)

if __name__ == "__main__":
  main()

