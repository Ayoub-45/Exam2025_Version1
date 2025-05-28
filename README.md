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

Make sure you have installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 📁 Project Structure
├── app.py # Flask application
├── Dockerfile # Dockerfile for Flask app
├── requirements.txt # Python dependencies
├── prometheus/prometheus.yaml # Prometheus config file
├── docker-compose.yml # Multi-container config
├── templates/ # HTML templates
└── README.md
## 🧪 Metrics Exposed

- `views_by_product{product="Apple"}` – Number of views per product
- `sales_duration_seconds` – Histogram measuring time spent processing sales

Metrics are available at:  
http://localhost:5000/metrics

---

## 🚀 Getting Started
### 1. fork your own copy
### 2. Clone the repository
```bash
git clone https://github.com/your-username/Exam2025_Version1.git
```
```bash
cd Exam2025_version1
```bash
docker-compose up --build
### 3. enjoy
```
