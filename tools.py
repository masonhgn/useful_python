#these are some useful ways to do things in python that I don't want to forget about



#how to convert a list of strings into a list of ints
nums = ['123','412']
nums = list(map(int, nums))


#how to make a 2d array
x = [[foo for i in range(10)] for j in range(10)]


#how to count vowels in a string

def vowels(st):
  return len([st.count(x) for x in 'aeiou'])


#make frequency map
count[i] = count.get(i, 0) + 1
