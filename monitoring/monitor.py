from models.anomaly_detector import detect_anomalies

def run_monitoring():
    df = detect_anomalies()
    anomalies = df[df['anomaly'] == -1]
    print(f"⚠️ Detected {len(anomalies)} anomalies!")
