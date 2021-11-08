import datetime

from flask import Flask, render_template
import datetime
import random
app = Flask(__name__)


szam1 = 5
szam2 = 7
szorzat = szam1 * szam2
ido = datetime.datetime.utcnow()

megyek = [
    '<td>Fejér</td><td>22</td>',
    '<td>Pest</td><td>4</td>',
    '<td>Zala</td><td>0</td>',
    '<td>Borsod</td><td>0</td>',

]

@app.route('/')
def index_site():
    return render_template("index.html",
                           jinjaszorzat=szorzat,
                           szerverido=ido,
                           veletlenszam=random.randint(1,14)
                           )

@app.route("/about")
def about():
    return render_template("about.html",
                           megyek=megyek
                           )

#HTTP státuszkódok:
# 200 - OK
# 404 - Erőforrás nem található a szerveren
# 500 - Internal server error - belső szerveroldali hiba

if __name__ == '__main__':
    app.run()