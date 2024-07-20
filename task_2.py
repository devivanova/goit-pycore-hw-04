def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 3:
                        cat_id, name, age = parts
                        cat_info = {
                            "id": cat_id,
                            "name": name,
                            "age": age
                        }
                        cats_info.append(cat_info)
                    else:
                        print(f"Некоректний рядок: {line}")

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")

    return cats_info


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
