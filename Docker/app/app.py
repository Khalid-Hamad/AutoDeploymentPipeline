from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Flask App</title>
          </head>
          <body>
            <div style="text-align:center; margin-top:50px;">
              <button onclick="displayMessage()">Click Me</button>
              <p id="message" style="margin-top:20px;"></p>
            </div>
            <script>
              function displayMessage() {
                document.getElementById('message').innerText = "Hi there, I hope you enjoy exploring this small project";
              }
            </script>
          </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
