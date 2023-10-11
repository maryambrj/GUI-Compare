from flask import Flask, render_template, jsonify, request
import imageio.v2 as imageio

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store_coordinates', methods=['POST'])
def store_coordinates():
    x = request.json.get('x')
    y = request.json.get('y')
    
    # Manipulating the coordinates (e.g., multiplying by 2)
    x_transformed = x * 2
    y_transformed = y * 2
    
    print(f"Received coordinates: x = {x}, y = {y}")
    print(f"Transformed coordinates: x = {x_transformed}, y = {y_transformed}")
    
    return jsonify({"x_transformed": x_transformed, "y_transformed": y_transformed})

if __name__ == '__main__':
    imagefile="./static/dog.png"
    imagefile="./static/ice_cream.png"
    im = imageio.imread(imagefile);
    imageio.imwrite('./static/targetimg.png',im);
    im[:,:,:] = 0;
    im[10:50,10:50,0] = 255;
    im[10:50,10:50,3] = 255;
    imageio.imwrite('./static/maskimg.png',im);

    print(im.shape)


    app.run(debug=True)
