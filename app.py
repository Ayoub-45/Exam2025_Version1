import random
import time
from flask import Flask, jsonify, render_template, request, redirect, url_for
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Metrics
views_product = Counter('views_by_product', 'Number of views by product', ['product'])
sales_duration = Histogram('sales_duration_seconds', 'Time spent processing sales')

# Product data
products = {
    1: {'description': 'Apple', 'price': 0.5},
    2: {'description': 'Banana', 'price': 0.3},
    3: {'description': 'Orange', 'price': 0.4},
    4: {'description': 'Mango', 'price': 1.0}
}

sales_history = []

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/calculate', methods=['POST'])
def calculate():
    product_code = int(request.form['product'])
    product_info = products.get(product_code)

    if product_info is None:
        return "Invalid product", 400

    quantity = int(request.form['quantity'])
    total = quantity * product_info['price']
    sales_history.append({
        'product': product_info['description'],
        'quantity': quantity,
        'total': total
    })
    views_product.labels(product=product_info['description']).inc()
    return render_template('result.html', product=product_info['description'], quantity=quantity, total=total)

@app.route('/sales', methods=['GET'])
def sales():
    return render_template('sales.html', sales=sales_history)

@app.route('/sales', methods=['POST'])
@sales_duration.time()
def sales_view():
    data = request.json
    product = data.get("product", "unknown")
    time.sleep(random.uniform(0.1, 0.5))  # Simulate processing
    return jsonify({"message": f"Sale completed for {product}"}), 200

@app.route('/back')
def back():
    return redirect(url_for('index'))

@app.route("/metrics")
def metric():
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4; charset=utf-8'}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
