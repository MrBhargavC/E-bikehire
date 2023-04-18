from flask import render_template
from flask import Flask

from datetime import datetime
import os

app = Flask(__name__,  template_folder='templates', static_folder='static')


@app.route('/', methods=['GET', 'POST'])
def signomein():
    return render_template("home.html")



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    

