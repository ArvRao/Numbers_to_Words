# NUMBERS TO WORDS CONVERSION IN PYTHON (INDIAN NUMBER SYSTEM)

def words(n):
    units = ['Zero', 'One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    teens = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Ninteen']
    tens = ['Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']
    if n>=0 and n<=9:
        return units[n]
    elif n>=10 and n<=19:
        return teens[n-10]
    elif n>=20 and n<=99:
        return tens[(n//10)-2] + " " + (units[n%10] if n%10!=0 else "")
    elif n>=100 and n<=999:
        return units[n//100] + " Hundred " + (words(n%100) if n%100!=0 else "")
    elif n>=1000 and n<=99999:
        return words(n//1000) + " Thousand " + (words(n%1000) if n%1000!=0 else "")
    elif n>=100000 and n<=9999999:
        return words(n//100000) + " Lakh "+(words(n%100000) if n%100000!=0 else "") 
    elif n>=10000000 and n<=99999999999:
        return words(n//10000000) + " Crore " + (words(n%10000000) if n%10000000!=0 else "")
    else:
        return 'Provide a valid number from one digit to eleven digits.'
    
#print(words(56749089032)) --> Five Thousand Six Hundred Seventy Four Crore Ninety  Lakh Eighty Nine Thousand Thirty Two
#print(words(-1)) --> Provide a valid number from one digit to eleven digits.