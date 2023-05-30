import base64
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

df=pd.read_csv("https://dati.comune.milano.it/dataset/108af032-bd90-481d-a08d-f976f4bd5b1b/resource/720717c5-9533-4596-bfe2-b797fe0df944/download/ds1880_studenti_scuola_secondaria_2grado_sudd_indirizzo_statale_as_2020_2021_no_dupl.csv", sep=";")
df["somma"]=df.ALUNNIMASCHI + df.ALUNNIFEMMINE
df1=df.groupby("PERCORSO")[["somma"]].count().sort_values(by=["somma"],ascending=False).reset_index()



@app.route('/')
def home2():
    return render_template('home2.html')

@app.route('/result2')
def result2():
    fig1, ax = plt.subplots(figsize=(10,8))
    ax.bar(df1.PERCORSO, df1.somma.sort_values(ascending=False),label="Studenti", color =["green"])
    plt.xticks(rotation=90,fontsize=15)
    ax.legend()
    ax.set_xlabel('Percorsi attivati')
    ax.set_ylabel('Numero di Studenti')
    ax.set_title("Studenti iscritti ai diversi percorsi")

    buf1 = BytesIO()
    fig1.savefig(buf1, format="png")
    data1 = base64.b64encode(buf1.getbuffer()).decode("ascii")
    return render_template('result2.html', image=f'data:image/png;base64,{data1}')


if __name__ == '__main__':
    app.run(debug=True)