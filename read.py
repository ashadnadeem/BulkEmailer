__author__ = "Ashad Nadeem Mahmudi"
__date__ = "9/23/2020"

# Reading existing CSV File
import csv

def Data(file_name):
    people = []
    with open(file_name) as file:
        csv_f = csv.reader(file)
        for row in csv_f:
            name, email = row
            person = {"name": name, "email": email}
            people.append(person)
    return people

def getBody(file_name):
    with open(file_name) as file:
        lines = file.readlines()
    updatedlines = []
    for line in lines:
        updatedlines.append(line.strip())
    body = "\n".join(updatedlines)
    return body