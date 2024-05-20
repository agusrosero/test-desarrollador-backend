"""
Manejo de Archivos y Expresiones Regulares

Pregunta: Escriba una función en Python que lea un archivo de texto y cuente el número de direcciones de correo electrónico válidas. Use expresiones regulares para identificar las direcciones de correo electrónico.
"""
import re


def email_counter(file):
    regex = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

    try:
        with open(file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: El archivo {file} no fue encontrado.")
        return 0
    except IOError:
        print(f"Error: No se puede leer el archivo {file}.")
        return 0

    emails = re.findall(regex, content)
    number_of_mails = len(emails)
    return number_of_mails


file = "./file.txt"
email_amount = email_counter(file)
print(f"Correos validos: {email_amount}")
