import sys
import os
sys.path.append('/data/.openclaw/workspace')
from send_email_with_attachments import send_email

recipient = "tek@biondekgasse.at"
subject = "Arbeitsblätter: The Giver (Update) & Word Formation 7B"
body = """Hallo Daniel,

hier sind die überarbeiteten Unterlagen:

1. The Giver (Ch. 1 & 2): Jetzt deutlich anspruchsvoller mit 12 Lücken, 4 Analyse-Fragen, 1 Diskussionsfrage und ausführlichen Lösungen.
2. Word Formation (7B): Neues Arbeitsblatt für die 7B mit Fokus auf B2/C1 Niveau und ausführlichen Erklärungen in den Lösungen.

Der QR-Code für die 7B ist in Vorbereitung ( GitHub Pages Sync folgt).

Viele Grüße,
Digit ✍️"""

attachments = [
    "/data/.openclaw/workspace/teaching-materials/The_Giver/Chapter_1-2/The_Giver_Chapter_1.pdf",
    "/data/.openclaw/workspace/teaching-materials/The_Giver/Chapter_1-2/The_Giver_Chapter_2.pdf",
    "/data/.openclaw/workspace/teaching-materials/english/year-7/word-formation/Word_Formation_7B.pdf"
]

send_email(recipient, subject, body, attachments)
