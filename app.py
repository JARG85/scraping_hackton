from scraping import make_scraping
from flask import Flask

import asyncio
import aiohttp

app = Flask(__name__)

@app.route('/')
def hello_world():
    async make_scraping
    return '¡Hola, mundo desde Flask!'

if __name__ == '__main__':
    app.run(debug=True)