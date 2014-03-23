import json
from django.template.loader import render_to_string
from django.conf import settings
from flask import Flask

app = Flask(__name__)
settings.configure(
    DEBUG=True,
    TEMPLATE_DEBUG=True,
    TEMPLATE_DIRS=['templates/'],
)
with open('data.json') as file:
    context = json.load(file)


@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def wireframe(path):
    return str(render_to_string(path, context))

if __name__ == '__main__':
    app.run()
