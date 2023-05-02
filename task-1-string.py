
#this a function to replace a charecter of specific index with another charecter

def task(sen,i,ch) :

#converting the string to a list so that  can modify 
    line = list(sen)

#replacing the char 
    line[i] = ch

#prinintg the resualt
    print(line)


task("sprints",0,'m')
