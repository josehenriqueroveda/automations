import PyPDF2
import sys

# grab N .pdfs passed as args to merge them
inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('merged.pdf')

pdf_combiner(inputs)