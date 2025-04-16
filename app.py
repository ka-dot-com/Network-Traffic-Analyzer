from flask import Flask, render_template, Response
from scapy.all import sniff
import threading
import time

app = Flask(__name__)
packet_data = []

def capture_packets():
    global packet_data
    while True:
        packets = sniff(count=10, timeout=5)
        packet_data = [{"size": len(pkt), "summary": str(pkt.summary())} for pkt in packets]
        time.sleep(5)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

def generate_data():
    global packet_data
    while True:
        yield f"data: {packet_data}\n\n"
        time.sleep(5)

@app.route("/data")
def data_stream():
    return Response(generate_data(), content_type="text/event-stream")

if __name__ == "__main__":
    threading.Thread(target=capture_packets, daemon=True).start()
    app.run(debug=True, host="0.0.0.0", port=5000)
