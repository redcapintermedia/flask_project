from flask import Flask  
import os  

app = Flask(__name__)  

@app.route('/')  
def home():  
    return "Hello from Railway!"  

import os
port = int(os.environ.get("PORT", 8080))
app.run(host="0.0.0.0", port=port)

