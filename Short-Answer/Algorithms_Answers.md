#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  
  a = 0
    while (a < n * n * n): -- will wait until a hits n**3
      a = a + n * n -- a increases n**2
    
    n**3 - n**2 = n, a will hit n**3 in n

  so O(N)

b)
  sum = 0
      for i in range(n): -- o(N)
        j = 1
        while j < n: -- will run until j hits n which is O(N)
          j *= 2 -- j increases by 2 so it will take power of 2 to reach each n
                -- so in relation to n it would be log n
          sum += 1
  o(n) * o(log n) = o(n log n)
   so o(n log n)

c) def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1) --- o(N) its like a for loop but recursive
    
    if bunnyEars was calledd it would be o(N), but its not so O(1)

## Exercise II


def anon(n):
  if n > f:
    egg broken
  else:
    egg lives

find n 

known for n story - n is sorted
lets say results is an array of results from each floor
in results[n] is stored results if egg is broken or not

the quick way to find which floor and minimize broken eggs is binary search

time complexity is O(log n)

So go to the middle floor of the building drop and egg depending 
on the results of the egg drop - then go up or down the middle section
and repeat until the solution is found