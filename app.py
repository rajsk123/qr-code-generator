from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_img = None
    if request.method == 'POST':
        data = request.form.get('data')
        if data:
            img = qrcode.make(data)
            buf = io.BytesIO()
            img.save(buf, format='PNG')
            buf.seek(0)
            return send_file(buf, mimetype='image/png', as_attachment=True, download_name='qr.png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
