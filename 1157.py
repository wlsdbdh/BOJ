w = list(map(str, input()))

count = {}
for i in w :
  i = i.upper()
  if i in count :
      count[i] += 1
  else :
      count[i] = 1

ans = [k for k, v in count.items() if max(count.values()) == v]
if len(ans) == 1 :
  print (*ans)
else :
  print ("?")
