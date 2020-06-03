import os
import csv

# initiates important variables
data_path = os.path.join(".", "Resources", "employee_data.csv")
emp_id = []
fname = []
lname = []
DOB = []
SSN = []
state = []

# defines a dictionary of state names and abbreviations.
state_dict = {"Alabama":"AL","Alaska":"AK","Arizona":"AZ","Arkansas":"AR","California":"CA","Colorado":"CO","Connecticut":"CT","Delaware":"DE","Florida":"FL","Georgia":"GA","Hawaii":"HI","Idaho":"ID","Illinois":"IL","Indiana":"IN","Iowa":"IA","Kansas":"KS","Kentucky":"KY","Louisiana":"LA","Maine":"ME","Maryland":"MD","Massachusetts":"MA","Michigan":"MI","Minnesota":"MN","Mississippi":"MS","Missouri":"MO","Montana":"MT","Nebraska":"NE","Nevada":"NV","New Hampshire":"NH","New Jersey":"NJ","New Mexico":"NM","New York":"NY","North Carolina":"NC","North Dakota":"ND","Ohio":"OH","Oklahoma":"OK","Oregon":"OR","Pennsylvania":"PA","Rhode Island":"RI","South Carolina":"SC","South Dakota":"SD","Tennessee":"TN","Texas":"TX","Utah":"UT","Vermont":"VT","Virginia":"VA","Washington":"WA","West Virginia":"WV","Wisconsin":"WI","Wyoming":"WY"}

# opens data file, extracts data, transforms into new formats, and creates lists for each field
with open(data_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    
    for row in csv_reader:
        emp_id.append(row[0])

        name = row[1]
        fname.append(name.split()[0])
        lname.append(name.split()[1])

        raw_dob = (row[2]) # YYYY-MM-DD
        dob = raw_dob.split('-')
        DOB.append(f"{dob[1]}/{dob[2]}/{dob[0]}")

        raw_ssn = row[3]
        ssn = raw_ssn.split('-')
        SSN.append(f"***-**-{ssn[2]}")
        
        state.append(state_dict[row[4]])


# resets results file and adds new header
write_path = os.path.join(".","analysis","clean_data.csv")
file_reset = open(write_path,"w") 
file_reset.write("EmployeeID,FirstName,LastName,DateOfBirth,SSN,State\n")
file_reset.close()

# writes new records from newly formatted lists to results file
with open(write_path,"a") as writer_file:
    for i in range(len(emp_id)):
        writer_file.write(f"{emp_id[i]},{fname[i]},{lname[i]},{DOB[i]},{SSN[i]},{state[i]}\n")