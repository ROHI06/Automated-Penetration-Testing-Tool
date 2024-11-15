from flask import Flask, jsonify, request, send_file
from scanners.nmap_scanner import scan_network
from scanners.zap_scanner import zap_scan
from report_generator import generate_pdf_report

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    target = request.json.get('target')
    nmap_result = scan_network(target)
    zap_result = zap_scan(target)

    # Aggregate results
    scan_results = {
        'nmap': nmap_result,
        'zap': zap_result,
    }

    # Generate PDF report
    report_path = generate_pdf_report(scan_results)
    return jsonify({'results': scan_results, 'report_path': report_path})

@app.route('/download_report', methods=['GET'])
def download_report():
    return send_file("reports/report.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)