filenames = ['1.Raw Data.txt', '2.Report.txt', '3.Presentation.txt']
for filename in filenames:
  filename = filename.replace('.','-',1 )# change immutable (string)
  filename = filename.replace('txt', 'py', 1)
  print(filename)
  
#tuple immutable list
