import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# -------- Step 1: Read the CSV File --------
data = pd.read_csv("data.csv")

# -------- Step 2: Analyze Data --------
average_score = data["Score"].mean()

# -------- Step 3: Generate PDF Report --------
def generate_pdf(dataframe, avg, filename="report.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 50, "Student Score Report")

    # Table Header
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, height - 100, "Name")
    c.drawString(300, height - 100, "Score")

    # Table Data
    c.setFont("Helvetica", 12)
    y = height - 130
    for index, row in dataframe.iterrows():
        c.drawString(100, y, str(row['Name']))
        c.drawString(300, y, str(row['Score']))
        y -= 20

    # Average
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y - 30, f"Average Score: {avg:.2f}")

    c.save()

# Call the function
generate_pdf(data, average_score)
print("PDF report generated as 'report.pdf'")
