# NetPeek

```text
 _   _      _   ____            _
| \ | | ___| |_|  _ \ ___  ___| | __
|  \| |/ _ \ __| |_) / _ \/ __| |/ /
| |\  |  __/ |_|  __/  __/ (__|   <
|_| \_|\___|\__|_|   \___|\___|_|\_\
```

Beginner-Friendly Network Recon Tool

---

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-learning%20project-orange)

NetPeek es una herramienta de **reconocimiento de red enfocada en aprendizaje**.

El objetivo del proyecto no es competir con herramientas como Nmap, sino ayudar a personas que están empezando en **ciberseguridad, redes o pentesting** a entender cómo funcionan los escaneos de puertos.

NetPeek intenta mostrar **qué ocurre detrás del escaneo**, no solo los resultados.

---

# Tabla de Contenidos

* [Motivación](#motivación)
* [Características](#características)
* [Instalación](#instalación)
* [Uso](#uso)
* [Ejemplo de salida](#ejemplo-de-salida)
* [Arquitectura del proyecto](#arquitectura-del-proyecto)
* [Cómo funciona el escaneo](#cómo-funciona-el-escaneo)
* [Puertos comunes](#puertos-comunes)
* [Roadmap](#roadmap)
* [Contribuir](#contribuir)
* [Uso ético](#uso-ético)
* [Licencia](#licencia)

---

# Motivación

Cuando empiezas en ciberseguridad, muchas herramientas son muy potentes pero también muy complejas.

Por ejemplo:

* escáneres con cientos de flags
* resultados difíciles de interpretar
* poca explicación educativa

NetPeek intenta resolver eso con una filosofía simple:

> Una herramienta que puedas leer, entender y modificar mientras aprendes.

El proyecto está diseñado para ser **un laboratorio educativo** además de una herramienta funcional.

---

# Características

* Escaneo de puertos TCP
* Escaneo rápido de puertos comunes
* Escaneo de lista personalizada
* Escaneo de rango de puertos
* Explicaciones educativas de servicios comunes
* Salida clara pensada para terminal

---

# Instalación

## Requisitos

* Python 3.10 o superior
* Terminal o shell

## Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/netpeek.git
cd netpeek
```

## Crear entorno virtual

Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Uso

Escaneo de puertos comunes:

```bash
python netpeek.py --target 192.168.1.10 --common
```

Escaneo de lista de puertos:

```bash
python netpeek.py --target 192.168.1.10 --ports 22,80,443
```

Escaneo de rango:

```bash
python netpeek.py --target 192.168.1.10 --range 1-1024
```

Timeout personalizado:

```bash
python netpeek.py --target 192.168.1.10 --common --timeout 0.5
```

---

# Ejemplo de salida

```
NetPeek v0.1
Target: 192.168.1.10

[OPEN] 22/tcp → SSH
Remote secure shell access.

[CLOSED] 80/tcp → HTTP

[OPEN] 443/tcp → HTTPS
Encrypted web traffic.

Scan completed.
10 ports scanned in 1.8 seconds
```

---

# Arquitectura del proyecto

Estructura sugerida:

```
netpeek/
│
├── NetPeek.py
├── scanner.py
├── ports.py
├── utils.py
│
├── README.md
├── requirements.txt
└── LICENSE
```

Descripción de módulos:

**netpeek.py**
Punto de entrada del programa y CLI.

**scanner.py**
Lógica principal de escaneo de puertos.

**ports.py**
Diccionario con puertos comunes y sus explicaciones.

**utils.py**
Funciones auxiliares.

---

# Cómo funciona el escaneo

NetPeek utiliza el módulo `socket` de Python.

Proceso simplificado:

1. El usuario define un objetivo (IP o dominio).
2. El programa intenta abrir una conexión TCP a cada puerto.
3. Si la conexión responde → el puerto está abierto.
4. Si no responde → el puerto se marca como cerrado.

Este método se conoce como:

**TCP Connect Scan**

Es uno de los métodos más simples de escaneo de puertos.

---

# Puertos comunes

Algunos puertos importantes que NetPeek puede explicar:

| Puerto | Servicio   |
| ------ | ---------- |
| 21     | FTP        |
| 22     | SSH        |
| 23     | Telnet     |
| 25     | SMTP       |
| 53     | DNS        |
| 80     | HTTP       |
| 443    | HTTPS      |
| 445    | SMB        |
| 3389   | RDP        |
| 3306   | MySQL      |
| 5432   | PostgreSQL |

---

# Roadmap

Futuras mejoras planeadas:

v0.2

* banner grabbing (detección básica de servicios)

v0.3

* exportar resultados a JSON

v0.4

* descubrimiento de hosts en red local

v0.5

* escaneo concurrente

v0.6

* modo educativo más detallado

---

# Contribuir

Las contribuciones son bienvenidas.

Ideas para contribuir:

* mejorar documentación
* agregar puertos y explicaciones
* mejorar rendimiento
* agregar nuevos modos de escaneo

Proceso:

1. Fork del repositorio
2. Crear rama
3. Realizar cambios
4. Enviar Pull Request

---

# Uso ético

NetPeek es una herramienta educativa.

Usa el software únicamente en:

* sistemas propios
* laboratorios de práctica
* redes donde tengas permiso explícito

El uso no autorizado puede ser ilegal.

---

# Licencia

MIT License

Este proyecto está licenciado bajo MIT, lo que permite usar, modificar y redistribuir el software libremente.
