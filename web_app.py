import os
import pydevd_pycharm
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = 'Hello World!'
    return msg

def attach():
  if os.environ.get('WERKZEUG_RUN_MAIN'):
    print('Connecting to debugger...')
    pydevd_pycharm.settrace('localhost', port=3500, stdoutToServer=True, stderrToServer=True)

if __name__ == '__main__':
  print('Starting hello-world server...')
  # comment out to use Pycharm's remote debugger
  # attach()

  app.run(host='localhost', port=8080)
