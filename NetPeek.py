import webbrowser

NetPeek_ascii = """
 _   _      _   ____            _    
| \ | | ___| |_|  _ \ ___  ___ | | __
|  \| |/ _ \ __| |_) / _ \/ _ \| |/ /
| |\  |  __/ |_|  __/  __/ (_) |   < 
|_| \_|\___|\__|_|   \___|\___/|_|\_\

      simple port recon tool
"""

def main():
    #definimiento de variables ;v
    global NetPeek_ascii
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
Selecciona una opción: """
    print(NetPeek_ascii, end="")
    print(main_text, end="")
    opcion = int(input())
    if opcion == 5: quit()
    elif opcion == 4:
        webbrowser.open("ayuda.html")
main()