import fpdf
import os

def create_single_page_pdf(markdown_file, output_pdf, title):
    pdf = fpdf.FPDF()
    pdf.set_margins(20, 20, 20)
    pdf.add_page()
    
    # Title
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(0, 10, title, ln=True, align='L')
    pdf.ln(5)
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content into Worksheet and Solutions
    parts = content.split("# Solutions")
    worksheet_text = parts[0]
    solutions_text = "# Solutions" + parts[1] if len(parts) > 1 else ""

    # Write Worksheet
    pdf.set_font("Helvetica", size=11)
    for line in worksheet_text.split('\n'):
        line = line.strip().replace('\u2019', "'").replace('\u2013', "-").replace('\u201c', '"').replace('\u201d', '"')
        if not line:
            pdf.ln(2)
            continue
        if line.startswith("## "):
            pdf.ln(3)
            pdf.set_font("Helvetica", 'B', 12)
            pdf.set_fill_color(240, 240, 240)
            pdf.cell(0, 8, line[3:], ln=True, fill=True)
            pdf.set_font("Helvetica", size=11)
        elif line.startswith("---"):
            pdf.line(pdf.get_x(), pdf.get_y(), pdf.get_x() + 170, pdf.get_y())
            pdf.ln(2)
        else:
            # Handle Bold Text in Lückentext / Markdown
            if "**" in line:
                parts = line.split("**")
                for i, part in enumerate(parts):
                    if i % 2 == 1: # Bold part
                        pdf.set_font("Helvetica", 'B', 11)
                        pdf.write(6, part)
                        pdf.set_font("Helvetica", size=11)
                    else:
                        pdf.write(6, part)
                pdf.ln(6)
            else:
                pdf.multi_cell(0, 6, line)

    # Solutions on a second page
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, "Solutions - " + title, ln=True)
    pdf.set_font("Helvetica", size=11)
    for line in solutions_text.split('\n'):
        line = line.strip().replace('\u2019', "'").replace('\u2013', "-").replace('\u201c', '"').replace('\u201d', '"')
        if not line: pdf.ln(2); continue
        pdf.multi_cell(0, 6, line)

    pdf.output(output_pdf)

create_single_page_pdf("teaching-materials/The_Giver/Chapter_1-2/ch1_worksheet.md", 
                       "teaching-materials/The_Giver/Chapter_1-2/The_Giver_Chapter_1.pdf", 
                       "The Giver - Chapter 1")

create_single_page_pdf("teaching-materials/The_Giver/Chapter_1-2/ch2_worksheet.md", 
                       "teaching-materials/The_Giver/Chapter_1-2/The_Giver_Chapter_2.pdf", 
                       "The Giver - Chapter 2")
