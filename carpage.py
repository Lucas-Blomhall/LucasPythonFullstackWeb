import psycopg2
from psycopg2 import sql


def connect_db():
    return psycopg2.connect(host="localhost", database="carappdb",
                            user="postgres", password="Vanligt123!")


def create_car(conn, name, horse_power, price, engine_type, top_speed, zerotohundred):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO car (name, horse_power, price, engine_type, top_speed, zerotohundred) VALUES (%s, %s, %s,%s, %s, %s)", (name, horse_power, price, engine_type, top_speed, zerotohundred))
        conn.commit()


def read_cars(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM car")
        for car in cur.fetchall():
            print(car)


def update_car(conn, id, name, horse_power, price, engine_type, top_speed, zerotohundred):
    with conn.cursor() as cur:
        cur.execute("UPDATE car SET name = %s, horse_power = %s, price = %s, engine_type = %s, top_speed = %s, zerotohundred = %s WHERE id = %s",
                    (name, horse_power, price, engine_type, top_speed, zerotohundred, id))
        conn.commit()


def delete_car(conn, id):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM car WHERE id = %s", (id,))
        conn.commit()


def main():
    conn = connect_db()
    while True:
        print(
            "\n1. Add new car\n2. List all cars\n3. Update a car\n4. Delete a car\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            horse_power = input("Enter horse_power: ")
            price = input("Enter price: ")
            engine_type = input("Enter engine_type: ")
            top_speed = input("Enter top_speed: ")
            zerotohundred = input("Enter zerotohundred: ")
            create_car(conn, name, horse_power, price,
                       engine_type, top_speed, zerotohundred)
        elif choice == "2":
            read_cars(conn)
        elif choice == "3":
            id = input("Enter car ID to update: ")
            name = input("Enter name: ")
            horse_power = input("Enter horse_power: ")
            price = input("Enter price: ")
            engine_type = input("Enter engine_type: ")
            top_speed = input("Enter top_speed: ")
            zerotohundred = input("Enter zerotohundred: ")
            update_car(conn, id, name, horse_power, price,
                       engine_type, top_speed, zerotohundred)
        elif choice == "4":
            id = input("Enter car ID to delete: ")
            delete_car(conn, id)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

    conn.close()


if __name__ == "__main__":
    main()
