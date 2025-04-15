# Network Traffic Analyzer

A web app to monitor network traffic and spot threats like DDoS attacks. Built with Python, Flask, and a lightweight ML model

## How It Works
- Captures packets using Scapy
- Analyzes packet sizes with a RandomForest model
- Shows a dashboard with status and risk score

## Setup
1. Install Python 3.8+
2. Run `pip install -r requirements.txt`
3. Start with `python app.py`
4. Visit http://localhost:5000

## Use Case
Gives admins a simple way to check network health without heavy tools. Useful for small networks needing quick threat detection

## Future Improvements
- Add real-time updates to the dashboard
- Include more packet features for better predictions

Contact: kswierczynska21@gmail.com