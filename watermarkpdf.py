import PyPDF2
import sys
templateloc = sys.argv[1]
watermarkloc = sys.argv[2]
template = PyPDF2.PdfFileReader(open(templateloc,'rb'))
watermark = PyPDF2.PdfFileReader(open(watermarkloc,'rb'))
output = PyPDF2.PdfFileWriter()
for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_out.pdf','wb') as file:
        output.write(file)