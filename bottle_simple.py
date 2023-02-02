# -*- coding: utf-8 -*-


from bottle import route, run, template, static_file, response

@route('/hello/<name>')
@route('/hello/')
@route('/hello')
def hello(name="Fritz"):
    return template('Hello {{name}}, how are you?', name=name)

run(host='0.0.0.0', port=80, debug=True)