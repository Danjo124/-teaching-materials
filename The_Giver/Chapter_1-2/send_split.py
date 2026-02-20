import sys
import os
sys.path.append('/data/.openclaw/workspace')
from send_email_with_attachments import send_email

recipient = "tek@biondekgasse.at"
subject = "Arbeitsblätter: The Giver - Chapters 1 & 2 (getrennt)"
body = """Hallo Daniel,

hier sind die überarbeiteten Arbeitsblätter zu 'The Giver' (Kapitel 1 und 2 getrennt, jeweils eine Seite + Lösungen).

Diese wurden auch auf GitHub aktualisiert.

Viele Grüße,
Digit ✍️"""

attachments = [
    "/data/.openclaw/workspace/teaching-materials/The_Giver/Chapter_1-2/The_Giver_Chapter_1.pdf",
    "/data/.openclaw/workspace/teaching-materials/The_Giver/Chapter_1-2/The_Giver_Chapter_2.pdf"
]

send_email(recipient, subject, body, attachments)
