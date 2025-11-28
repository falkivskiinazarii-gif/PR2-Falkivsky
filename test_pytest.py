import pytest
from main import calculate_exchange

# 1. FIXTURE (Фікстура - підготовка даних)
@pytest.fixture
def base_rate():
    return 41.5

# 2. PARAMETRIZE (Параметризація - багато тестів в одному)
@pytest.mark.parametrize("input_amount, rate, expected", [
    (100, 41.5, 4150.0),
    (10, 10.0, 100.0),
    (0, 50.0, 0.0)
])
def test_calculator_param(input_amount, rate, expected):
    assert calculate_exchange(input_amount, rate) == expected

# 3. RAISES (Перевірка на помилку)
def test_error_handling():
    with pytest.raises(TypeError):
        calculate_exchange(100, None)

# 4. SKIP (Пропуск тесту)
@pytest.mark.skip(reason="Цей тест тимчасово вимкнено")
def test_skipped_feature():
    assert 1 == 0

# 5. XFAIL (Очікувана невдача)
@pytest.mark.xfail(reason="Відомий баг: функція поки не підтримує від'ємні числа")
def test_negative_numbers():
    # Припустимо, ми хочемо, щоб це працювало, але поки що воно падає
    assert calculate_exchange(-100, 41.5) == "Error"
def test_fake_fail():
    print("Це спеціальна помилка для звіту")
    assert 2 + 2 == 5