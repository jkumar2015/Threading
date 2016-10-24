import threading
import math
from pip._vendor.distlib.compat import raw_input


class ThreadingPython(threading.Thread):
    """
    Author: Jyoti Kumar
    Class: 4AHITM
    Homework: Threading in Python (SEW)
    Date: 21.10.2016

    Information to Class:
    The Class shows how to use threading in
    encrypting & decrypting a message from input of user.
    Where he can select the power of
    encryption and the numbers of threads.
    Where the Output has to be in Upper Case

    """



    def __init__(self,text,zahl,threads,auswahl):

        """
        :param self: refers to init
        :param text: user input
        :param zahl: user input
        :param threads: user input
        :param auswahl: user input

        The __init__ method is like the constructer in java ,
        in this method you define all parameter you need in yor class
        that you can easily refer to them by using self.

        """

        threading.Thread.__init__(self)
        self.text = text
        self.zahl = zahl
        self.threads = threads
        self.auswahl = auswahl


    def example(self):

        """
        :param self:refers to init
        :return self.liste: for example_reverse2

        The encryption method used for this class was
        Ceaser encryption. In which one can
        choose how strong he wants to encrypt.

        For example: A (encryption 2) is C

        The aim of returning the list is, to
        be able to use it in the  first way of decryption.

        If the text contains "z", the
        if clause will start counting from a +
        the number how strong it should encrypt.

        If the text contains a space, the if clause
        won´t change it and return it as it is.

        If the text contains characters under 97
        and up to 122 they will ignored and returned as
        they are. For example "!" will stay "!" or
        "2" will be "2"
        """


        self.liste = ""

        for x in text.lower():

            if x == "z":
               x = chr(int(96) + int(zahl))
               self.liste += x

            elif x == " ":
                self.liste += x

            elif ord(x) < 97 or ord(x) > 122:
                self.liste += x


            else:
                change1 = (chr(ord(x) + int(zahl)))
                self.liste += change1

        print(("Your encrypted message: %s")%self.liste.upper())
        return self.liste

    def example_reverse(self):

        """
        :param self: refers to init

        The class also has 2 ways of decryption.
        One the easier way by just giving the original message
        returned in upper case.

        """

        print (("Your decrypted message in the first way: %s")%self.text.upper())

    def example_reverse2(self):

        """
        :param self: refers to init

        The second way is to reverse the whole
        process of encryption one by one.

        If text contains a character "a"
        it should set the counter to "z"
        and calculate from z - number(how strong
        the text should be encrypted).

        If the text contains a space
        it won´t be changed.

        If the text contains any
        character which is not between
        a and z it will be ignored.

        If the Integer value of
        x is less than 97
        it should start counting from
        z -number(how strong
        the text should be encrypted).

        Othervise the method
        should just reverse the
        process of encryption

        At the end the result should
        be printed in upper case.

        """

        liste_reverse = ""

        for x in self.liste.lower():

            if x == "a":
               x = chr(int(123) - int(self.zahl))
               liste_reverse += x

            elif x == " ":
                liste_reverse += x

            elif ord(x) < 97 or ord(x) > 122:
                liste_reverse += x

            elif ord(x) -int(self.zahl) < 97:
                help = ord(x)-int(self.zahl)
                help2 = 97-help
                x = chr(int(123) - int(help2))
                liste_reverse += x

            else:
                change1_reverse = (chr(ord(x) - int(self.zahl)))
                liste_reverse += change1_reverse


        print(("Your decrypted message in the second way: %s")%liste_reverse.upper())



    def run(self):

        """
        :param self: refers to init

        If the user input is 1
        the method encryption will
        be called


        If the user input is 2
        the first way of
        encryption will be called

        If the user input is 3
        the encryption and decryption method will
        be called because
        the second decryption method need
        the list from encryption method.

        If the user input is 0
        the program will be quit
        no method will be called

        """

        if(self.auswahl==1):
         self.example()
        elif(self.auswahl==2):
         self.example_reverse()
        elif(self.auswahl==3):
          self.example()
          self.example_reverse2()
        elif(self.auswahl==0):
             quit()


text = raw_input("Which message do you want to encrypt?")
text = text.lower()
zahl = raw_input("How strong do you want to encrypt your input type a number?")
threads = int(raw_input("How many threads should encrypt the message?"))

if(int(threads)>len(text)):
        print ("Please enter a thread number which has the number less than your text length ")
        quit()

if (int(threads) == 0):
        print("Please enter a thread number which has the number less than your text length ")
        quit()

auswahl = int(raw_input("What do you want to do? 1=encryption 2= decryption1 3= decryption2 0=exit :"))

mycounter = []



for i in range(threads):

      #ZeroDivisionError: print ("Please enter a valid number of threads!")

        anzahlderparts = int(len(text) / threads)
        anfangsstartwert = i * anzahlderparts
        endstartwert = anfangsstartwert + anzahlderparts

        mycounter.append(text[anzahlderparts:endstartwert])

# the for loop iterates throw threads number, (took help by Markus Reichl)
# anzahlderparts:the length divided by threads makes portion of text and
# returns the number in how many portions the text it is divided
# anfangsstartwert: i increments throw the loop, so
# the number will variate throw out the for loop, every
# beginning part of the portion will be run throw threads
# endstartwert: to have every portion/part from text
# the endstartwert stores the beginning + the end = the last character



thread1 = ThreadingPython(text,zahl,threads,auswahl) #creating thread by calling the class (like in Java by new)

thread1.start() #starting the run method, thread1.stop not important, it will
                #automatically stop at the last line of run method

#######################################################################################################################