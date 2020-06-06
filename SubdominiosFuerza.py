import dns.resolver
from os import path
import argparse

parser =argparse.ArgumentParser(description="Script para realizar fuerza bruta subdominios")
parser.add_argument('-o', '--objetivo', help="nombre dominio sin el 'WWW'")
parser =parser.parse_args()
print('Iniciando...')
def main():
    if parser.objetivo:
        objetivo = parser.objetivo
        if path.exists('subdominios.txt'):
            wordlist = open('subdominios.txt', 'r')
            wordlist = wordlist.read().split('\n')
            lista = []
            for s in wordlist:
                try:                    
                    dns.resolver.query('{}.{}'.format(s,objetivo), 'A')
                    lista.append('{}.{}'.format(s, objetivo))
                    print('{}.{}'.format(s, objetivo))
                except:
                    pass
            if len(lista) > 0:
                print('--------------------------------------------------------------------------------------')
                print('Numero de subdominios posibles: {}'.format(len(lista)))
                for e in lista:
                    
                    print(e)
            else:
                print('No se encontraron subdominios')
        else:
            print('No existe el archivo subdominios.txt')
    else:
        print("No hay objetivo")
       

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
    