import requests
import time
import Parser as Parser
import sys, getopt
import download as download

requests.packages.urllib3.disable_warnings()


def get_help():
    return "python main.py -k <keyword> -p <codigo_pais> -n <numero_de_paginas>\r\n" \
           "Ejemplo: main.py -k \"pendientes de plata\" -p ES -n 5"


def main(argv):
    keyword = ''
    country = ''
    number_pages = 0
    opts, args = getopt.getopt(argv, "hk:p:n:", ["keyword=", "pais=", "pages="])
    for opt, arg in opts:
        if opt == '-h':
            print('python main.py -k <keyword> -p <codigo_pais> -n <numero_de_paginas>')
            sys.exit()
        elif opt in ("-k", "--keyword"):
            keyword = arg
        elif opt in ("-p", "--pais"):
            country = arg
            if len(country) != 2:
                print(
                    "El pais debe estar en su formato ISO-2, puede buscarlo en la siguiente web: https://es.wikipedia.org/wiki/ISO_3166-1_alfa-2")
                print(get_help())
                sys.exit()
        elif opt in ("-n", "--pages"):
            number_pages = arg
    if keyword == '' or country == '' or number_pages == 0:
        print(get_help())
        sys.exit()

    inicio = time.time()
    dr = Parser.Parser(keyword, country)
    dr.create_data_table()
    print("Parseando las " + str(number_pages) + " primeras paginas en " + str(country) + " de: " + str(keyword))
    for a in range(1, int(number_pages) + 1):
        response1 = dr.primera_peticion()
        response2 = dr.segunda_peticion()
        if response1 == 0 or response2 == 0:
            break
        print(str(dr.contador_productos) + " items parseados en la pagina " + str(dr.pagina))
        dr.pasar_pagina()

    fin = time.time()
    print("Generando fichero .xlsx")
    download.downloadfile(dr.dbname)
    print("Tiempo de ejecucion: " + str(fin - inicio))


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except SystemExit as e:
        print('Error!', e)
        print('Presiona una tecla (y soluciona el problema)')
        input()
