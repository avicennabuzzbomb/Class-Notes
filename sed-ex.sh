sed s/\(\"\)\([0-9]\)[,]\([0-9]\)/\(\)\([0-9]\)\([0-9]\)/g exercise-file1.txt > editedFile1.txt
#filename is "exercise-file1"

#check the number of commas in each line of the file
sed s/[,]\([0-9]\)[,]\([0-9]\)/[,]\([0-9]\)[,]\([0-9]\)/g editedFile1.txt > editedFile2.txt
