import requests 

def obtener_categorias():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print('codigo de estado: ', r.status_code)
    print('contenido: ', r.text)
    print('tipo de dato: ', type(r.text))
    categorias = r.json()
    for categoria in categorias:
        print('nombre: ', categoria['name'])
        