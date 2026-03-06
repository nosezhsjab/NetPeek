import socket
import time
from concurrent.futures import ThreadPoolExecutor

#codigo echo por chatGPT, haci que no me pregunten nada weyes.
#att: NST
TIMEOUT = 0.3
MAX_THREADS = 200


def scan_port(ip, port):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)

        result = s.connect_ex((ip, port))

        if result == 0:
            print(f"[OPEN] {port}/tcp")

        s.close()

    except:
        pass


def escanear_host(ip):

    print(f"\nEscaneando host: {ip}")
    print("Puertos 1-1024\n")

    start = time.time()

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        executor.map(lambda port: scan_port(ip, port), range(1,1025))

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

    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(lambda port: scan_port(ip, port), common_ports)

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

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        executor.map(lambda port: scan_port(ip, port), range(inicio,fin+1))

    end = time.time()

    print("\nScan terminado")
    print(f"Tiempo: {round(end-start,2)} segundos")