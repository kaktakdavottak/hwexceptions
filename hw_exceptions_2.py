documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "nme": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def search_person_by_document_number(documents):
  user_input = input('Введите номер документа:')
  for document in documents:
    if document["number"] == user_input:
      print('Документ с данным номером принадлежит {}'.format(document["name"]))
      break
  else:
    print('Документов с таким номером не обнаружено')


def print_all_documents(documents):
  for document in documents:
    print(document["type"], document["number"], document["name"])


def search_directory_by_document_number(directories):
  user_input = input('Введите номер документа:')
  for directory, document_number in directories.items():
    if user_input in document_number:
      print('Документ с таким номером лежит на полке №{}'.format(directory))
      break
  else:
    print('Документов с таким номером не обнаружено')


def add_new_document(documents, directories):
  user_input_type = input('Введите тип документа:')
  user_input_number = input('Введите номер документа:')
  user_input_name = input('Введите имя владельца:')
  user_input_directory = input('Введите номер полки для документа:')
  documents.append({"type": user_input_type, "number": user_input_number, "name": user_input_name})
  print(documents)
  if user_input_directory in directories.keys():
    directories[user_input_directory].append(user_input_number)
    print(directories)
  else:
    directories[user_input_directory] = list()
    directories[user_input_directory].insert(len(directories[user_input_directory]) + 1, user_input_number)
    print(directories)


def delet_document_by_number(documents, directories):
  user_input = input('Введите номер документа:')
  for i, document in enumerate(documents):
    if document["number"] == user_input:
      del(documents[i])
      print(documents)
  for directory_list in directories.values():
    if user_input in directory_list:
      directory_list.remove(user_input)
      print(directories)


def move_from_directory_to_directory(directories):
  user_input_number = input('Введите номер документа:')
  user_input_directory = input('Введите номер новой полки для документа:')
  for directory_list in directories.values():
    if user_input_number in directory_list:
      directory_list.remove(user_input_number)
  if user_input_directory in directories.keys():
    directories[user_input_directory].append(user_input_number)
    print(directories)
  else:
    directories[user_input_directory] = list()
    directories[user_input_directory].insert(0, user_input_number)
    print(directories)


def add_new_shelf(directories):
  user_input_directory = input('Введите номер новой полки:')
  if user_input_directory not in directories.keys():
    directories[user_input_directory] = list()
    print(directories)


# Доманшнее задание по теме исключения:
# Расширить домашние задание из лекции 1.4 «Функции — использование встроенных и создание собственных» новой функцией,
# выводящей имена всех владельцев документов. С помощью исключения KeyError проверяйте, если поле "name" и документа.
# Ключ name в одном из документов "испорчен"

def print_names(documents):
    for document in documents:
        try:
            print(document["name"])
        except KeyError:
            print('Документ №{} не содержит поле "Имя"'.format(document["number"]))


while True:
  input_menu = input('\nСписок доступных команд:\n\n'
                     ' p – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\n'
                     ' l – команда, которая выведет список всех документов;\n'
                     ' s – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\n'
                     ' a – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,'
                     ' имя владельца и номер полки, на котором он будет храниться;\n'
                     ' m – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;\n'
                     ' d – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;\n'
                     ' as – команда, которая спросит номер новой полки и добавит ее в перечень;\n'
                     ' ex - дополнительная команда из урока исключений\n'
                     ' Для выхода из программы введите Выход\n\n'
                     ' Введите нужную команду:')
  if input_menu == 'Выход':
    break
  elif input_menu == 'p':
    search_person_by_document_number(documents)
  elif input_menu == 'l':
    print_all_documents(documents)
  elif input_menu == 's':
    search_directory_by_document_number(directories)
  elif input_menu == 'a':
    add_new_document(documents, directories)
  elif input_menu == 'm':
    move_from_directory_to_directory(directories)
  elif input_menu == 'd':
    delet_document_by_number(documents, directories)
  elif input_menu == 'as':
    add_new_shelf(directories)
  elif input_menu == 'ex':
    print_names(documents)
  else:
    print('Данная команда недоступна')
