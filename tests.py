import unittest
# Імпортуємо нашу функцію розрахунку з головного файлу
from main import calculate_exchange

# --- ЧАСТИНА 1: Тести через assert (Пункт 1 завдання) ---
def run_assert_tests():
    print("Запуск тестів assert...")
    # Тест 1: Перевірка звичайного множення
    assert calculate_exchange(100, 41.5) == 4150.0, "Помилка в тесті 1"
    
    # Тест 2: Перевірка множення на нуль
    assert calculate_exchange(0, 41.5) == 0, "Помилка при множенні на 0"
    
    # Тест 3: Перевірка малих чисел
    assert calculate_exchange(1, 1) == 1, "Помилка при множенні 1 на 1"
    
    print("Всі тести assert пройшли успішно!\n")

# --- ЧАСТИНА 2: Тести через unittest (Пункт 2 завдання) ---
class TestCurrencyConverter(unittest.TestCase):
    
    def test_usd_calculation(self):
        """Перевірка коректності розрахунку для USD"""
        result = calculate_exchange(100, 41.50)
        self.assertEqual(result, 4150.0)

    def test_float_precision(self):
        """Перевірка роботи з дробовими числами"""
        result = calculate_exchange(10.5, 2)
        self.assertEqual(result, 21.0)

    def test_zero_amount(self):
        """Перевірка, що 0 грошей дає 0 результату"""
        result = calculate_exchange(0, 40.0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    # Спочатку запускаємо assert
    run_assert_tests()
    # Потім запускаємо unittest
    unittest.main()