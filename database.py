# database.py
import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, db_file='tornadolab.db'):
        self.db_file = db_file
        self._init_db()
        self._add_sample_data()  # Раскомментируйте для добавления тестовых данных

    def _create_connection(self):
        """Создать соединение с базой данных"""
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            conn.row_factory = sqlite3.Row  # Для доступа к полям по имени
            return conn
        except Error as e:
            print(f"Ошибка подключения к SQLite: {e}")
        return conn

    def _init_db(self):
        """Инициализация таблиц"""
        conn = self._create_connection()
        if conn is not None:
            try:
                cursor = conn.cursor()

                # Таблица пользователей
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT,
                        full_name TEXT,
                        registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')

                # Таблица товаров
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS products (
                        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        description TEXT,
                        price REAL,
                        quantity INTEGER,
                        category TEXT,
                        image_url TEXT
                    )
                ''')

                # Таблица заказов
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS orders (
                        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        product_id INTEGER,
                        quantity INTEGER,
                        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        status TEXT DEFAULT 'pending',
                        FOREIGN KEY (user_id) REFERENCES users (user_id),
                        FOREIGN KEY (product_id) REFERENCES products (product_id)
                    )
                ''')

                conn.commit()
                print("Таблицы успешно созданы")
            except Error as e:
                print(f"Ошибка при создании таблиц: {e}")
            finally:
                conn.close()

    def _add_sample_data(self):
        """Добавление тестовых данных (вызывается один раз)"""
        sample_products = [
            {
                "name": "Офисный стул",
                "description": "Эргономичный стул с регулируемой высотой",
                "price": 4500.00,
                "quantity": 15,
                "category": "office",
                "image_url": "https://example.com/office_chair.jpg"
            },
            {
                "name": "Компьютерный стол",
                "description": "Просторный стол для работы за компьютером",
                "price": 8900.00,
                "quantity": 8,
                "category": "office",
                "image_url": "https://example.com/desk.jpg"
            }
        ]

        if not self.get_products():
            for product in sample_products:
                self.add_product(**product)
            print("Тестовые данные добавлены")

    def _add_sample_data(self):
        """Добавление тестовых данных (мебели для офиса и химической мебели)"""
        sample_products = [
            # Офисная мебель
            {
                "name": "Офисный стул 'Комфорт'",
                "description": "Эргономичный стул с регулируемой высотой и подлокотниками",
                "price": 6500.00,
                "quantity": 12,
                "category": "office",
                "image_url": "https://example.com/office_chair_comfort.jpg"
            },
            {
                "name": "Рабочий стол 'Престиж'",
                "description": "Просторный стол с ящиками и cable management",
                "price": 12500.00,
                "quantity": 8,
                "category": "office",
                "image_url": "https://example.com/office_desk_prestige.jpg"
            },
            {
                "name": "Офисный диван 'Мини'",
                "description": "Компактный диван для зоны отдыха в офисе",
                "price": 18900.00,
                "quantity": 5,
                "category": "office",
                "image_url": "https://example.com/office_sofa_mini.jpg"
            },

            # Химическая мебель
            {
                "name": "Лабораторный стол с мойкой",
                "description": "Стол из химически стойкого материала со встроенной мойкой",
                "price": 32400.00,
                "quantity": 6,
                "category": "chemical",
                "image_url": "https://example.com/lab_table_sink.jpg"
            },
            {
                "name": "Вытяжной шкаф 120см",
                "description": "Шкаф для работы с агрессивными химическими веществами",
                "price": 87500.00,
                "quantity": 3,
                "category": "chemical",
                "image_url": "https://example.com/fume_hood_120.jpg"
            },
            {
                "name": "Лабораторный стул",
                "description": "Стул с устойчивым к химикатам покрытием",
                "price": 9200.00,
                "quantity": 7,
                "category": "chemical",
                "image_url": "https://example.com/lab_chair.jpg"
            },

            # Индивидуальные заказы
            {
                "name": "Индивидуальный мебельный проект",
                "description": "Разработка и производство мебели по вашим чертежам",
                "price": 0.00,  # Цена определяется после консультации
                "quantity": 999,  # Условное большое количество
                "category": "custom",
                "image_url": "https://example.com/custom_project.jpg"
            }
        ]

        # Добавляем только если таблица товаров пуста
        if not self.get_products():
            for product in sample_products:
                self.add_product(**product)
            print("Добавлены тестовые товары")

    # Методы для работы с пользователями
    def add_user(self, user_id, username=None, full_name=None):
        conn = self._create_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR IGNORE INTO users (user_id, username, full_name)
                VALUES (?, ?, ?)
            ''', (user_id, username, full_name))
            conn.commit()
        except Error as e:
            print(f"Ошибка при добавлении пользователя: {e}")
        finally:
            conn.close()

    # Методы для работы с товарами
    def add_product(self, name, description, price, quantity, category, image_url):
        conn = self._create_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO products (name, description, price, quantity, category, image_url)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, description, price, quantity, category, image_url))
            conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Ошибка при добавлении товара: {e}")
        finally:
            conn.close()

    def get_products(self, category=None):
        conn = self._create_connection()
        try:
            cursor = conn.cursor()
            if category:
                cursor.execute('SELECT * FROM products WHERE category = ?', (category,))
            else:
                cursor.execute('SELECT * FROM products')
            return cursor.fetchall()
        except Error as e:
            print(f"Ошибка при получении товаров: {e}")
        finally:
            conn.close()

    # Методы для работы с заказами
    def create_order(self, user_id, product_id, quantity):
        conn = self._create_connection()
        try:
            cursor = conn.cursor()

            cursor.execute('SELECT quantity FROM products WHERE product_id = ?', (product_id,))
            result = cursor.fetchone()

            if result and result['quantity'] >= quantity:
                cursor.execute('''
                    INSERT INTO orders (user_id, product_id, quantity)
                    VALUES (?, ?, ?)
                ''', (user_id, product_id, quantity))

                cursor.execute('''
                    UPDATE products 
                    SET quantity = quantity - ?
                    WHERE product_id = ?
                ''', (quantity, product_id))

                conn.commit()
                return True
            return False
        except Error as e:
            print(f"Ошибка при создании заказа: {e}")
        finally:
            conn.close()

    def get_user_orders(self, user_id):
        conn = self._create_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT o.order_id, p.name, o.quantity, p.price, o.order_date, o.status
                FROM orders o
                JOIN products p ON o.product_id = p.product_id
                WHERE o.user_id = ?
                ORDER BY o.order_date DESC
            ''', (user_id,))
            return cursor.fetchall()
        except Error as e:
            print(f"Ошибка при получении заказов: {e}")
        finally:
            conn.close()