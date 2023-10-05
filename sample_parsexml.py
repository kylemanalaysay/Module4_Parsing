import xml.etree.cElementTree as et
# Kyle Andrei M. Manalaysay
tree = et.parse("sample.xml")
root = tree.getroot()
Job_Title = []
Company_Name = []
Category = []
City = []

for title in root.iter('job_title'):
    Job_Title.append(title.text)

for company in root.iter('company_name'):
    Company_Name.append(company.text)

for cat in root.iter('category'):
    Category.append(cat.text)

for ct in root.iter('city'):
    City.append(ct.text)   

print(Job_Title)
print("============================================")
print(Company_Name)
print("============================================")
print(Category)
print("============================================")
print(City)