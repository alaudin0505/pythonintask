#Задача 5. Вариант 48
#Напишите программу, которая бы при запуске случайным образом отображала
#название одного из восьми категорий, на которые разделяются дорожные знаки в
#соответствии с Венской конвенцией о дорожных знаках и сигналах.

#Generalov K. A.

import random
a = random.choice(['Предупреждающие знаки.','Знаки преимущественного права проезда.','Запрещающие и ограничивающие знаки.', 'Предписывающие знаки.', 'Знаки особых предписаний.', 'Информационные знаки, знаки, обозначающие объекты и знаки сервиса.', 'Указатели направлений и информационно-указательные знаки.', 'Дополнительные таблички.'])
print(a)
input("\nВведите Enter для завершения")