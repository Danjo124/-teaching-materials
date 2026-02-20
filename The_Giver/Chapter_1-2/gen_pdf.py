import fpdf
import os

def create_pdf(markdown_file, output_pdf, title):
    pdf = fpdf.FPDF()
    pdf.set_margins(20, 20, 20)
    pdf.add_page()
    
    # Title
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(0, 10, title, ln=True, align='L')
    pdf.ln(5)
    
    # Content
    pdf.set_font("Helvetica", size=12)
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                pdf.ln(2)
                continue
            
            if line.startswith("# "):
                pdf.ln(5)
                pdf.set_font("Helvetica", 'B', 14)
                pdf.set_fill_color(240, 240, 240)
                pdf.cell(0, 10, line[2:], ln=True, fill=True)
                pdf.set_font("Helvetica", size=12)
                pdf.ln(2)
            elif line.startswith("## "):
                pdf.ln(3)
                pdf.set_font("Helvetica", 'B', 12)
                pdf.cell(0, 8, line[3:], ln=True)
                pdf.set_font("Helvetica", size=12)
            elif line.startswith("---"):
                pdf.line(pdf.get_x(), pdf.get_y(), pdf.get_x() + 170, pdf.get_y())
                pdf.ln(2)
            else:
                pdf.multi_cell(0, 7, line)
    
    pdf.output(output_pdf)

# Files
ws_md = "teaching-materials/The_Giver/Chapter_1-2/worksheet.md"
sol_md = "teaching-materials/The_Giver/Chapter_1-2/solutions.md"
output_pdf = "teaching-materials/The_Giver/Chapter_1-2/The_Giver_Ch1-2.pdf"

# Merge into one PDF with page break
pdf = fpdf.FPDF()
pdf.set_margins(20, 20, 20)

def add_content_to_pdf(pdf, markdown_file, title):
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(0, 10, title, ln=True, align='L')
    pdf.ln(5)
    pdf.set_font("Helvetica", size=12)
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                pdf.ln(2)
                continue
            if line.startswith("# "):
                pdf.ln(5)
                pdf.set_font("Helvetica", 'B', 14)
                pdf.set_fill_color(240, 240, 240)
                pdf.cell(0, 10, line[2:], ln=True, fill=True)
                pdf.set_font("Helvetica", size=12)
                pdf.ln(2)
            elif line.startswith("## "):
                pdf.ln(3)
                pdf.set_font("Helvetica", 'B', 12)
                pdf.cell(0, 8, line[3:], ln=True)
                pdf.set_font("Helvetica", size=12)
            elif line.startswith("---"):
                pdf.line(pdf.get_x(), pdf.get_y(), pdf.get_x() + 170, pdf.get_y())
                pdf.ln(2)
            else:
                pdf.multi_cell(0, 7, line)

add_content_to_pdf(pdf, ws_md, "The Giver - Worksheet (Ch. 1-2)")
add_content_to_pdf(pdf, sol_md, "The Giver - Solutions (Ch. 1-2)")
pdf.output(output_pdf)
print(f"PDF created: {output_pdf}")
