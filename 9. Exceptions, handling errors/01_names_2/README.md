## Задача 1. Имена 2
### Что нужно сделать
Есть файл `people.txt`, в котором построчно хранится N имён пользователей. 

Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа выводит общую сумму. Если в какой-либо строке меньше трёх символов (не считая литерала \n), то вызывается ошибка и сообщение, в какой именно строке возникла ошибка. Программа при этом не завершается и обрабатывает все имена файла.

Также при желании можно вывести все ошибки в отдельный файл `errors.log`.

**Пример работы программы**
```
Содержимое файла people.txt:
Василий
Николай
Надежда
Никита
Ян
Ольга
Евгения
Кристина

Ответ в консоли:
Ошибка: менее трёх символов в строке 5.
Общее количество символов: 49.
```
