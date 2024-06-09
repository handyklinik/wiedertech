from flask import Flask, render_template

app = Flask(__name__)

# Sample data
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 500, "description": "A powerful laptop."},
    {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 300, "description": "A latest model smartphone."},
    {"id": 3, "name": "Headphones", "category": "Electronics", "price": 50, "description": "Noise-cancelling headphones."},
    {"id": 4, "name": "Monitor", "category": "Electronics", "price": 200, "description": "A high-resolution monitor."}
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
