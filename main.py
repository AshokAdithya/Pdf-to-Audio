#PDF-AUDIO FORMAT
from gtts import gTTS
import PyPDF2

def text_to_speech(text, language='en', filename='C:/Users/Ashok Adithya/OneDrive - SSN Trust/phy/output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    print(f'Audiobook saved to {filename}')

if __name__ == "__main__":
    reader = PyPDF2.PdfReader('C:/Users/Ashok Adithya/OneDrive - SSN Trust/phy/hi.pdf')
    length=(len(reader.pages))
    text=''
    for page in range(length):
        text+=reader.pages[page].extract_text()
    text_to_speech(text)

