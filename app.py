from flask import Flask, render_template
from scapy.all import sniff
import numpy as np
from model import load_predictor

app = Flask(__name__)
predictor = load_predictor("network_model.pkl")

def capture_packets():
    try:
        packets = sniff(count=50, timeout=10)
        sizes = [len(pkt) for pkt in packets]
        return np.array(sizes).reshape(1, -1)
    except Exception as e:
        print(f"Error capturing packets: {e}")
        return np.zeros((1, 50))

@app.route("/")
def dashboard():
    packet_data = capture_packets()
    risk_score = predictor.predict(packet_data)[0]
    status = "Network Stable" if risk_score < 0.5 else "Possible Threat!"
    return render_template("dashboard.html", status=status, score=round(risk_score, 2))

if __name__ == "__main__":
    print("Starting Network Traffic Analyzer on http://localhost:5000")
    app.run(debug=False, host="0.0.0.0", port=5000)
