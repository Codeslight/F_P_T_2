# Import
from flask import Flask, render_template,request, redirect
import k
import main2
app = Flask(__name__)
# SQLite'ı bağlama
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/cevap', methods=["POST"])
def cevap():
    c_m=request.form.get("subtitle")
    print(c_m)
    c2=main2.c(c_m)
    
    return render_template("s_a.html", c2=c2)


# Dinamik beceriler

@app.route('/', methods=['POST'])
def process_form():
    button_chat = request.form.get('button_chat')
    button_python = request.form.get('button_python')
    return render_template('index.html', button_chat=button_chat, button_python=button_python)

    
@app.route('/ses')
def ses():
    s=k.tr_konusma()
    return render_template("s_a.html", s=s)


if __name__ == "__main__":
    app.run(debug=True)
