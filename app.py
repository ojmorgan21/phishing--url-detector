from flask import Flask, request, render_template_string
import train

app = Flask(__name__)

HTML = """
<h2>Phishing URL Detector</h2>
<form method="POST">
<input name="url" placeholder="Paste URL here" style="width:300px;padding:8px">
<button style="padding:8px">Check</button>
</form>
{% if result %}<h3>{{result}}</h3><p>Score: {{score}}</p>{% endif %}
"""

@app.route('/', methods=['GET','POST'])
def home():
    result = None
    score = 0
    if request.method == 'POST':
        url = request.form['url']
        score = train.score(url)
        result = "PHISHING - DANGER" if score >= 5 else "SAFE - Legit"
    return render_template_string(HTML, result=result, score=score)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

