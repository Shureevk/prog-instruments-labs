import numpy as np
from statistics_analyzer import DataAnalyzer


def main():
    """Основная функция для демонстрации работы модуля"""

    # Параметры
    a = 3
    sigma = 4
    n = 109

    # Создаем анализатор
    analyzer = DataAnalyzer()

    # Генерация выборки
    print("1. Генерация выборки из нормального распределения...")
    X = analyzer.generate_normal_sample(a, sigma, n, seed=42)
    analyzer.set_data(X)

    # Правило Стерджеса
    print(f"\n2. Число интервалов по правилу Стерджеса: {analyzer.calculate_sturges()}")

    # Расчет частот
    abs_freq, rel_freq, bins = analyzer.calculate_frequencies()

    print("\n3. Абсолютные частоты:")
    for i in range(len(abs_freq)):
        print(f"  [{bins[i]:.2f}, {bins[i + 1]:.2f}): {abs_freq[i]}")

    print(f"\n4. Сумма абсолютных частот: {np.sum(abs_freq)}")
    print(f"   Сумма относительных частот: {np.sum(rel_freq):.4f}")

    # Модальный интервал
    left, right, freq = analyzer.find_modal_interval(rel_freq, bins)
    print(f"\n5. Модальный интервал: [{left:.2f}, {right:.2f})")
    print(f"   Относительная частота: {freq:.4f}")

    # Статистики
    print("\n6. Статистические характеристики:")
    manual_stats = analyzer.manual_statistics()
    builtin_stats = analyzer.builtin_statistics()

    print("\n   Сравнение оценок:")
    for key in ['mean', 'median', 'variance', 'variance_corrected']:
        if key in manual_stats and key in builtin_stats:
            print(f"   {key:20}: {manual_stats[key]:.6f} | {builtin_stats[key]:.6f}")

    # F-распределение
    print("\n7. Генерация выборки из F-распределения...")
    Y = analyzer.generate_f_sample(5, 10, n, seed=42)
    analyzer.set_data(Y)

    f_stats = analyzer.manual_statistics()
    print(f"   Статистики F-распределения:")
    print(f"   Среднее: {f_stats['mean']:.4f}")
    print(f"   Дисперсия: {f_stats['variance']:.4f}")
    print(f"   Асимметрия: {f_stats['skewness']:.4f}")

    # Большая выборка
    print("\n8. Анализ большой выборки (n=6540)...")
    X_large = analyzer.generate_normal_sample(a, sigma, n * 60, seed=42)
    large_stats = analyzer.manual_statistics(X_large)

    print(f"   Среднее: {large_stats['mean']:.6f} (теоретическое: {a})")
    print(f"   Дисперсия: {large_stats['variance']:.6f} (теоретическое: {sigma ** 2})")

    print("\nАнализ завершен!")


if __name__ == "__main__":
    main()