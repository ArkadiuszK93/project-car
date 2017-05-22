import xml.sax
from models import Osoba


class ExampleFileHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.inElement = False
        self.inPotomek = False
        self.text=""
    def startElement(self,name,attrs):
        if name == "student":
            self.inElement = True
            #for (k,v) in attrs.items():
                #print k,v
        if name == "adres":
            self.inPotomek = True

    def characters(self,ch):
        if self.inPotomek:
            #print "characters", ch
            self.text += ch
           
    def endElement(self,name):
        if name == 'student':
            #print self.text.strip()
            self.inElement = False
            self.text=""
        if name == 'adres':
            self.inPotomek = False

parser = xml.sax.make_parser()
parser.setContentHandler(ExampleFileHandler())
parser.parse(open("osoby.xml","r"))
   


"""



if __name__ == "__main__":
#zad1
    tab=[]
    x=5
    if x%2==1 :
       
        p=0
        k=x-1;
        for b in range(x):
            tab_temp=[]
            for a in range(x):
                if a==p or a==k :
                    #print "*",a,p,k
                    tab_temp.append("*")
                else:
                    tab_temp.append(" ")
                    #print "spacja",a,p,k
            tab.append(tab_temp)
            p=p+1
            k=k-1
            if p>k:
                p=p-1
                k=k+1
   
   
    else:
       
        p=0
        k=x-1;
        for b in range(x):
            tab_temp=[]
            for a in range(x-1):
                if a==p or a==k :
                    #print "*",a,p,k
                    tab_temp.append("*")
                else:
                    tab_temp.append(" ")
                    #print "spacja",a,p,k
            tab.append(tab_temp)
            p=p+1
            k=k-1
            if p>k:
                p=p-1
                k=k+1
    for elem in tab:       
        print elem
               
                   
   
#zad 2
    #x=input("Podaj x:")
    a=[]
    for num in range(1,6):
        x=[num]
        for num2 in range(0,num -1):
            x.append(num)
            #print(x)
        a.append(x)
    print "Zad1",a
#zad3a   
    lista_zad2=[]
    for num in range(1,11):
        x=(num,num*num)
        lista_zad2.append(x)
    print "Zad2a",lista_zad2
#zad3b       
    lista_wiek=[]
    lista_lata=[1993,1920,2000,1995,1993]
    for elem in lista_lata:
        x=2017-elem
        lista_wiek.append(x)
    print "Zad2b",lista_lata
    print "Zad2b",lista_wiek
#zad3c
    lista_zad3c=[]
    for num in range(1,1001):
        if num%7==0 and num%5!=0:
            lista_zad3c.append(num)
    print lista_zad3c
   
    """
