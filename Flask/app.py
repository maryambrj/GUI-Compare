from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField
from PIL import Image
import os
import base64
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class SaveMaskForm(FlaskForm):
    save = SubmitField('Save Mask')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SaveMaskForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

@app.route('/save_mask', methods=['POST'])
def save_mask():
    data = request.json
    mask_data = data['mask_data']

    mask_img = Image.open(BytesIO(base64.b64decode(mask_data.split(',')[1])))
    mask_img_name = "ice_cream_mask.png"
    mask_img.save(os.path.join('static', mask_img_name))

    return jsonify(status='success')

if __name__ == "__main__":
    app.run(debug=True)
