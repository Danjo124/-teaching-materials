import fpdf
import os

# Define a function to draw a mock QR code grid
def draw_mock_qr(pdf, x, y, size, url):
    # Draw outer box
    pdf.set_line_width(0.5)
    pdf.rect(x, y, size, size)
    
    # Draw the three typical QR position detection patterns (squares in corners)
    box_s = size / 5
    # Top-left
    pdf.rect(x + 1, y + 1, box_s, box_s, 'F')
    # Top-right
    pdf.rect(x + size - box_s - 1, y + 1, box_s, box_s, 'F')
    # Bottom-left
    pdf.rect(x + 1, y + size - box_s - 1, box_s, box_s, 'F')
    
    # Add some random "bits" for visual representation
    import random
    random.seed(url) # Consistent pattern for same URL
    dot_s = size / 10
    for i in range(10):
        for j in range(10):
            if (i < 3 and j < 3) or (i > 6 and j < 3) or (i < 3 and j > 6):
                continue # Skip corner boxes
            if random.random() > 0.5:
                pdf.rect(x + i*dot_s, y + j*dot_s, dot_s, dot_s, 'F')

def create_advanced_pdf_with_qr(markdown_file, output_pdf, title, full_url):
    pdf = fpdf.FPDF()
    pdf.set_margins(20, 20, 20)
    
    pdf.add_page()
    
    # Title
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(130, 10, title, ln=0, align='L')
    
    # Real QR Mockup (Visual placeholder with full URL text)
    qr_x, qr_y, qr_size = 160, 15, 30
    draw_mock_qr(pdf, qr_x, qr_y, qr_size, full_url)
    
    pdf.set_xy(160, 47)
    pdf.set_font("Helvetica", '', 6)
    # Truncate or wrap long URLs if necessary
    pdf.multi_cell(30, 3, full_url, align='C')
    
    pdf.set_xy(20, 35)
    pdf.ln(15)
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = content.split("# Solutions")
    worksheet_text = parts[0]
    solutions_text = "# Solutions" + parts[1] if len(parts) > 1 else ""

    pdf.set_font("Helvetica", size=11)
    for line in worksheet_text.split('\n'):
        line = line.strip().replace('\u2019', "'").replace('\u2013', "-").replace('\u201c', '"').replace('\u201d', '"').replace('\u2014', "--")
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
            if "**" in line:
                parts_b = line.split("**")
                for i, p in enumerate(parts_b):
                    if i % 2 == 1:
                        pdf.set_font("Helvetica", 'B', 11)
                        pdf.write(6, p)
                        pdf.set_font("Helvetica", size=11)
                    else:
                        pdf.write(6, p)
                pdf.ln(6)
            else:
                pdf.multi_cell(0, 6, line)

    # Solutions page
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, "Detailed Solutions - " + title, ln=True)
    pdf.ln(5)
    pdf.set_font("Helvetica", size=11)
    for line in solutions_text.split('\n'):
        line = line.strip().replace('\u2019', "'").replace('\u2013', "-").replace('\u201c', '"').replace('\u201d', '"').replace('\u2014', "--")
        if not line: pdf.ln(2); continue
        if line.startswith("#"):
            pdf.set_font("Helvetica", 'B', 12)
            pdf.multi_cell(0, 7, line)
            pdf.set_font("Helvetica", size=11)
        else:
            pdf.multi_cell(0, 6, line)

    pdf.output(output_pdf)

# Base URL for GitHub Pages
base_url = "https://danjo124.github.io/-teaching-materials/"

# Giver Ch 1
create_advanced_pdf_with_qr("teaching-materials/The_Giver/Chapter_1-2/ch1_worksheet.md", 
                            "teaching-materials/The_Giver/Chapter_1-2/The_Giver_Chapter_1.pdf", 
                            "The Giver - Chapter 1", base_url + "The_Giver/Chapter_1-2/index.html")

# Giver Ch 2
create_advanced_pdf_with_qr("teaching-materials/The_Giver/Chapter_1-2/ch2_worksheet.md", 
                            "teaching-materials/The_Giver/Chapter_1-2/The_Giver_Chapter_2.pdf", 
                            "The Giver - Chapter 2", base_url + "The_Giver/Chapter_1-2/index.html")

# 7B Word Formation
create_advanced_pdf_with_qr("teaching-materials/english/year-7/word-formation/worksheet.md", 
                            "teaching-materials/english/year-7/word-formation/Word_Formation_7B.pdf", 
                            "Word Formation - Grade 7B", base_url + "english/year-7/word-formation/index.html")

# Unit 8
create_advanced_pdf_with_qr("teaching-materials/english/year-1/unit8_clothes_advanced.md", 
                            "teaching-materials/english/year-1/Unit8_Clothes_Advanced.pdf", 
                            "Unit 8: Clothes & Shopping", base_url + "english/year-1/unit8_clothes_advanced.html")
