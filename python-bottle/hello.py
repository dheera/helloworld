#!/usr/bin/python
import bottle

app = bottle.default_app()

@app.route('/')
def index():
  return 'Hello world!'

@app.route('/<path>')
def index_name(name):
  return bottle.template('Hello {{path}}', path=path)

if __name__ == '__main__':
  app.run(host='localhost', port=5000)
