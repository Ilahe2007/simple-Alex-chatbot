import webbrowser
print('Hi,i am Alex.I created by Ilaha to help you about few things.How are you?')
a=str(input())
a=a.lower()
if a=='i am great':
    print('How can i help you then?')
    a=str(input())
    a=a.lower()
    if a=="tell me joke" or a=="tell me a joke" or a=='tell me jokes':
        print('Why did the gym closed down?')
        a=str(input(''))
        print('Because it did not worked out.')
        print('HA HA HA')
        a=int(input('If you want hear more press 1 else press 0:'))
        if a==0:
            print('Bye')
        else:
            print('How do actors stay cool?')
            print('They have a lot of fans.')
            print('HA HA HA')
    elif a=='search something' or a=='search':
        print("what do you want me search")
        print('1.music')
        print('2.code(programming)')
        print('3.email')
        print('4.whatsapp web')
        print('5.youtube')
        print('6.movies')
        print('7.others')
        a=str(input('Choose one: '))
        a=a.lower()
        if a=='1' or a=='music':
            webbrowser.open("https://open.spotify.com/")
        elif a=='2' or a=='code' or a=='programming' or a=='coding':
            a=str(input("Do you want to solve problems or learn programming or programming space?"))
            a=a.lower()
            if a=='solving' or a=='solve problems' or a=='solve':
                print('Chose one of the recommended sites:')
                print('1.e-olymp')
                print('2.hackerrank')
                print("3.codewars")
                a=str(input())
                a=a.lower()
                if a=='e-olymp' or a=='eolymp':
                    webbrowser.open('https://www.eolymp.com/az/problems')
                elif a=='hackerrank':
                    webbrowser.open('https://www.hackerrank.com/dashboard')
                else:
                    webbrowser.open('https://www.codewars.com/dashboard')
            elif a=='learn programming' or a=='learn':
                a=str(input("book or site?"))
                a=a.lower()
                if a=='site' or a=='sites':
                    print('Recommended sites:')
                    print('1.W3schools')
                    print('2.Coursera')
                    print('3.Stack Overflow')
                    a=str(input())
                    a=a.lower()
                    if a=='1' or a=='w3schools':
                        webbrowser.open('https://www.w3schools.com/')
                    elif a=='2' or a=='coursera':
                        webbrowser.open('https://www.coursera.org/')
                    else:
                        webbrowser.open('https://stackoverflow.com/')
                else:
                    webbrowser.open('https://www.trendyol.com/unikod/sifirdan-uzmanliga-python-programlama-p-46642459?boutiqueId=612660&merchantId=153818')
            else:
                webbrowser.open('Colab: https://colab.research.google.com/drive/14hZVsH5sMvWsGa_ZOCgsUFqheAeAaBB9')
        elif a=='3' or a=='email' or a=='gmail':
            webbrowser.open('https://accounts.google.com/b/0/AddMailService')
        elif a=='4' or a=='whatsapp web' or a=='wpweb' or a=='wp web':
            webbrowser.open('https://web.whatsapp.com/')
        elif a=='5' or a=='youtube':
            webbrowser.open('https://www.youtube.com/')
        elif a=='6' or a=='movies':
            webbrowser.open('https://fmovies.to/')
        else:
            print('For your other needs please check google:')
            webbrowser.open('https://www.google.com/')
elif a=='i am bored':
    print('How can i entertain you?')
    a=str(input())
    a=a.lowe()
    if a=="tell me joke" or a=="tell me a joke" or a=="tell me jokes":
        print('Why did the gym closed down?')
        a=str(input(''))
        print('Because it did not worked out.')
        print('HA HA HA')
        a=int(input('If you want hear more press 1 else press 0:'))
        if a==0:
            print('Bye')
        else:
            print('How do actors stay cool?')
            print('They have a lot of fans.')
            print('HA HA HA')
    elif a=='search something' or a=='search':
        print("what do you want me search")
        print('1.music')
        print('2.code(programming)')
        print('3.email')
        print('4.whatsapp web')
        print('5.youtube')
        print('6.movies')
        print('7.others')
        a=str(input('Choose one: '))
        a=a.lower()
        if a=='1' or a=='music':
            webbrowser.open("https://open.spotify.com/")
        elif a=='2' or a=='code' or a=='programming' or a=='coding':
            a=str(input("Do you want to solve problems or learn programming or programming space?"))
            a=a.lower()
            if a=='solving' or a=='solve problems' or a=='solve':
                print('Chose one of the recommended sites:')
                print('1.e-olymp')
                print('2.hackerrank')
                print("3.codewars")
                a=str(input())
                a=a.lower()
                if a=='e-olymp' or a=='eolymp':
                    webbrowser.open('https://www.eolymp.com/az/problems')
                elif a=='hackerrank':
                    webbrowser.open('https://www.hackerrank.com/dashboard')
                else:
                    webbrowser.open('https://www.codewars.com/dashboard')
            elif a=='learn programming' or a=='learn':
                a=str(input("book or site?"))
                a=a.lower()
                if a=='site' or a=='sites':
                    print('Recommended sites:')
                    print('1.W3schools')
                    print('2.Coursera')
                    print('3.Stack Overflow')
                    a=str(input())
                    a=a.lower()
                    if a=='1' or a=='w3schools':
                        webbrowser.open('https://www.w3schools.com/')
                    elif a=='2' or a=='coursera':
                        webbrowser.open('https://www.coursera.org/')
                    else:
                        webbrowser.open('https://stackoverflow.com/')
                else:
                    webbrowser.open('https://www.trendyol.com/unikod/sifirdan-uzmanliga-python-programlama-p-46642459?boutiqueId=612660&merchantId=153818')
            else:
                webbrowser.open('Colab: https://colab.research.google.com/drive/14hZVsH5sMvWsGa_ZOCgsUFqheAeAaBB9')
        elif a=='3' or a=='email' or a=='gmail':
            webbrowser.open('https://accounts.google.com/b/0/AddMailService')
        elif a=='4' or a=='whatsapp web' or a=='wpweb' or a=='wp web':
            webbrowser.open('https://web.whatsapp.com/')
        elif a=='5' or a=='youtube':
            webbrowser.open('https://www.youtube.com/')
        elif a=='6' or a=='movies':
            webbrowser.open('https://fmovies.to/')
        else:
            print('For your other needs please check google:')
            webbrowser.open('https://www.google.com/') 
else:
    print('How can help you?')
    a=str(input())
    if a=="Tell me joke":
        print('Why did the gym closed down?')
        a=str(input(''))
        print('Because it did not worked out.')
        print('HA HA HA')
        a=int(input('If you want hear more press 1 else press 0:'))
        if a==0:
            print('Bye')
        else:
            print('How do actors stay cool?')
            print('They have a lot of fans.')
            print('HA HA HA')
    elif a=='search something' or a=='search':
        print("what do you want me search")
        print('1.music')
        print('2.code(programming)')
        print('3.email')
        print('4.whatsapp web')
        print('5.youtube')
        print('6.movies')
        print('7.others')
        a=str(input('Choose one: '))
        a=a.lower()
        if a=='1' or a=='music':
            webbrowser.open("https://open.spotify.com/")
        elif a=='2' or a=='code' or a=='programming' or a=='coding':
            a=str(input("Do you want to solve problems or learn programming or programming space?"))
            a=a.lower()
            if a=='solving' or a=='solve problems' or a=='solve':
                print('Chose one of the recommended sites:')
                print('1.e-olymp')
                print('2.hackerrank')
                print("3.codewars")
                a=str(input())
                a=a.lower()
                if a=='e-olymp' or a=='eolymp':
                    webbrowser.open('https://www.eolymp.com/az/problems')
                elif a=='hackerrank':
                    webbrowser.open('https://www.hackerrank.com/dashboard')
                else:
                    webbrowser.open('https://www.codewars.com/dashboard')
            elif a=='learn programming' or a=='learn':
                a=str(input("book or site?"))
                a=a.lower()
                if a=='site' or a=='sites':
                    print('Recommended sites:')
                    print('1.W3schools')
                    print('2.Coursera')
                    print('3.Stack Overflow')
                    a=str(input())
                    a=a.lower()
                    if a=='1' or a=='w3schools':
                        webbrowser.open('https://www.w3schools.com/')
                    elif a=='2' or a=='coursera':
                        webbrowser.open('https://www.coursera.org/')
                    else:
                        webbrowser.open('https://stackoverflow.com/')
                else:
                    webbrowser.open('https://www.trendyol.com/unikod/sifirdan-uzmanliga-python-programlama-p-46642459?boutiqueId=612660&merchantId=153818')
            else:
                webbrowser.open('Colab: https://colab.research.google.com/drive/14hZVsH5sMvWsGa_ZOCgsUFqheAeAaBB9')
        elif a=='3' or a=='email' or a=='gmail':
            webbrowser.open('https://accounts.google.com/b/0/AddMailService')
        elif a=='4' or a=='whatsapp web' or a=='wpweb' or a=='wp web':
            webbrowser.open('https://web.whatsapp.com/')
        elif a=='5' or a=='youtube':
            webbrowser.open('https://www.youtube.com/')
        elif a=='6' or a=='movies':
            webbrowser.open('https://fmovies.to/')
        else:
            print('For your other needs please check google:')
            webbrowser.open('https://www.google.com/')
