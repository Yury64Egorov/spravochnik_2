class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, last_name, first_name, phone_number, city, middle_name=None):
        contact = {
            'last_name': last_name,
            'first_name': first_name,
            'middle_name': middle_name,
            'phone_number': phone_number,
            'city': city
        }
        self.contacts.append(contact)
        print("Контакт успешно добавлен.")

    def edit_contact(self, index, field, new_value):
        if index < len(self.contacts):
            self.contacts[index][field] = new_value
            print("Контакт успешно отредактирован.")
        else:
            print("Контакта с таким индексом не существует.")

    def view_contacts(self):
        if self.contacts:
            for index, contact in enumerate(self.contacts):
                print(f"Контакт {index + 1}:")
                for key, value in contact.items():
                    print(f"{key}: {value}")
                print()
        else:
            print("Телефонная книга пуста.")

    def delete_contact(self, index):
        if index < len(self.contacts):
            del self.contacts[index]
            print("Контакт успешно удален.")
        else:
            print("Контакта с таким индексом не существует.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for contact in self.contacts:
                for key, value in contact.items():
                    file.write(f"{key}: {value}\n")
                file.write('\n')
        print("Контакты успешно сохранены в файле.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                contact = {}
                for line in file:
                    line = line.strip()
                    if line:
                        key, value = line.split(': ')
                        contact[key] = value
                    else:
                        self.contacts.append(contact)
                        contact = {}
                if contact:  # добавляем последний контакт
                    self.contacts.append(contact)
            print("Контакты успешно загружены из файла.")
        except FileNotFoundError:
            print("Файл с контактами не найден. Создайте новый.")

    def copy_contact(self, index, source_filename, target_filename):
        if index < len(self.contacts):
            contact = self.contacts[index]
            with open(target_filename, 'a') as target_file:
                target_file.write('\n')
                for key, value in contact.items():
                    target_file.write(f"{key}: {value}\n")
            print("Контакт успешно скопирован в другой файл.")
        else:
            print("Контакта с таким индексом не существует.")

def main():
    phonebook = Phonebook()
    filename = "phonebook.txt"
    phonebook.load_from_file(filename)

    while True:
        print("\nВыберите действие:")
        print("1. Добавить контакт")
        print("2. Редактировать контакт")
        print("3. Просмотреть контакты")
        print("4. Удалить контакт")
        print("5. Сохранить контакты в файл")
        print("6. Изменить контакт и сохранить в файл")
        print("7. Копировать контакт в другой файл")
        print("8. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество (необязательно): ")
            phone_number = input("Введите номер телефона: ")
            city = input("Введите город: ")
            phonebook.add_contact(last_name, first_name, phone_number, city, middle_name)

        elif choice == '2':
            index = int(input("Введите индекс контакта для редактирования: "))
            field = input("Введите поле для редактирования: ")
            new_value = input("Введите новое значение: ")
            phonebook.edit_contact(index - 1, field, new_value)

        elif choice == '3':
            phonebook.view_contacts()

        elif choice == '4':
            index = int(input("Введите индекс контакта для удаления: "))
            phonebook.delete_contact(index - 1)

        elif choice == '5':
            filename = input("Введите название файла для сохранения (с расширением .txt): ")
            phonebook.save_to_file(filename)

        elif choice == '6':
            index = int(input("Введите индекс контакта для изменения: "))
            field = input("Введите поле для изменения: ")
            new_value = input("Введите новое значение: ")
            filename = input("Введите название файла для сохранения (с расширением .txt): ")
            phonebook.edit_and_save_contact(index - 1, field, new_value, filename)

        elif choice == '7':
            index = int(input("Введите индекс контакта для копирования: "))
            source_filename = input("Введите имя файла, из которого нужно скопировать контакт: ")
            target_filename = input("Введите имя файла, в который нужно скопировать контакт: ")
            phonebook.copy_contact(index - 1, source_filename, target_filename)

        elif choice == '8':
            break

        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
