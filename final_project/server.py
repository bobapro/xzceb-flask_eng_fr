from machinetranslation import translator
from flask import Flask, render_template, request
import json
from machinetranslation.translator import english_to_french, french_to_english

app = Flask("Web Translator")

def get_html():
    html = f'''
            <html>
                <body>

                <h2>French -> English</h2>

                <form action="/frenchToEnglish">
                  <label for="fname">Enter French:</label><br>
                  <input type="text" id="fname" name="frword" value="Bonjour le monde"><br>
                  <input type="submit" value="Translate!">
                </form> 

                <h2>English -> French</h2>

                <form action="/englishToFrench">
                  <label for="fname">Enter French:</label><br>
                  <input type="text" id="fname" name="eword" value="Hello world"><br>
                  <input type="submit" value="Translate!">
                </form> 

                </body>
                </html>
                '''

    return html


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('eword')
    return get_html() + f"<br>English to French:<br>{textToTranslate}   -> {english_to_french(textToTranslate)}"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('frword')
    return get_html() + f"<br>French to English:<br>{textToTranslate}   -> {french_to_english(textToTranslate)}"

@app.route("/")
def renderIndexPage():
    return get_html()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
