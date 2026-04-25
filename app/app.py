from flask import Flask, jsonify, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import random
import time

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "demo_api_requests_total",
    "Total HTTP requests handled by ktrail-api",
    ["endpoint", "method", "status"]
)

REQUEST_LATENCY = Histogram(
    "demo_api_request_latency_seconds",
    "Request latency in seconds",
    ["endpoint"]
)

@app.route("/")
def home():
    start = time.time()
    time.sleep(random.uniform(0.01, 0.15))
    REQUEST_COUNT.labels(endpoint="/", method="GET", status="200").inc()
    REQUEST_LATENCY.labels(endpoint="/").observe(time.time() - start)
    return jsonify({
        "service": "ktrail-api",
        "status": "ok",
        "message": "GitOps demo running on Kubernetes"
    })

@app.route("/healthz")
def healthz():
    REQUEST_COUNT.labels(endpoint="/healthz", method="GET", status="200").inc()
    return jsonify({"status": "healthy"})

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
