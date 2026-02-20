from fpdf import FPDF
import os

class CleanWorksheet(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, self.worksheet_title, ln=True, align='L')
        self.ln(10)

    def section_header(self, title):
        self.ln(5)
        self.set_fill_color(240, 240, 240)
        self.set_text_color(0, 0, 0)
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, f' {title}', ln=True, fill=True)
        self.ln(4)

    def task_line(self, text):
        self.set_font('Helvetica', '', 11)
        self.set_text_color(0, 0, 0)
        # Linksbündig schreiben
        self.multi_cell(0, 7, text, align='L')
        self.ln(1)

    def draw_lines(self, count=1):
        self.set_draw_color(200, 200, 200)
        for _ in range(count):
            self.ln(6)
            self.line(self.get_x(), self.get_y(), self.get_x() + 170, self.get_y())
        self.ln(4)

def generate_fixed_pdf():
    pdf = CleanWorksheet()
    pdf.worksheet_title = "The Giver - Chapters 3 & 4"
    pdf.set_margins(20, 20, 20)
    pdf.add_page()

    # I. Vocabulary
    pdf.section_header("I. Vocabulary: Contextual Understanding")
    pdf.set_font('Helvetica', 'I', 10)
    pdf.cell(0, 7, "Explain the following terms in the context of the community.", ln=True)
    pdf.ln(2)
    
    words = [
        "1. Remorse (n.):",
        "2. Chortle (v.):",
        "3. Gravitate (v.):",
        "4. Serene (adj.):",
        "5. Infraction (n.):"
    ]
    for word in words:
        pdf.set_font('Helvetica', 'B', 11)
        pdf.cell(0, 7, word, ln=True)
        pdf.draw_lines(1)

    # II. Analysis
    pdf.section_header("II. Analysis: The Apple & The Gaze")
    pdf.task_line("1. Describe the 'change' Jonas noticed in the apple. Why was he so confused by it?")
    pdf.draw_lines(2)
    pdf.task_line("2. Why are 'pale eyes' considered unusual? What does this suggest about the 'Sameness'?")
    pdf.draw_lines(2)

    # III. House of the Old
    pdf.section_header("III. Social Structures: The House of the Old")
    pdf.task_line("1. Explain the ritual of 'bathing the elderly.' What does it reveal about their society?")
    pdf.draw_lines(2)
    pdf.task_line("2. Compare the 'Release of a Newchild' with the 'Release of the Elderly.'")
    pdf.draw_lines(2)

    # IV. Discussion
    pdf.section_header("IV. Discussion & Critical Reflection")
    pdf.task_line("1. Predictability vs. Freedom: Would you prefer a life where your future is planned by 'Elders', or a life with freedom to fail?")
    pdf.draw_lines(2)
    pdf.task_line("2. The Nature of Guilt: Does the public apology for every 'infraction' truly help or is it a tool for control?")
    pdf.draw_lines(2)

    # SOLUTIONS PAGE
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 10, "Solutions: Chapters 3 & 4", ln=True)
    pdf.ln(5)
    
    pdf.set_font('Helvetica', '', 11)
    solutions = [
        "I. Vocabulary: 1. Deep regret, 2. Gleeful laugh, 3. To move toward, 4. Calm, 5. Rule violation.",
        "II. Analysis: 1. Color flicker; Jonas only knows grey. 2. Genetic variety vs. total conformity.",
        "III. House of the Old: 1. Care but isolation. 2. Tragedy vs. Celebration; both mysterious.",
        "IV. Discussion: Individual answers."
    ]
    for sol in solutions:
        pdf.multi_cell(0, 7, sol)
        pdf.ln(2)

    pdf.output("The_Giver_Ch3_4_Fixed.pdf")

if __name__ == "__main__":
    generate_fixed_pdf()
