from gtts import gTTS
import pdfplumber
from art import tprint
from pathlib import Path


def pdf_to_mp3(file_path="test.pdf", language="en"):
    if Path(file_path).is_file() and Path(file_path).suffix == ".pdf":
        print(f"[+] Original file: {Path(file_path).name}")
        print(f"[+] Work in progress...")
        with pdfplumber.PDF(open(file=file_path, mode="rb")) as f:
            pages = [page.extract_text() for page in f.pages]

        text = "".join(pages)
        text = text.replace("\n", "")

        mp3 = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        mp3.save(f"{file_name}.mp3")

        return f"[+] {file_name}.mp3 saved"
    else:
        return "File not exist!"


def main():
    tprint('PDF2MP3', font="verilate")
    file_path = input("\n Enter a file path: ")
    language = input("\n Enter a language: ")
    print((pdf_to_mp3(file_path=file_path, language=language)))


if __name__ == '__main__':
    main()
