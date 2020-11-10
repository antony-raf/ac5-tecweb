from flask import Flask
from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:thuglove3@localhost/times'
db = SQLAlchemy(app)

class times(db.Model):
    __tablename__ = 'cadastros'
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(50))
    localEquipe = db.Column(db.String(20))
    corequipe1 = db.Column(db.String(10))
    corequipe2 = db.Column(db.String(10))
    def __init__(self, nome, localEquipe, corequipe1, corequipe2):
        self.nome = nome
        self.localEquipe = localEquipe
        self.corequipe1 = corequipe1
        self.corequipe2 = corequipe2

db.create_all()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/equipes')
def equipes():
        return render_template("equipes.html")

@app.route("/novasPartidas")
def nvoasPartidas():
    return render_template("novasPartidas.html")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/mensagem")
def mensagem():
    return render_template("mensagem.html")

@app.route("/cadastrar",methods=['GET', 'POST'])
def cadastrar():
    if request.method =="POST":
        nome = (request.form.get("nome"))
        localEquipe = (request.form.get("localEquipe"))
        corequipe1 = (request.form.get("corequipe1"))
        corequipe2 = (request.form.get("corequipe2"))
        if nome:
            g = times(nome,localEquipe,corequipe1,corequipe2)
            db.session.add(g)
            db.session.commit()
    return redirect(url_for("mensagem"))

if __name__ == "__main__":
    app.run(debug=True)
