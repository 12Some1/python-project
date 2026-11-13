from flask import Flask
import random as rd

facts =[ "A maioria das pessoas que sofre de dependência tecnológica sente um forte estresse quando fica fora da área de cobertura de rede ou não pode usar seus dispositivos",
         "De acordo com um estudo realizado em 2018, mais de 50 das pessoas entre 18 e 34 anos se consideram dependentes de seus smartphones.",
         "O estudo da dependência tecnológica é uma das áreas mais relevantes da pesquisa científica moderna",
         "Segundo um estudo de 2019, mais de 60 das pessoas respondem a mensagens de trabalho em seus smartphones dentro de 15 minutos após sair do trabalho"
        ]

charadas = ["O que é, o que é? Tem cabeça, tem dente, mas não é gente.",
            "O que é, o que é? Tem asas, mas não voa.",
            "O que é, o que é? Tem quatro patas e um rabo, mas não é um animal. ",
            "O que é, o que é? Tem olhos, mas não vê. "
           ]

app = Flask(__name__)

@app.route("/") 
def home(): 
    return f"<h1>Página inicial</h1>" "<a href="'/random_fact'">Veja um fato aleatório!</a><br><a href="'/charadas'">Veja uma charada!</a>"

@app.route("/random_fact")
def random_fact():
    fact = rd.choice(facts)
    return f"<h1>Fato aleatório</h1><p>{fact}</p><a href='/'>Voltar para a página inicial</a>"

@app.route("/charadas")
def charadas():
    charada = rd.choice(charadas)
    return f"<h1>Charadas</h1><p>{charada}</p><a href='/'>Voltar para a página inicial</a>"



app.run(debug=True)