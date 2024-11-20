## Задача 3. Глубокое копирование
### Что нужно сделать
Вы сделали для заказчика структуру сайта по продаже телефонов:
```python
site = {
	'html': {
		'head': {
			'title': 'Куплю/продам телефон недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на iPhone',
			'div': 'Купить',
			'p': 'Продать'
		}
	}
}
```

Заказчик рассказал своим коллегам на рынке, и они тоже захотели такой сайт, только для своих товаров. Вы посчитали, что это лёгкая задача, и быстро принялись за работу. 

Напишите программу, которая запрашивает у клиента, сколько будет сайтов, а затем запрашивает название продукта и после каждого запроса выводит на экран активные сайты. 

Условия:
- Учтите, что функция должна уметь работать с разными сайтами (иначе вам придётся переделывать программу под каждого заказчика заново);
- Вы должны получить список, хранящий сайты для разных продуктов (а значит, для каждого продукта нужно будет первым делом выполнить `глубокое` копирование сайта).

### Подсказка: 
- Чтобы заменить элемент, его нужно найти. Для поиска можете использовать рекурсивный алгоритм из задачи по поиску элемента.

Пример:
```
Сколько сайтов: 2
Введите название продукта для нового сайта: iPhone
Сайт для iPhone: 
site = {
	'html': {
		'head': {
			'title': 'Куплю/продам iPhone недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на iPhone',
			'div': 'Купить',
			'p': ‘Продать'
		}
	}
}

Введите название продукта для нового сайта: Samsung
Сайт для iPhone: 
site = {
	'html': {
		'head': {
			'title': 'Куплю/продам iPhone недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на iPhone',
			'div': 'Купить',
			'p': ‘Продать'
		}
	}
}

Сайт для Samsung: 
site = {
	'html': {
		'head': {
			'title': 'Куплю/продам Samsung недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на Samsung',
			'div': 'Купить',
			'p': ‘Продать'
		}
	}
}
```