from typing import Text
from flask import Flask, render_template , request ,flash
from model import read
import mysql.connector as sql
from mysql.connector.constants import ClientFlag
from model import *


app = Flask(__name__)

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/about')
def about():
 return render_template('about.html')

@app.route('/history', methods=['POST', 'GET'])
def history():
    config ={
                'user': 'root',
                'password': 'pass123',
                'host': '34.121.155.244',
                'database':'insurancedb',
                'client_flags': [ClientFlag.SSL],
                'ssl_ca': 'ssl/server-ca.pem',
                'ssl_cert': 'ssl/client-cert.pem',
                'ssl_key': 'ssl/client-key.pem'
                            }
    cnx = sql.connect(**config) 
    cur = cnx.cursor()
    cur.execute("select * from data")
    rows = cur.fetchall()
    cnx.close()
    return render_template('history.html', rows= rows)

#inference
@app.route('/inference', methods=['POST', 'GET'])
def inference():
    if request.method == 'POST':
        sex = request.form['sex']
        smoker =request.form['smoker']
        bmi = request.form['bmi']
        region = request.form['region']
        age=request.form['age']
        children = request.form['kid']

        if not sex:
            flash('enter sex male or female')
        else:
            expense = read(sex,smoker,region,age, bmi,children)
            #Gcloud
            config ={
            'user': 'root',
            'password': 'pass123',
            'host': '34.121.155.244',
            'database':'insurancedb',
            'client_flags': [ClientFlag.SSL],
            'ssl_ca': 'ssl/server-ca.pem',
            'ssl_cert': 'ssl/client-cert.pem',
            'ssl_key': 'ssl/client-key.pem'
                        }
        # now we establish our connection
            with sql.connect(**config) as cnx:
                        cur = cnx.cursor() # initialize connection cursor

                        cur.execute("insert into data(sex,smoker,region,age,bmi,children,insurance) VALUES (%s,%s,%s,%s,%s,%s,%s)",(sex,smoker,region,age,bmi,children,expense))

                        cnx.commit()
                        cnx.close()
            return render_template('inference.html',expense = expense)
    return render_template('inference.html')
if __name__ == "__main__":    
      app.run(debug=True,port=8080,host='0.0.0.0')
