import webbrowser
import time
import scanner as sc
import os
from colorama import init, Fore

init(autoreset=True)

NetPeek_ascii = """
 _   _      _   ____            _    
| \ | | ___| |_|  _ \ ___  ___ | | __
|  \| |/ _ \ __| |_) / _ \/ _ \| |/ /
| |\  |  __/ |_|  __/  __/ (_) |   < 
|_| \_|\___|\__|_|   \___|\___/|_|\_\

      simple port recon tool
"""

import webbrowser
import time
import scanner as sc

NetPeek_ascii = """
 _   _      _   ____            _    
| \ | | ___| |_|  _ \ ___  ___ | | __
|  \| |/ _ \ __| |_) / _ \/ _ \| |/ /
| |\  |  __/ |_|  __/  __/ (_) |   <
|_| \_|\___|\__|_|   \___|\___/|_|\_\

      simple port recon tool
"""

def main():

    while True:

        main_text = f"""
{'='*50}
              NETPEEK - MAIN MENU
{'='*50}

[1] Escanear host (IP o dominio)
[2] Escaneo rápido (puertos comunes)
[3] Escaneo personalizado (rango de puertos)
[4] Ayuda / explicación de puertos
[5] Salir

{'='*50}
"""

        print(NetPeek_ascii)
        print(main_text)

        try:
            opcion = int(input("Selecciona una opción: "))

            if opcion == 5:
                quit()

            elif opcion == 4:
                webbrowser.open("ayuda.html")

            elif opcion == 3:
                ip = input("Target (IP o dominio): ")
                sc.rango_de_puertos(ip)

            elif opcion == 2:
                ip = input("Target (IP o dominio): ")
                sc.escan_rapido(ip)

            elif opcion == 1:
                ip = input("Target (IP o dominio): ")
                sc.escanear_host(ip)

            else:
                print("Opción fuera de rango.")

        except ValueError as e:
            
            print(Fore.RED + f"Opción no válida. Ingresa un número.\nError:", Fore.RESET + Fore.MAGENTA + str(e))
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
main()
