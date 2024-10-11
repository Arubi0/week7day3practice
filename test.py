newphase = "rainstorm"
           #012345678
           #123456789 #college board
#create a mew variable called shortphase
# and assign it a vaule by slicing 
#the newphase variable by removing 
#the first 3 characters
#and the last 3 characters
# the first three characters are "rai"
#the last three characters are "orm"
#substring(string, start,end )
shortphase = newphase[3:len(newphase)-3]
#collegeboard version[4:len(newphase)-6]
print(shortphase)
#explain len(newphase)-3 = 9-3 = 6
#why does it end with 6?
#because the last index is not included