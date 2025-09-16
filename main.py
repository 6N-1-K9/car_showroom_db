import psycopg2
from config import host, user, password, db_name

def crud():
    print("|Выберите действие CRUD или аналитический запрос                                                        |")
    print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
    print("|1 - добавить данные в таблицу                                                                          |")
    print("|2 - получить данные из таблицы                                                                         |")
    print("|3 - редактировать данные из таблицы                                                                    |")
    print("|4 - удалить данные из таблицы                                                                          |")
    print("|5 - аналитический запрос по таблице                                                                    |")
    print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")

print("░█████╗░░█████╗░██████╗░░░░░░░░░░██████╗██╗░░██╗░█████╗░░██╗░░░░░░░██╗██████╗░░█████╗░░█████╗░███╗░░░███╗")
print("██╔══██╗██╔══██╗██╔══██╗░░░░░░░░██╔════╝██║░░██║██╔══██╗░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗████╗░████║")
print("██║░░╚═╝███████║██████╔╝░░░░░░░░╚█████╗░███████║██║░░██║░╚██╗████╗██╔╝██████╔╝██║░░██║██║░░██║██╔████╔██║")
print("██║░░██╗██╔══██║██╔══██╗░░░░░░░░░╚═══██╗██╔══██║██║░░██║░░████╔═████║░██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║")
print("╚█████╔╝██║░░██║██║░░██║░░░░░░░░██████╔╝██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░██║░░██║╚█████╔╝╚█████╔╝██║░╚═╝░██║")
print("░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░░░╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░░░░░░░░░░░░██╗░░░██╗███████╗██████╗░░░░░░░░░░░███╗░░░░░░█████╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░░░░░░░░░░░░██║░░░██║██╔════╝██╔══██╗░░░░░░░░░████║░░░░░██╔══██╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░░░░░░░░░░░░╚██╗░██╔╝█████╗░░██████╔╝░░░░░░░░██╔██║░░░░░██║░░██║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░░░░░░░░░░░░░╚████╔╝░██╔══╝░░██╔══██╗░░░░░░░░╚═╝██║░░░░░██║░░██║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░╚██╔╝░░███████╗██║░░██║░░░░░░░░███████╗██╗╚█████╔╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░░░░░░╚══════╝╚═╝░╚════╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")

def crud_action(crud_num, table_name):
    # добавление данных в табцу
    if crud_num == 1:
        if table_name == "car":
            print("|Вам сначала необходимо заполнить mileage и gearbox                                                     |")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")

            # сначала введем mileage
            print("|Введите (mileae(int))                                                                                  |")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            with connection.cursor() as cursor:
                insert_data = (input())
                insert_query = f"INSERT INTO mileage(mileage) VALUES {insert_data};"
                cursor.execute(insert_query)
                connection.commit()

            # теперь введем gearbox
            with connection.cursor() as cursor:
                print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
                print("|Введите '(mechanics(bool)', 'automatic(bool)', 'variable(bool)', 'robot(bool)')                        |")
                print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
                insert_data = (input())
                insert_query = f"INSERT INTO gearbox(mechanics, automatic, variable, robot) VALUES {insert_data};"
                cursor.execute(insert_query)
                connection.commit()

            # алелуя, мы можем внести машинку
            with connection.cursor() as cursor:
                print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
                print("|Введите '(brand(str)', 'provider(str)', 'year_of_issue(str)', 'guarantee(str)')                        |")
                print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
                insert_data = (input())
                insert_query = f"INSERT INTO car(brand, provider, year_of_issue, guarantee) VALUES {insert_data};"
                cursor.execute(insert_query)
                connection.commit()

        # вводим mileage
        elif table_name == "mileage":
            print("|Введите (mileae(int))                                                                                  |")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            with connection.cursor() as cursor:
                insert_data = (input())
                insert_query = f"INSERT INTO mileage(mileage) VALUES {insert_data};"
                cursor.execute(insert_query)
                connection.commit()

        # вводим gearbox
        elif table_name == "gearbox":
            with connection.cursor() as cursor:
                print("|Введите '(mechanics(str)', 'automatic(str)', 'variable(str)', 'robot(str)')                            |")
                print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
                insert_data = (input())
                insert_query = f"INSERT INTO gearbox(mechanics, automatic, variable, robot) VALUES {insert_data};"
                cursor.execute(insert_query)
                connection.commit()

    # вывод данных
    elif crud_num == 2:
        print("|Что вы хотите вывести?                                                                                 |")
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
        print("|1 - вывод строки с определенным id                                                                     |")
        print("|2 - вывод всех строк                                                                                   |")
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
        read_num = int(input())
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
        # вывод с определенным индексом
        if read_num == 1:
            if table_name == "car":
                print("|Введите интересующий вас id:                                                                           |")
                print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
                table_id = int(input())
                print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
                with connection.cursor() as cursor:
                    select_all_rows = f"SELECT * FROM car where id_car = {table_id};"
                    cursor.execute(select_all_rows)
                    rows = cursor.fetchall()
                    for row in rows:
                        print(row)
                    print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            elif table_name == "mileage":
                print("|Введите интересующий вас id:                                                                           |")
                print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
                table_id = int(input())
                print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
                with connection.cursor() as cursor:
                    select_all_rows = f"SELECT * FROM mileage where id_mileage = {table_id};"
                    cursor.execute(select_all_rows)
                    rows = cursor.fetchall()
                    for row in rows:
                        print(row)
                    print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            elif table_name == "gearbox":
                print("|Введите интересующий вас id:                                                                           |")
                print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
                table_id = int(input())
                print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
                with connection.cursor() as cursor:
                    select_all_rows = f"SELECT * FROM gearbox where id_gearbox = {table_id};"
                    cursor.execute(select_all_rows)
                    rows = cursor.fetchall()
                    for row in rows:
                        print(row)
                    print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")

        # вывод всех строк
        elif read_num == 2:
            if table_name == "car":
                with connection.cursor() as cursor:
                    #select_all_rows = f"SELECT * FROM car order by id_car desc;"
                    select_all_rows = f"SELECT brand, provider, year_of_issue, guarantee FROM car order by id_car desc;"
                    cursor.execute(select_all_rows)
                    rows = cursor.fetchall()
                    for row in rows:
                        print(row)
                        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
                    #print("#" * 20)
            elif table_name == "mileage":
                with connection.cursor() as cursor:
                    select_all_rows = f"SELECT mileage FROM mileage order by id_mileage desc;"
                    #select_all_rows = f"SELECT brand, provider, year_of_issue, guarantee FROM car order by id_car desc limit 10;"
                    cursor.execute(select_all_rows)
                    rows = cursor.fetchall()
                    for row in rows:
                        print(row)
                        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            elif table_name == "gearbox":
                with connection.cursor() as cursor:
                    select_all_rows = f"SELECT mechanics, automatic, variable, robot FROM gearbox order by id_gearbox desc;"
                    #select_all_rows = f"SELECT brand, provider, year_of_issue, guarantee FROM car order by id_car desc limit 10;"
                    cursor.execute(select_all_rows)
                    rows = cursor.fetchall()
                    for row in rows:
                        print(row)
                        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")

    # редактирование данных
    # делаем апдейт по айдишнику
    elif crud_num == 3:
        print("|Введите интересующий вас id:                                                                           |")
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")

        table_id = int(input())
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")

        if table_name == "car":
            print("|Введите новое значени brand:                                                                           |")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            new_brand = str(input())
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            print("|Введите новое значени provider:                                                                        |")
            new_provider = str(input())
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            print("|Введите новое значени year_of_issue:                                                                   |")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            new_year_of_issue = str(input())
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            print("|Введите новое значени guarantee:                                                                       |")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            new_guarantee = str(input())
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")

            with connection.cursor() as cursor:
                update_qu = f"UPDATE {table_name} SET brand = {new_brand}, provider = {new_provider}, year_of_issue = {new_year_of_issue}, guarantee = {new_guarantee} WHERE id_car = {table_id};"
                cursor.execute(update_qu)
                connection.commit()

        elif table_name == "mileage":
            print("|Введите новое значение mileage:                                                                        |")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            new_mileage = str(input())
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            with connection.cursor() as cursor:
                update_qu = f"UPDATE {table_name} SET mileage = {new_mileage} WHERE id_mileage = {table_id};"
                cursor.execute(update_qu)
                connection.commit()

        elif table_name == "gearbox":
            print("|Введите новое значени mechanics:                                                                       |")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            new_mechanics = str(input())
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            print("|Введите новое значени automatic:                                                                       |")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            new_automatic = str(input())
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            print("|Введите новое значени variable:                                                                        |")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            new_variable = str(input())
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            print("|Введите новое значени robot:                                                                           |")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            new_robot = str(input())
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")

            with connection.cursor() as cursor:
                update_qu = f"UPDATE {table_name} SET mechanics = {new_mechanics}, automatic = {new_automatic}, variable = {new_variable}, robot = {new_robot} WHERE id_gearbox = {table_id};"
                cursor.execute(update_qu)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                connection.commit()

    # удаление данных
    elif crud_num == 4:
        print("|Введитe интересующий вас id:                                                                           |")
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
        table_id = int(input())
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
        # удаоение машины из car
        if table_name == "car":
            # удаляем машину
            with connection.cursor() as cursor:
                delete_query = f"DELETE FROM car WHERE id_car = {table_id};"
                cursor.execute(delete_query)
                connection.commit()

            # удаляем ее пробег из mileage
            with connection.cursor() as cursor:
                delete_query = f"DELETE FROM mileage WHERE id_mileage = {table_id};"
                cursor.execute(delete_query)
                connection.commit()

            # удаляем ее КПП из gearbox
            with connection.cursor() as cursor:
                delete_query = f"DELETE FROM gearbox WHERE id_gearbox = {table_id};"
                cursor.execute(delete_query)
                connection.commit()
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
        # удаление пробега из mileage
        elif table_name == "mileage":
            with connection.cursor() as cursor:
                delete_query = f"DELETE FROM mileage WHERE id_mileage = {table_id};"
                cursor.execute(delete_query)
                connection.commit()
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")

        # удаение КПП из gearbox
        with connection.cursor() as cursor:
            delete_query = f"DELETE FROM gearbox WHERE id_gearbox = {table_id};"
            cursor.execute(delete_query)
            connection.commit()
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")

    # аналитические запросы
    elif crud_num == 5:
        # вывод количества машин определенной марки
        if table_name == "car":
            print("|Аналитический запрос для подсчета машин определенной макри                                             |")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            print("|Введите интересующую вас марку:                                                                        |")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            car_name = str(input())
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            with connection.cursor() as cursor:
                analitic_query = f"SELECT kolvo_brand {car_name};"
                cursor.execute(analitic_query)
                connection.commit()
                rows = cursor.fetchall()
                print(rows)
                print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")


        # вывод разности максимального и минимального пробега
        elif table_name == "mileage":
            print("|Аналитический запрос для вывода разности максимального и минимального пробеа                           |")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            with connection.cursor() as cursor:
                analitic_query = f"SELECT mileage_maxmin();"
                cursor.execute(analitic_query)
                connection.commit()
                rows = cursor.fetchall()
                print(rows)
                print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")

        # подсчет количества каждого типа КПП из mileage
        elif table_name == "gearbox":
            print("|Аналитический запрос подсчета количества КПП (механика, автомат, вариатор и робот)                     |")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
            with connection.cursor() as cursor:
                analitic_query = f"SELECT SUM(CASE WHEN mechanics = 't' THEN 1 ELSE 0 END) AS mechanics_count,SUM(CASE WHEN automatic = 't' THEN 1 ELSE 0 END) AS automatic_count,SUM(CASE WHEN variable = 't' THEN 1 ELSE 0 END) AS variable_count,SUM(CASE WHEN robot = 't' THEN 1 ELSE 0 END) AS robot_count FROM gearbox;"
                cursor.execute(analitic_query)
                connection.commit()
                rows = cursor.fetchall()
                print(rows)
                print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

# выбор таблицы
    print('|Выберите таблицу для дальнейшей работы:                                                                |')
    print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
    print("|1 - таблица car (таблица машин)                                                                        |")
    print("|2 - таблица mileage (таблица пробега)                                                                  |")
    print("|3 - таблица gearbox (таблица КПП)                                                                      |")
    print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")

    table_num = int(input())

    if table_num == 1:
        table_name = 'car'
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
        print("|Вы выбрали таблицу car                                                                                 |")
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
        crud()
        crud_num = int(input())
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
        crud_action(crud_num, table_name)
    elif table_num == 2:
        table_name = 'mileage'
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
        print("|Вы выбрали таблицу mileage                                                                             |")
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
        crud()
        crud_num = int(input())
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
        crud_action(crud_num, table_name)
    elif table_num == 3:
        table_name = 'gearbox'
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
        print("|Вы выбрали таблицу gearbox                                                                             |")
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
        crud()
        crud_num = int(input())
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————")
        crud_action(crud_num, table_name)

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")