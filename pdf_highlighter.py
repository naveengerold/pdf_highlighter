import fitz
import re
from pathlib import Path

filepath = "//home/naveen/Desktop/PDF_highlighter/data/Unit5.pdf"
input_file = fitz.open(filepath)

# def pdftext():
for page in input_file:
    print(page)
    text_file = open("/home/naveen/Desktop/PDF_highlighter/data/data_words.txt", "r")
    data = text_file.read()
    text_file.close()
    text = data
    value = text.split()
    search_str = []
    for sub in value:
        search_str.append(re.sub('\n', '', sub))
    print(search_str)
    text_instances = [page.search_for(text) for text in search_str]
    # iterate through each instance for highlighting
    for inst in text_instances:
        annot = page.addHighlightAnnot(inst)
        # annot = page.add_rect_annot(inst)
        ## Adding comment to the highlighted text
        info = annot.info
        print(info)
        # info["title"] = "word_diffs"
        info["content"] = "new_ data"
        annot.set_info(info)
        annot.update()

# pdftext()
#Saving the PDF Output
filename = Path(filepath).stem
output = filename + "_highlighted.pdf"
input_file.save(output)
