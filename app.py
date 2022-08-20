from flask import Flask
import pymysql

conn= pymysql.connect(host = 'tested.cya2lw5rkrbc.ap-south-1.rds.amazonaws.com' , port = 3306 ,user = 'Anirudh' , password = 'Ani##365##' ,db = 'anime' )

app=Flask(__name__)

@app.route("/")
def home():
    cur=conn.cursor()
    cur.execute("SELECT * FROM anime.ranking")
    details=cur.fetchall()
    return list(details)

if  __name__=="__main__":
	app.run()
