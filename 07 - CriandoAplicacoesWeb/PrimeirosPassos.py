from flask import Flask

app = Flask(__name__)       #nome do meu aplicativo é __name__
@app.route("/")             #quer dizer que essa app mostrará la na pagina da web, de cara, a resposta
                            #da função hello() criada abaixo

# criando uma função que irá permitir executar uma ação nessa app
def hello():
    return "Hello, World!"

if __name__ == "__main__":      #executando o app. Se eu estiver no bloco main, usar == main
    app.run()                           
