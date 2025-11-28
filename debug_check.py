import sys
import os

print("--- ПОЧАТОК ДІАГНОСТИКИ ---")
print(f"Поточна папка: {os.getcwd()}")

try:
    import main
    print(f"Файл main.py знайдено тут: {main.__file__}")
    
    if hasattr(main, 'calculate_exchange'):
        print("✅ УРА! Функцію calculate_exchange знайдено!")
    else:
        print("❌ Функції calculate_exchange НЕМАЄ всередині main.py.")
        print("Ось що Python бачить у файлі main.py:", dir(main))
        
except ImportError as e:
    print(f"❌ Критична помилка імпорту: {e}")

print("--- КІНЕЦЬ ---")