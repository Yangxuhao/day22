import PyPDF2
filepath=r"C:\Users\xuhao_yang\PycharmProjects\day22\2.pdf"
pdffile=open(filepath,"rb")
pdfreader=PyPDF2.PdfFileReader(pdffile)
print(pdfreader.numPages)
for i in range(pdfreader.numPages):
    page=pdfreader.getPage(i)
    print(page.extractText())