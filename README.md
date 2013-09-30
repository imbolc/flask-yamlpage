flask-yamlpage
==============
Flatpages in yaml syntax

app.py
------
    from flask import Flask
    from flask_yamlpage import FlaskYamlPage


    app = Flask(__name__)
    yamlpages = FlaskYamlPage(app)


    @app.route('/')
    def index():
        return 'index'


    if __name__ == '__main__':
        app.run(debug=True, port=8000)


yamlpages/#test#.yml
-------------------
    title: test yamlpage
    body: |
        Yamlpage
        ========
        Hello, world!
        {{ url_for('index') }}


templates/yamlpage.html
-----------------------
    <title>{{ page.title }}</title>

    {{ page.body | render | markdown | safe }}


config defaults
---------------
    'YAMLPAGE_CONTENT_DIR'      : './yamlpages',
    'YAMLPAGE_DEFAULT_TEMPLATE' : 'yamlpage.html',
    'YAMLPAGE_AUTO_ROUTING'     : True,
    'YAMLPAGE_MARKDOWN_FILTER'  : True,
    'YAMLPAGE_RENDER_FILTER'    : True,
