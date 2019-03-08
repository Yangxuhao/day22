import docx

def getText(path):
    doc=docx.Document(path)
    fulltext=[]
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return fulltext

path=r"C:\Users\xuhao_yang\PycharmProjects\day22\Python正则表达式七种兵器.docx"
data=getText(path)
print(data)