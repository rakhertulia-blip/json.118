import cases
import storage


def show_cases(items):
    if len(items) == 0:
        print("Журнал пуст.")
        return

    for item in items:
        print("ID:", item["id"])
        print("Название:", item["title"])
        print(" Статус:", item["status"])


def read_id():
    text = input("Введите ID: ").strip()

    try:
        case_id = int(text)

    except ValueError:
        print("Ошибка: ID должен быть целым числом.")
        return None

    if case_id <= 0:
        print("Ошибка: ID должен быть положительным.")
        return None

    return case_id


def main():
    items = storage.load_cases("cases.json")

    if items is None:
        print("Ошибка: файл cases.json повреждён или содержит неверные данные.")
        return

    while True:
        print("\n--- Журнал тестовых проверок EKEB ---")
        print("1 - Список проверок")
        print("2 - Добавить проверку")
        print("3 - Изменить результат")
        print("4 - Сводка")
        print("5 - Сохранить")
        print("0 - Выход")

        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            show_cases(items)

        elif choice == "2":
            title = input("Введите название проверки: ")
            case_id = cases.add_case(items, title)

            if case_id is None:
                print("Название должно содержать минимум 5 символов.")
            else:
                print("Проверка добавлена. ID:", case_id)
                print("Для сохранения выберите пункт 5.")

        elif choice == "3":
            case_id = read_id()

            if case_id is None:
                continue

            status = input("Введите статус (pending/pass/fail): ")


            result = cases.set_result(items, case_id, status)

            if result == "updated":
                print("Результат изменён.")

            elif result == "unchanged":
                print("Этот статус уже установлен.")

            elif result == "not_found":
                print("Проверка с таким ID не найдена.")

            else:
                print("Неверный статус. Используйте pending, pass или fail.")
        elif choice == "4":
            summary = cases.summarize(items)

            print("Всего:", summary["total"])
            print("Не проверено:", summary["pending"])
            print("Пройдено:", summary["pass"])
            print("Ошибки:", summary["fail"])

        elif choice == "5":
            if storage.save_cases("cases.json", items):
                print("Данные сохранены.")
            else:
                print("Не удалось сохранить данные.")

        elif choice == "0":
            answer = input("Сохранить? да/нет: ").strip().lower()

            if answer == "да":
                if storage.save_cases("cases.json", items):
                    print("Данные сохранены. До свидания!")
                    break

                print("Не удалось сохранить. Попробуйте снова.")

            elif answer == "нет":
                print("Выход без сохранения.")
                break

            else:
                print("Введите «да» или «нет».")

        else:
            print("Нет такого пункта меню.")
if __name__ == "__main__":
            main()


