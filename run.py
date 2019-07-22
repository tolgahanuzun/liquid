from app.settings import app, database
from app import liquid


app.add_url_rule('/', '/', liquid.home, ['GET', 'POST'])


app.debug = True
app.secret_key = "secret_key"
app.run(host='0.0.0.0')
