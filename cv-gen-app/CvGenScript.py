from docxtpl import DocxTemplate

# create a doc

skills_and_experiences = [
    {
        "name": "skill1",
        "tasks": ["Lorem ipsum dolor sit amet","Lorem ipsum dolor sit amet",
            "Lorem ipsum dolor sit amet"],
    },
    {
        "name": "skill2",
        "tasks": ["Lorem ipsum dolor sit amet","Lorem ipsum dolor sit amet",
            "Lorem ipsum dolor sit amet"],
    },
    {
        "name": "skill3",
        "tasks": ["Lorem ipsum dolor sit amet","Lorem ipsum dolor sit amet",
            "Lorem ipsum dolor sit amet"],
    },
]

employments = [
    {
        "title":"Prophet",
        "period": "580-600",
        "company":"quraish",
        "city":"mecca",
        "location":"medina",
    },
    {
        "title": "depression",
        "period" :"0000-2023",
        "company":"asad",
        "city":"earth",
        "location":"bruh"
    }
    
]

education_history = [
    {
        "degree":"M.Sc computer science engineering",
        "date":"2022",
        "university": "institut superieur de zatla sud grombalia",
        "country":"tunis",
    },
    {
        "degree":"baccalaureat science experimental",
        "date":"2021",
        "university":"7abit nemshi medecien hhhhhhhhh",
        "country":"jandouba",
    }
    
]

doc = DocxTemplate("Resume_Sample_Functional.docx")

# create context dictionary
context = {
    "name": " Mohamad Al bo3bo3 ",
    "address": "janah",
    "phoneNumber": "69 696 969",
    "email": "sol3om@gmail.com",
    "high_qualifications": ["text1","text2","text3"],
    "skills_and_experiences": skills_and_experiences,
    "employments": employments,
    "education_history": education_history,
}

# render context into the document object
doc.render(context)

# save the document object as a word file
doc.save('cv-docx.docx')rom docxtpl import DocxTemplate

# create a doc

skills_and_experiences = [
    {
        "name": "skill1",
        "tasks": ["Lorem ipsum dolor sit amet","Lorem ipsum dolor sit amet",
            "Lorem ipsum dolor sit amet"],
    },
    {
        "name": "skill2",
        "tasks": ["Lorem ipsum dolor sit amet","Lorem ipsum dolor sit amet",
            "Lorem ipsum dolor sit amet"],
    },
    {
        "name": "skill3",
        "tasks": ["Lorem ipsum dolor sit amet","Lorem ipsum dolor sit amet",
            "Lorem ipsum dolor sit amet"],
    },
]

employments = [
    {
        "title":"Prophet",
        "period": "580-600",
        "company":"quraish",
        "city":"mecca",
        "location":"medina",
    },
    {
        "title": "depression",
        "period" :"0000-2023",
        "company":"asad",
        "city":"earth",
        "location":"bruh"
    }
    
]

education_history = [
    {
        "degree":"M.Sc computer science engineering",
        "date":"2022",
        "university": "institut superieur de zatla sud grombalia",
        "country":"tunis",
    },
    {
        "degree":"baccalaureat science experimental",
        "date":"2021",
        "university":"7abit nemshi medecien hhhhhhhhh",
        "country":"jandouba",
    }
    
]

doc = DocxTemplate("Resume_Sample_Functional.docx")

# create context dictionary
context = {
    "name": " Mohamad Al bo3bo3 ",
    "address": "janah",
    "phoneNumber": "69 696 969",
    "email": "sol3om@gmail.com",
    "high_qualifications": ["text1","text2","text3"],
    "skills_and_experiences": skills_and_experiences,
    "employments": employments,
    "education_history": education_history,
}

# render context into the document object
doc.render(context)

# save the document object as a word file
doc.save('cv-docx.docx')
