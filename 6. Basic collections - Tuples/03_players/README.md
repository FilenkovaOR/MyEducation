## Задача 3. Игроки
### Что нужно сделать
У вас есть словарь игроков, которые участвовали в трёх видах спорта. В словаре хранятся пары «ФИ — очки»:

```python
players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
```

Один программист попросил нас для его базы прислать другой вариант хранения этой информации.

Напишите программу, которая объединяет ключ словаря со значением в один кортеж, и выведите результат на экран. Постарайтесь использовать как можно более эффективное решение.

Результат работы программы:

```
[('Ivan', 'Volkin', 10, 5, 13), ('Bob', 'Robbin', 7, 5, 14), ('Rob', 'Bobbin', 12, 8, 2)]
```
