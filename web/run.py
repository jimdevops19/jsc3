from jsc3 import app
import os

if __name__ == '__main__':
    app.run(
        os.environ.get('HOST', '0.0.0.0'),
        port=5000,
        debug=os.environ.get('DEBUG') == '1'
    )