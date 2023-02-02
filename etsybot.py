import requests
import time
import Parser as Parser
import sys, getopt


requests.packages.urllib3.disable_warnings()


def get_help():
    return "python main.py -k <keyword> -p <codigo_pais> -n <numero_de_paginas>\r\n" \
           "Ejemplo: main.py -k \"pendientes de plata\" -p ES -n 5"


def main(argv):
    keyword = input("Introduce la keyword: ")
    if keyword == '':
        exit("Debe introducir una keyword de busqueda. Por ejemplo: tazas personalizables")
    country = input("Introduce el pais: ").upper()
    if country == '' or len(country) != 2:
        exit("El pais debe ser en su formato del código ISO de 2 digitos - https://www.iban.com/country-codes")
    number_pages = input("Introduce el numero de paginas: ")
    if number_pages == '':
        exit("El numero de paginas a buscar debe ser numerico")

    inicio = time.time()
    dr = Parser.Parser(keyword, country)
    dr.delete_imgs()
    print("Parseando las " + str(number_pages) + " primeras paginas en " + str(country) + " de: " + str(keyword))
    print("El proceso puede tardar un rato. Sea paciente")
    for a in range(1, int(number_pages) + 1):
        response1 = dr.primera_peticion()
        if response1 == 2:
            dr.pasar_pagina()
            continue
        response2 = dr.segunda_peticion()
        if response2 == 2:
            dr.pasar_pagina()
            continue
        if response1 == 0 or response2 == 0:
            break
        print(str(dr.contador_productos) + " items parseados en la pagina " + str(dr.pagina))
        dr.pasar_pagina()

    fin = time.time()
    dr.delete_images()
    #Limpiamos images
    print("Tiempo de ejecucion: " + str(fin - inicio))


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except SystemExit as e:
        print('Error!', e)
        print('Presiona una tecla (y soluciona el problema)')
        input()