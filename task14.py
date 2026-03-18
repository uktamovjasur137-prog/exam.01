text = input("document: ")

if text.endswith(".pdf"):
    print("Fayl turi: pdf")

elif text.endswith(".docx"):
    print("Fayl turi: docx")

elif text.endswith(".txt"):
    print("Fayl turi: txt")

else:
    print("Xato")