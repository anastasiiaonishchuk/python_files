gender = ''
while (gender != 'выход'):
   gender = input('Если хочешь закончить, набери “выход”\nПожалуйста, укажи свой пол:')
   if (gender == 'мальчик' or gender == 'мужчина' or gender == 'юноша' or gender == 'муж' or gender == 'male' or gender == 'м' or gender == 'm'):
       print( 'wazzaaaap' )
   elif (gender == 'девочка' or gender == 'женщина' or gender == 'девушка' or gender == 'жен' or gender == 'female' or gender == 'female' or gender == 'ж' or gender == 'f'):
           print('Hi, darling')
   else:
       print('Hello')
print('Bye')
