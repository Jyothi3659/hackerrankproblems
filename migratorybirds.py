def migratorybirds(arr):
   bird_frequency =[0,0,0,0,0,0,0]
   for i in range(len(arr)):
       bird_frequency[arr[i]] += 1
   return bird_frequency.index(max(bird_frequency))


arr = [1,2,2,2,4,5,1,3,6]
print(migratorybirds((arr)))
