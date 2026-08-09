from prometheus_client import Counter, Gauge, Histogram

request_counter = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "http_status"]
)

request_duration = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration in seconds",
    ["method", "endpoint"]
)

active_streams = Gauge(
    "active_streams",
    "Number of active streams"
)
