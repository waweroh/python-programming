feet_inches = input('enter feet and inches: ')

def convert (feet_inches):
  part = feet_inches.split(' ')
  feet = float(part[0])
  inches = float(part[1]) 

  meters = feet * 0.3048 + inches * 0.0254
  return meters

result = (convert(feet_inches))
print(result)

if result < 1:
  print('kid is too small')
else:
  print('kid can use the slide')
