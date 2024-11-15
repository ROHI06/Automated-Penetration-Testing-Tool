from fpdf import FPDF

def generate_pdf_report(scan_results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Penetration Test Report", 0, 1, "C")

    for tool, result in scan_results.items():
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, f"{tool.upper()} Results:", 0, 1)
        pdf.set_font("Arial", "", 10)
        pdf.multi_cell(0, 10, str(result))
        pdf.ln(5)

    report_path = "reports/report.pdf"
    pdf.output(report_path)
    return report_path