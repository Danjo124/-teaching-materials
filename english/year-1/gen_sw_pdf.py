import fpdf
import os
import urllib.request
import urllib.parse

def create_signal_pdf(markdown_file, output_pdf, title, quiz_url):
    pdf = fpdf.FPDF()
    pdf.set_margins(20, 20, 20)
    pdf.add_page()
    
    # Header
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(130, 10, title, ln=0)
    
    # QR API
    qr_size = 30
    safe_url = urllib.parse.quote(quiz_url)
    api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={safe_url}"
    try:
        urllib.request.urlretrieve(api_url, "temp_qr_sw.png")
        pdf.image("temp_qr_sw.png", x=160, y=15, w=qr_size, h=qr_size)
        os.remove("temp_qr_sw.png")
    except:
        pdf.rect(160, 15, qr_size, qr_size)
    
    pdf.set_xy(160, 47)
    pdf.set_font("Helvetica", 'B', 6)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(qr_size, 3, "SCAN FOR INTERACTIVE QUIZ", ln=1, align='C')
    pdf.set_text_color(0, 0, 0)
    
    pdf.set_xy(20, 40)
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = content.split("# Solutions")
    ws_text = parts[0]
    sol_text = "# Solutions" + parts[1]

    pdf.set_font("Helvetica", size=11)
    for line in ws_text.split('\n'):
        line = line.strip().replace('\u2019', "'").replace('\u2013', "-")
        if not line: pdf.ln(2); continue
        if line.startswith("## "):
            pdf.ln(3); pdf.set_font("Helvetica", 'B', 12); pdf.set_fill_color(240, 240, 240)
            pdf.cell(0, 8, line[3:], ln=True, fill=True); pdf.set_font("Helvetica", size=11)
        elif line.startswith("---"):
            pdf.line(20, pdf.get_y(), 190, pdf.get_y()); pdf.ln(2)
        else:
            if "**" in line:
                for part in line.split("**"):
                    if line.find("**"+part+"**") != -1: pdf.set_font("Helvetica", 'B', 11)
                    else: pdf.set_font("Helvetica", size=11)
                    pdf.write(6, part)
                pdf.ln(6)
            else: pdf.multi_cell(0, 6, line)

    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 14); pdf.cell(0, 10, "Solutions", ln=True)
    pdf.set_font("Helvetica", size=11)
    for line in sol_text.split('\n'):
        pdf.multi_cell(0, 6, line.strip())

    pdf.output(output_pdf)

url = "https://danjo124.github.io/-teaching-materials/english/year-1/signal_words_quiz.html"
create_signal_pdf("teaching-materials/english/year-1/signal_words_practice.md", "teaching-materials/english/year-1/Signal_Words_Worksheet.pdf", "Simple Present: Signal Words", url)
