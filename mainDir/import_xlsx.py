import openpyxl

book = openpyxl.open("../media/template_students.xlsx")

sheet = book.active

print(sheet[2][0].value)

for row in range(2, sheet.max_row+1):
    surname = sheet[row][0].value
    name = sheet[row][1].value
    patronymic = sheet[row][2].value
    birthday = sheet[row][3].value

    print(surname, name, patronymic, birthday)
