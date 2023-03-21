file = open("student.txt","a")      #if use w to write file then it remove all files and create new files what i write
file.write("\nSonargaon University")
file.close()
file = open("student1.txt","w")         #to create a new file and write on it
file.write("Tonmoy")
file.close()