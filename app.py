import pandas as pd
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

df=pd.read_csv("https://dati.comune.milano.it/dataset/108af032-bd90-481d-a08d-f976f4bd5b1b/resource/720717c5-9533-4596-bfe2-b797fe0df944/download/ds1880_studenti_scuola_secondaria_2grado_sudd_indirizzo_statale_as_2020_2021_no_dupl.csv", sep=";")

@app.route('/')
def home():
    return render_template('home.html', df=df)

@app.route('/result')
def result():
    schName = request.args.get('school')
    scelta=df[df.DenominazioneIstitutoRiferimento==schName.upper()]
    return render_template('result.html', scelta=scelta)

if __name__ == '__main__':
    app.run(debug=True)