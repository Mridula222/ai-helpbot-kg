from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("data_ingestion/docs/sample.pdf", pagesize=letter)
c.drawString(100, 750, "Sample PDF Document")
c.drawString(100, 730, "This is a test page for parsing.")
c.save()
