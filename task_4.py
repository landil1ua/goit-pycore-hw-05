def input_error(func):
    '''
    Декоратор для обробки помилок вводу користувача
    Args:
        func (function): функція-обробник команди
    Returns:
        (function): обгорнута функція-обробник команди
    '''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Give me right arguments please."
        except IndexError:
            return "Please enter a name."
    return inner


@input_error
def add_contact(args, contacts):
    '''
    Функція додавання нового контакту
    Args:
        args (list): ім'я та номер телефону
        contacts(dict): словник із контактами
    Returns:
        (str): результат операції
    '''
    name, phone = args
    contacts[name] = phone
    return 'Contact added'


@input_error
def change_contact(args, contacts):
    '''
    Функція зміни існуючого контакту
    Args:
        args (list): ім'я та номер телефону
        contacts(dict): словник із контактами
    Returns:
        (str): результат операції
    '''
    name, new_phone = args
    if name not in contacts:
        raise KeyError('Contact not found')
    contacts[name] = new_phone
    return 'Contact updated'


@input_error
def show_phone(args, contacts):
    '''
    Функція пошуку номеру телефону за ім'ям
    Args:
        args (list): ім'я
        contacts(dict): словник із контактами
    Returns:
        (str): результат операції
    '''
    name = args[0]
    phone = contacts[name]
    return f'[{phone}]'


def show_all(contacts):
    '''
    Функція виводу усіх доданих контактів
    Args:
        contacts(dict): словник із контактами
    Returns:
        (str): результат операції
    '''
    if not contacts:
        return 'No added contacts'
    lines = [f"{name}: [{contacts[name]}]" for name in sorted(contacts)]
    return "\n".join(lines)


def parse_input(user_input):
    '''
    helper функція. Парсер вводу користувача
    Args:
        user_input (str): команда користувача
    Returns:
        (str, list): назва команди, аргументи команди
    '''
    if not user_input:
        return '', []

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


def main():
    contacts = {}  # словник із контактами (поки що у форматі dict)

    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        # пошук відповідної команди
        if command in ['close', 'exit']:
            print('Good bye!')
            break

        elif command == '':
            continue

        elif command == 'hello':
            print('How can I help you?')

        elif command == 'add':
            print(add_contact(args, contacts))

        elif command == 'change':
            print(change_contact(args, contacts))

        elif command == 'phone':
            print(show_phone(args, contacts))

        elif command == 'all':
            print(show_all(contacts))

        else:
            print('Invalid command')


if __name__ == '__main__':
    main()
