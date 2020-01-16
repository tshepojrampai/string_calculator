import re

#Add function
def add(string):
    if len(string) == 0:
      return 0
    result = 0
    negs = []
    digits = re.findall(r"-?\d+", string)
    
    for i in digits:
        i = int(i)
        if i < 0:
            negs.append(num)
        if i < 1000:
            result = result + int(i)
        else:
            if i>1000:
                result= 0
    if len(negs) > 0:
        exception = "-numbers not allowed! "
        for i in range(len(negs)):
            if i != len(negs)-1:
                exception += str(negs[i]) + ", "
            else:
                exception += str(negs[i]) + "."
        raise Exception(exception)

    return result
  

