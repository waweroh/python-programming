feet_inches = input('enter feet and inches: ')

def parse(feet_inches):
  part = feet_inches.split(' ')
  feet = float (part[0])
  inches = float (part[1])
  return {'feet': feet, 'inches':inches}

# result = parse(feet_inches)
# print(result)

def convert (feet, inches):
  meters = feet * 0.3048 + inches * 0.0254
  return meters

parsed = parse(feet_inches)
result = (convert(parsed['feet'], parsed['inches']))
print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters")

if result < 1:
  print('kid is too small')
else:
  print('kid can use the slide')
