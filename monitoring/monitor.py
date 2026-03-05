"""Run anomaly monitoring and write reports to output/."""
from config.paths import OUTPUT_DIR
from models.anomaly_detector import detect_anomalies


def run_monitoring():
    """Run anomaly detection and write anomaly report to output/."""
    df = detect_anomalies()
    anomalies = df[df["anomaly"] == -1]
    print(f"⚠️ Detected {len(anomalies)} anomalies!")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = OUTPUT_DIR / "anomaly_report.csv"
    anomalies.to_csv(report_path, index=False)
    print(f"✅ Report saved to {report_path}")
