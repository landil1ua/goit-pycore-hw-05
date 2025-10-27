import sys
from my_tabulate import my_tabulate as tabulate


def load_logs(log_path: str):
    """
    Завантаження логів з файлу
    Args:
        log_path (str): шлях до файлу з логами
    Returns:
        list: список словників з логами
    """
    with open(log_path, 'r', encoding='utf-8') as f:
        return [parse_log_line(i) for i in f]


def parse_log_line(line: str) -> dict:
    '''
    Парсинг рядка логів
    Args:
        line (str): рядок з логами
    Returns:
        dict: словник з даними логів
    '''
    splitted = line.strip().split(maxsplit=3)
    return {key: value for key, value in
            zip(['date', 'time', 'level', 'message'], splitted)}


def filter_logs_by_level(logs: list, level: str):
    '''
    Фільтрація логів за рівнем
    Args:
        logs (list): список логів
        level (str): рівень логування
    Returns:
        list: відфільтрований список логів
    '''
    if not level:
        return []
    logs_level = [log for log in logs
                  if log['level'].lower() == level.lower()]
    return logs_level


def count_logs_by_level(logs: list) -> dict:
    '''
    Підрахунок логів за рівнем
    Args:
        logs (list): список логів
    Returns:
        dict: словник з кількістю логів за рівнем
    '''
    counts = {}

    for log in logs:
        lvl = log['level']
        if lvl not in counts:
            counts[lvl] = 1
        else:
            counts[lvl] += 1

    return counts


def display_log_counts(counts: dict):
    '''
    Відображення кількості логів за рівнем
    Args:
        counts (dict): словник з кількістю логів за рівнем
    Returns:
        str: відформатована таблиця з кількістю логів
    '''
    table = [(level, count) for level, count in counts.items()]
    return tabulate(table, headers=["Рівень логування", "Кількість"])


def main(argv):
    len_argv = len(argv)  # довжина списку аргументів
    level = None  # рівень логування за замовчуванням

    # перевірка наявності необхідних аргументів
    if len_argv < 2:
        return -1
    log_path = argv[1]
    if len_argv > 2:
        level = argv[-1]

    logs = load_logs(log_path)  # завантаження логів з файлу
    counts = count_logs_by_level(logs)  # підрахунок логів за рівнем
    # фільтрація логів за рівнем
    details_level = filter_logs_by_level(logs, level)

    # відображення результатів
    print(display_log_counts(counts))

    # деталі логів для вказаного рівня
    if level and details_level:  # якщо рівень вказано та є логи
        print(f'\nДеталі логів для рівня {level.upper()}:')
        for i in details_level:
            print(f"{i['date']} {i['time']} - {i['message']}")
        print('\n')
    else:  # якщо рівень вказано, але логів для цього рівня немає
        print(f'\nЛоги для рівня {level.upper()} відсутні.\n')

    # успішне завершення
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
