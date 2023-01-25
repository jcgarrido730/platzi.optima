import tienda
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def obtener_lista():
    return [1, 2, 3]

@app.get('/contacto')
def obtener_diccionario():
    return {'nombre': 'mi nombre'}

@app.get('/retornaHTML', response_class=HTMLResponse)
def obtener_html():
    return """
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    """

def run():
    tienda.obtener_categorias()

if __name__ == '__main__':
    run()
