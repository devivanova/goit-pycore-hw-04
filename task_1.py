def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    salaries.append(float(salary))
                except ValueError:
                    print(f"Невірний формат рядка: {line.strip()}")

        if not salaries:
            return (0, 0)

        total = sum(salaries)
        average = total / len(salaries)
        return (total, average)

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, "
      f"Середня заробітна плата: {average}")
