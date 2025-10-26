def my_tabulate(data, headers):
	'''
	Функція для форматування таблиці логів
	Args:
		data (list of tuples): дані для таблиці
		headers (list): заголовки полів таблиці
	Returns:
		(str): відформатована таблиця у вигляді рядка
	'''
	# Визначення ширини кожного стовпця
	widths = [len(header) for header in headers]
	for row in data:
		for i, item in enumerate(row):
			widths[i] = max(widths[i], len(str(item)))
	
	# Формування рядка з роздільниками
	line = '|'
	for width in widths:
		line += '-' * (width + 2)
		if width != widths[-1]:
			line += '|'
	line += '\n'

	# Формування заголовку таблиці
	rows = []
	header_row = '|'
	for i, header in enumerate(headers):
		header_row += f" {header:<{widths[i]}}"
		if header != headers[-1]:
			header_row += " |"
		
	rows.append(f"{header_row}\n")
	rows.append(line)
	# Формування рядків таблиці
	for row in data:
		row_str = '|'
		for i, item in enumerate(row):
			row_str += f" {item:<{widths[i]}}"
			if item != row[-1]:
				row_str += " |"
		rows.append(row_str + '\n')
	return ''.join(rows) + line