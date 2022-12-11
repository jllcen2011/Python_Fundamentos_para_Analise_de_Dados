from flask import Flask

app = Flask(__name__) #nome do meu aplicativo é app
@app.route("/") #quer dizer que essa app ficará no diretório raíz, ou seja, 
                #"07 - CriandoApli....MiniProjeto5"
# criando uma função que irá permitir executar uma ação nessa app
def hello():
    return "Hello, World!"

if __name__ == "__main__":      #executando o app. Ou seja, se eu estiver no bloco main
    app.run()                            # (ou seja, to na pasta raíz), usar o == main
