import markdown
import pdfkit
from pathlib import Path

# קבצים
md_path = Path("example.md")
html_path = Path("temp.html")
pdf_path = Path("output.pdf")

#  קריאת markdown
md_text = md_path.read_text(encoding="utf-8")

#  המרה ל-HTML
html = markdown.markdown(md_text)

#  שמירת HTML זמני
html_path.write_text(html, encoding="utf-8")

#  נתיב ל-wkhtmltopdf (אם צריך)
config = pdfkit.configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
)

#  המרה ל-PDF
pdfkit.from_file(str(html_path), str(pdf_path), configuration=config)

print("PDF created successfully!")
