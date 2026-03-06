import socket
import time

def scan_port(ip, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((ip, port))

    if result == 0:
        print(f"[OPEN] {port}/tcp")
    else:
        print(f"[CLOSED] {port}/tcp")

    s.close()


def escanear_host(ip):

    print(f"\nEscaneando host: {ip}")
    print("Puertos 1-1024\n")

    start = time.time()

    for port in range(1, 1025):
        scan_port(ip, port)

    end = time.time()

    print("\nScan terminado")
    print(f"Tiempo: {round(end-start,2)} segundos")


def escan_rapido(ip):

    common_ports = [
        21,22,23,25,53,
        80,110,139,143,
        443,445,3389,3306
    ]

    print(f"\nEscaneo rápido contra {ip}\n")

    start = time.time()

    for port in common_ports:
        scan_port(ip, port)

    end = time.time()

    print("\nScan terminado")
    print(f"Tiempo: {round(end-start,2)} segundos")


def rango_de_puertos(ip):

    rango = input("Rango (ej: 1-1024): ")

    inicio, fin = rango.split("-")

    inicio = int(inicio)
    fin = int(fin)

    print(f"\nEscaneando {ip} puertos {inicio}-{fin}\n")

    start = time.time()

    for port in range(inicio, fin+1):
        scan_port(ip, port)

    end = time.time()

    print("\nScan terminado")
    print(f"Tiempo: {round(end-start,2)} segundos")