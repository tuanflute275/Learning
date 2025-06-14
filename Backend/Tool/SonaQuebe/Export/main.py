import requests
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

# Lấy dữ liệu lỗi từ SonarQube API
response = requests.get(
    "http://localhost:9000/api/issues/search?componentKeys=BE-khodulieumo",
    auth=("squ_469b7c0afede22a1e87e08f5b4d05e32e2a9ac12", "")
)

# Phân tích dữ liệu JSON
issues = response.json()['issues']

# Tạo PDF
pdf_filename = "sonarqube_report_professional.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
story = []

# Lấy các kiểu văn bản có sẵn từ thư viện reportlab
styles = getSampleStyleSheet()

# Tiêu đề
title = Paragraph("SonarQube Issues Report", styles['Title'])
story.append(title)

# Tạo một đoạn văn giới thiệu tổng quan
overview = Paragraph("This is a detailed report of SonarQube issues for the project 'BE-khodulieumo'. "
                     "It lists issues based on their severity levels and provides a summary of each issue.", styles['Normal'])
story.append(overview)

# Thêm thông tin tóm tắt về số lượng lỗi
high_issues = len([issue for issue in issues if issue['severity'] == 'CRITICAL'])
medium_issues = len([issue for issue in issues if issue['severity'] == 'MAJOR'])
low_issues = len([issue for issue in issues if issue['severity'] == 'MINOR'])

summary = Paragraph(f"Summary: {high_issues} Critical Issues, {medium_issues} Major Issues, {low_issues} Minor Issues.", styles['Normal'])
story.append(summary)

# Tạo bảng để hiển thị các lỗi
data = [["#", "Key", "Message", "Severity", "File/Path"]]  # Header for the table

# Thêm lỗi vào bảng, phân loại mức độ nghiêm trọng (Severity)
for index, issue in enumerate(issues, start=1):
    key = issue['key']
    message = issue['message']
    severity = issue['severity']
    file_path = issue.get('component', 'N/A')  # Đường dẫn file (component)
    data.append([index, key, message, severity, file_path])

# Tạo bảng với dữ liệu lỗi
table = Table(data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background color
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold header
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Grid lines
    ('FONTSIZE', (0, 0), (-1, -1), 10),  # Font size for all cells
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Background color for rows
    ('ALIGN', (1, 1), (-1, -1), 'LEFT'),  # Left align all columns except first column
    ('ALIGN', (0, 1), (0, -1), 'CENTER'),  # Center align first column (Index)
]))

story.append(table)

# Tạo một kết luận
conclusion = Paragraph("The report details all the issues found in the 'BE-khodulieumo' project. "
                       "Please address the high severity issues first to ensure the project's quality and security.", styles['Normal'])
story.append(conclusion)

# Tạo PDF
doc.build(story)

print("Professional PDF Report generated successfully!")
