import csv
rows = []
maxMarks = ['0','0','0','0','0','0']
sub =['Maths','Biology','English','Chemistry','Physics','History']
subTop = ['','','','','','']
with open('Student_marks_list.csv','rt') as file:
  csv_rows = csv.reader(file)
  for row in csv_rows:
    rows.append(row)
  for i in range(1,len(rows)):
    for j in range(1,7):
      if rows[i][j] > maxMarks[j-1]:
        maxMarks[j-1] = rows[i][j]
        subTop[j-1] = rows[i][0]
  for i in range(0,6):
    print("Topper in " + sub[i] + " is " + subTop[i])
  maxTotal=[0,0,0]
  rank=['','','']
  for i in range(0,3):
    index = 0
    for j in range(1,len(rows)):
      sum = 0
      for k in range(1,7):
        sum += int(rows[j][k])
      if sum>maxTotal[i]:
        maxTotal[i] = sum
        rank[i] = rows[j][0]
        index = j
    rows.pop(index)
  print("Best Students in class are:")
  print(rank[0] + "-First Rank")
  print(rank[1] + "-Second Rank")
  print(rank[2] + "-Third Rank")
