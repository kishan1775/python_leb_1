subjects = ["java","python","j2ee","cs","c++"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter the mark for {subject} "))
    marks.append(mark)
    
total =sum(marks)
average = total/len(subjects)

if average >=90:
    grade = 'A'
elif average >=70:
    grade = 'B'
elif average >=60:
    grade = 'C'
elif average >=40:
    grade = 'D'
else:
    grade= 'Fail'
    
print("total marks:",total)
print("average marks:",average)
print("grade:",grade)


