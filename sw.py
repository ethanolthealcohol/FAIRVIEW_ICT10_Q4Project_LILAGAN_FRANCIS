from pyscript import document, display

class Classmate:
    def __init__(self, name, section, subject):  #reads the categories of each classmate
        self.name=name
        self.section=section
        self.subject=subject
    
    def introduce(self):
        return "Hi! I am " + self.name + " from " + self.section + ". My favorite subject is " + self.subject + "." #This is the sentence that introduces a clasmate.

c1= Classmate("Judah", "Ruby", "Math")
c2= Classmate("Jazmar", "Sapphire", "English")
c3= Classmate("Fateh", "Emerald", "Social Studies")
c4= Classmate("Hendrich", "Ruby", "Math")
c5= Classmate("Miko", "Emerald", "PE")

classmates = [c1, c2, c3, c4, c5]  #list of classmates


def add(event):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    c = Classmate("Ethan", "Ruby", "Math")
    
    
    classmates.append(c)

    document.getElementById("output").innerHTML = "Classmate added!"  #recites "Classmate added!" when it successfully adds a classmates.


def show(event):
    text = ""

    for c in classmates:
        text += c.introduce() + "<br>"   #Introduces or sends a text

    document.getElementById("output").innerHTML = text