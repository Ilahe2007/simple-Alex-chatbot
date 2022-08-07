a=str(input())
a=a.capitalize()
if a=='Hi' or a=='Hello':
  print('Hi,i am Alex.I created by Ilaha to help you about few things.How are you?')
  a=str(input())
  if a=='I am great':
    print('How can i help you then?')
    a=str(input())
    if a=="Tell me joke" or a=='Tell me jokes':
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
    elif a=="How can i write 'Hello World' in python?":
      print('print("Hello World")')
  elif a=='I am bored':
    print('How can i entertain you?')
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
    elif a=="How can i write 'Hello World' in python?":
      print('print("Hello World")')
  elif a=='I am sad':
    print('How can i cheer you up?')
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
    elif a=="How can i write 'Hello World' in python?":
      print('print("Hello World")')
      a=str(input())
      print('bye')
  else:
    print('Bye then.')
