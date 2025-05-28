# 🛒 Flask Sales App with Prometheus & Grafana Monitoring

A simple Flask-based web application to simulate product sales and monitor metrics such as product views and sales latency using **Prometheus** and **Grafana**.

---

## 🚀 Features

- View and select products to "purchase"
- Tracks number of views per product
- Measures sales processing latency
- Exposes Prometheus metrics
- Includes Grafana dashboard for visualization

---

## ⚙️ Technologies

- Python 3, Flask
- Prometheus + Flask Exporter
- Grafana
- Docker + Docker Compose

---

## 📦 Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 📁 Project Structure

├── app.py # Flask application
├── Dockerfile # Dockerfile for Flask app
├── requirements.txt # Python dependencies
├── prometheus/
│ └── prometheus.yaml # Prometheus config file
├── docker-compose.yaml # Multi-container setup
├── templates/ # HTML templates
└── README.md

---

## 🧪 Metrics Exposed

- `views_by_product{product="Apple"}` – Number of views per product
- `sales_duration_seconds` – Histogram measuring time spent processing sales

📍 Metrics endpoint:  
[http://localhost:5000/metrics](http://localhost:5000/metrics)

---
---
## 📊 Accessing the Interfaces
Flask App: http://localhost:5000

Prometheus UI: http://localhost:9090

Grafana Dashboard: http://localhost:3000

🔐 Default Grafana credentials:

Username: admin

Password: admin
