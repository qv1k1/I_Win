<<<<<<< HEAD
# Проект 0. Угадай число 

## Оглавление:

[1. Описание проекта](README.md#описание-проекта)  
[2. Какой кейс решаем?](README.md#какой-кейс-решаем)  
[3. Краткая информация о данных](README.md#краткая-информация-о-данных)  
[4. Этапы работы над проектом](README.md#этапы-работы-над-проектом)  
[5. Результат](README.md#результат)  
[6. Выводы](README.md#выводы)  

### Описание проекта

Угадай число  
Нужно написать программу, которая угадывает число за минимальное число попыток.  

### Какой кейс решаем?

Условия соревнования:  
* Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число». 

* Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.  

* Необходимо добиться того, чтобы программа угадывала число меньше, чем за 20 попыток.  


### Краткая информация о данных

> Приведено два примера по решению этой задачи:
1. [Подход 1: Случайное угадывание]

### Этапы работы над проектом

### Результат

### Выводы




[def]: final_task_01.ipynb#
=======
# Проект 0. Угадай число 

## Оглавление:

[1. Описание проекта](README.md#описание-проекта)  
[2. Какой кейс решаем?](README.md#какой-кейс-решаем)  
[3. Краткая информация о данных](README.md#краткая-информация-о-данных)  
[4. Этапы работы над проектом](README.md#этапы-работы-над-проектом)  
[5. Результат](README.md#результат)  
[6. Выводы](README.md#выводы)  

### Описание проекта

Угадай число  
Нужно написать программу, которая угадывает число за минимальное число попыток.  

### Какой кейс решаем?

Условия соревнования:  
* Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число». 

* Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.  

* Необходимо добиться того, чтобы программа угадывала число меньше, чем за 20 попыток.  


### Краткая информация о данных

> Приведено два примера по решению этой задачи:
1. [Подход 1: Случайное угадывание](https://github.com/qv1k1/I_Win/blob/master/project_0/final_task_01.ipynb)
* Простейший способ решения: научить программу случайным образом выбирать число до тех пор, пока оно не будет угадано. Этот способ не дает хорошего результата, однако будет для нас хорошей стартовой точкой.  
2. [Подход 2: Угадывание с коррекцией](https://github.com/qv1k1/I_Win/blob/master/project_0/final_task_01.ipynb)
* Сначала устанавливаем любое случайное число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
3. [Функция для оценки](https://github.com/qv1k1/I_Win/blob/master/project_0/final_task_01.ipynb)
* Эта функция необходима, чтобы определить, за какое число попыток программа угадывает наше число.
4. [Оценка работы алгоритмов](https://github.com/qv1k1/I_Win/blob/master/project_0/final_task_01.ipynb)
* Определяем, какой подход лучше.


### Этапы работы над проектом

>Для решения данной задачи были применены следующие методы:
* Создаем max_pred и min_pred переменные их мы будем изменять по мере отлонения числа в большую или меньшую сторону. Это нужно для того, чтобы снизить диапозон угадывания чисел.
* В цикле прописываем формулу и за счет средних чисел подбираемся к загадоному числу.


### Результат

1. [Подход 3](https://github.com/qv1k1/I_Win/blob/master/project_0/final_task_01.ipynb)
* Мною разработанное решение

### Выводы

> В задание указано решить задачу менее чем за 20 попыток. В подходе 3, применена формула, которая позволяет узнать любое загадонное число максимум за 8 попыток.

[К оглавлению](README.md#оглавление)

>>>>>>> 56220fa200861e76c6489ee09cdf52d1b58bd0d8
