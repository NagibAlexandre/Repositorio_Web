from flask import Flask, render_template


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('God of War', 'Ação', 'Playstation')
jogo2 = Jogo('Cs:Go', 'Tiro', 'PC')
jogo3 = Jogo('Minecraft', 'Construção', 'PC')

ListaJ = [jogo1, jogo2, jogo3]

app = Flask(__name__)


@app.route('/inicio')
def ola():
    return render_template('lista.html',titulo='Meus Jogos', jogos=ListaJ)


app.run()