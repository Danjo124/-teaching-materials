from fpdf import FPDF
import os

class ExpertWorksheet(FPDF):
    def header(self):
        # Clean header with subject and teacher info
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(44, 62, 80)
        self.cell(0, 10, self.worksheet_title, ln=True, align='L')
        self.set_font('Helvetica', '', 10)
        self.set_text_color(127, 140, 141)
        self.cell(0, 5, 'Subject: English 5C | Teacher: Daniel', ln=True, align='L')
        self.ln(10)

    def section_header(self, title):
        self.ln(5)
        self.set_fill_color(236, 240, 241) # Light grey
        self.set_text_color(44, 62, 80)
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, f'  {title}', ln=True, fill=True)
        self.ln(4)

    def write_task(self, text):
        self.set_font('Helvetica', '', 11)
        self.set_text_color(52, 73, 94)
        self.multi_cell(0, 7, text)
        self.ln(1)

def generate_pdf(markdown_file, output_pdf, title):
    pdf = ExpertWorksheet()
    pdf.worksheet_title = title
    pdf.set_margins(20, 20, 20)
    pdf.set_auto_page_break(auto=True, margin=20)
    
    # Page 1: Worksheet
    pdf.add_page()
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = content.split("# SOLUTIONS")
    worksheet_content = parts[0]
    solutions_content = "# SOLUTIONS" + parts[1] if len(parts) > 1 else ""

    # Parse Worksheet
    for line in worksheet_content.split('\n'):
        line = line.strip().replace('\u2019', "'").replace('\u2013', "-").replace('\u2014', "--")
        if not line:
            continue
        if line.startswith("## "):
            pdf.section_header(line.replace("## ", ""))
        elif line.startswith("---"):
            pdf.ln(2)
            pdf.line(20, pdf.get_y(), 190, pdf.get_y())
            pdf.ln(5)
        else:
            pdf.write_task(line)

    # Page 2: SOLUTIONS
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 16)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(0, 10, f'Solutions: {title}', ln=True, align='L')
    pdf.ln(10)
    
    for line in solutions_content.split('\n'):
        line = line.strip().replace('\u2019', "'").replace('\u2013', "-").replace('\u2014', "--")
        if not line or line.startswith("#"):
            continue
        if line.startswith("## "):
            pdf.set_font('Helvetica', 'B', 12)
            pdf.ln(5)
            pdf.cell(0, 10, line.replace("## ", ""), ln=True)
            pdf.set_font('Helvetica', '', 11)
        else:
            pdf.set_font('Helvetica', '', 11)
            pdf.multi_cell(0, 7, line)

    pdf.output(output_pdf)

if __name__ == "__main__":
    generate_pdf("teaching-materials/The_Giver/Chapter_3-4/worksheet.md", 
                 "teaching-materials/The_Giver/Chapter_3-4/The_Giver_Ch3_4_Worksheet.pdf", 
                 "The Giver - Chapters 3 & 4")
