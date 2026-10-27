import cases
import storage


def main():
    items = [{"id": 1, "title": "Вход в систему", "status": "pending"},{"id": 4, "title": "Открытие расписания", "status": "pass"},{"id": 7, "title": "Сохранение профиля", "status": "fail"}]

    print("1. Проверка списка:", cases.valid_cases(items))
    print("2. Пустой список:", cases.valid_cases([]))

    print("3. Добавление проверки:",cases.add_case(items, "Новый тест"))

    print("4. Изменение статуса:",cases.set_result(items, 1, "pass"))

    print("5. Повторный статус:",cases.set_result(items, 1, "pass"))

    print("6. Несуществующий ID:",cases.set_result(items, 99, "fail"))

    print("7. Неправильный статус:",cases.set_result(items, 1, "hello"))

    print("8. Сводка:", cases.summarize(items))

    print("9. Загрузка отсутствующего файла:",storage.load_cases("missing.json"))

    print("10. Сохранение файла:",storage.save_cases("check-cases.json", items))


if __name__ == "__main__":
    main()