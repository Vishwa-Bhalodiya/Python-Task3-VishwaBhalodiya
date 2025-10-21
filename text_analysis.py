import os
import re

def analyze_text(file_path):
    
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()


    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    paragraph_count = len(paragraphs)


    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(sentences)

  
    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)

   
    file_size = os.path.getsize(file_path)  
    file_size_kb = round(file_size / 1024, 2)


    print("📘 Text Analysis Report")
    print(f"Paragraphs: {paragraph_count}")
    print(f"Sentences: {sentence_count}")
    print(f"Words: {word_count}")
    print(f"File Size: {file_size_kb} KB")

    return {
        "paragraphs": paragraph_count,
        "sentences": sentence_count,
        "words": word_count,
        "file_size_kb": file_size_kb
    }


if __name__ == "__main__":
    file_path = "sample.txt" 
    analyze_text(file_path)
