import PyPDF2
import sys

pdf_input = sys.argv[1]
watermark_input = sys.argv[2]

pdf_template = PyPDF2.PdfFileReader(open(pdf_input, 'rb'))
pdf_watermark = PyPDF2.PdfFileReader(open(watermark_input, 'rb'))
pdf_output = PyPDF2.PdfFileWriter()

def put_watermark(template, watermark, output):
    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open('watermarked_output.pdf', 'wb') as file:
            output.write(file)

put_watermark(pdf_template, pdf_watermark, pdf_output)