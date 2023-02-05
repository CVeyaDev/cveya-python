from docxtpl import DocxTemplate
from docx2pdf import convert

# create a document object
doc = DocxTemplate("Resume_Sample_Functional.docx")

# create context dictionary
context = {
    "name": " Mohamad Al bo3bo3 ",
    "address": "janah",
    "phoneNumber": "69 696 969",
    "email": "sol3om@gmail.com",
}

# render context into the document object
doc.render(context)

# save the document object as a word file
doc.save('cv-docx.docx')
convert("cv-docx.docx", "cv-pdf.pdf")

