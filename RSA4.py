"""Group Members
1. Henok Matheas   UGR/2553/12
2. Kaleab Taye     UGR/0490/12
3. Kaleab Tekalign UGR/3664/12
4. Betel Tagesse   UGR/5409/12
5. Beka Dessalegn  UGR/4605/12
6. Bethlehem Alula UGR/0462/12
7. Tsega Yakob     UGR/8465/12 """


p=721960629061904110756973047896820529650646626913987914193058081946869300323505631503613785147235083747598529092067962512605338801581684234964490805070294572618497933653948906694134011361476095650659862416376029070102910970128990995504864728056436234936733309062195718092793663000312918831684212336353
q=991983977971967953947941937929919911907887883881877863859857853839829827823821811809797787773769761757751743739733727719709701691683677673661659653647643641631619617613607601599593587577571569563557547541523521509503499491487479467463461457449443439433431421419409401397389383379373367359353349347337

e=57

n=p*q

phi_n=(p-1)*(q-1)


def rel_prime(p,q):
    if  min(p,q)==1:
        return True
    elif min(p,q)==0:
        return False
    else:
        return rel_prime(min(p,q),max(p,q)%min(p,q))

print(rel_prime(e,phi_n))

d=(pow(e,-1,phi_n))



message=input("input a string: ")


print(f"\n public key e: {e}"
      f"\n and n={n}")


def m_num(message):
    "converts the string message into numeric format"
    number=""
    for i in message.upper():
        number+=str(ord(i))
    return int(number)



def int_to_string(number,word):
    "converts the numeric form into string format"
    if number<=90:
        word=str(chr(number))+word
        return word
    else:
        word=str(chr(number%100))+word
        return int_to_string(number//100,word)




def simplifier(message,e,n):
    if not rel_prime(message,n):
        return "message and n are not relatively prime, could you change your wording and try again."
    rem=1
    while(e>2):
        rem*=message**(e%2)
        e=e//2
        message=pow(message,2,n)
    return pow(message*rem,e,n)


def encrypt(message,e,n):
    enc = (simplifier(m_num(message),e,n))
    return enc


def decrypt(encrypted,d,n):
    dec=(simplifier(encrypted,d,n))
    return int_to_string(dec,"")



enc=encrypt(message,e,n)

print(enc)


dec=decrypt(enc,d,n)

print(dec,"this is the decrypted")


