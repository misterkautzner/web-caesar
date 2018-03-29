from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE HTML>
    <html>
        <head>
            <style>
                form {
                    background-color:#eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <form method="post">
                <label for="rot">
                    Rotate by: 
                    <input type="text" name="rot" value=0 />
                </label>
                <br />
                <br />
                <input type="textarea" name="text" />
                <br />
                <input type="submit" value="Submit Query" />
        </body>
    </html>
    """

@app.route('/', methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    
    if validate_int(rot):
        rot = int(rot)
    
    encrypted = rotate_string(text, rot)
    encrypted_html = "<h1>{0}</h1>".format(encrypted)

    return encrypted_html


def validate_int(maybe_int):
    try:
        int(maybe_int)
    except(ValueError):
        return False
    return True


@app.route('/')
def index():
    return form

app.run()