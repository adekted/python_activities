import os
import csv

csvpath = os.path.join('.',"employees.csv")
output = os.path.join(".","output.csv")
email_lst = []

with open(csvpath, newline = '') as csvfile:
    dictreader = csv.DictReader(csvfile, delimiter = ",")
    for row in dictreader:
        
        email = row["First Name"].lower() + "." + row["Last Name"].lower() +"@example.com"
        # email = f"{first_name}.{last_name}@example.com"
        
        row["Email"] = email
        # email_lst.append({first_name:first_name, last_name:last_name, ssn:row[ssn], email:email})

        email_lst.append(row)

with open(output,'w') as datafile:
    fieldnames = ["First Name","Last Name","SSN","Email"]

    writer = csv.DictWriter(datafile,fieldnames=fieldnames)
    # writer.writerow(["First Name","Last Name","SSN","Email"])
    writer.writeheader()
    for i in email_lst:
        writer.writerow(i)