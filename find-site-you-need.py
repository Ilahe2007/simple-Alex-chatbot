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
  print("https://open.spotify.com/")
elif a=='2' or a=='code' or a=='programming' or a=='coding':
  a=str(input("Do you want to solve problems or learn programming or programming space?"))
  a=a.lower()
  if a=='solving' or a=='solve problems' or a=='solve':
    print('Recommended sites:')
    print('e-olymp: https://www.eolymp.com/az/problems')
    print('Hackerrank: https://www.hackerrank.com/dashboard')
    print('Codewars :https://www.codewars.com/dashboard')
  elif a=='learn programming' or a=='learn':
    print('Recommended sites:')
    print('Youtube: https://youtu.be/8DvywoWv6fI')
    print('W3schools: https://www.w3schools.com/')
    print('Coursera: https://www.coursera.org/')
    print('Stack Overflow: https://stackoverflow.com/')
    print('Recommended books:')
    print('https://www.trendyol.com/unikod/sifirdan-uzmanliga-python-programlama-p-46642459?boutiqueId=612660&merchantId=153818')
  else:
    print('Recommended compilers:')
    print('Colab: https://colab.research.google.com/drive/14hZVsH5sMvWsGa_ZOCgsUFqheAeAaBB9')
    print('Programiz: https://www.programiz.com/python-programming/online-compiler/')
elif a=='3' or a=='email' or a=='gmail':
  print('https://accounts.google.com/b/0/AddMailService')
elif a=='4' or a=='whatsapp web' or a=='wpweb' or a=='wp web':
  print('https://web.whatsapp.com/')
elif a=='5' or a=='youtube':
  print('https://www.youtube.com/')
elif a=='6' or a=='movies':
  print('https://fmovies.to/')
  print('https://b-bmovies.com/')
  print('https://cmovies.vc/film/the-big-bang-theory-season-12/watching.html?ep=10')
  print('https://www.themovieblog.com/2021/08/some-of-the-6-absolute-best-movie-channels/')
else:
  print('For your other needs please check google:')
  print('https://www.google.com/')
