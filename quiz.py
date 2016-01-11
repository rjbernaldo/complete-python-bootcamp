#st = 'Print only the words that start with s in this sentence'
#
#for word in st.split():
#  if word[0].lower() == 's':
#    print word

#print [x for x in range(0,11) if x % 2 == 0]

#print [x for x in range(1,50) if x % 3 == 0]

#st = 'Print every word in this sentence that has an even number of letters'
#for word in st.split():
#  if len(word) % 2 == 0:
#    print word

for x in range(0,101):
  if x % 3 == 0:
    print 'Fizz'
  if x % 5 == 0:
    print 'Buzz'
  else:
    print x
