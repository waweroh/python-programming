def get_avg():
  with open('temps.txt', 'r') as f:
    temp = f.readlines()
    values = temp[1:]
    values = [float(i) for i in values]
    avg = float(sum(values) / len(values))
  return avg

average = get_avg()
print (average)