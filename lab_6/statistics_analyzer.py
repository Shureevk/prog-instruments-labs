import numpy as np
import math
from scipy import stats


class DataAnalyzer:
    def __init__(self):
        self.data = None
        self.n = 0

    def set_data(self, data):
        """Устанавливает данные для анализа"""
        self.data = np.array(data)
        self.n = len(self.data)

    def generate_normal_sample(self, a, sigma, n, seed=None):
        """Генерирует выборку из нормального распределения"""
        if seed is not None:
            np.random.seed(seed)
        return np.random.normal(a, sigma, n)

    def generate_f_sample(self, dfn, dfd, n, seed=None):
        """Генерирует выборку из F-распределения"""
        if seed is not None:
            np.random.seed(seed)
        return np.random.f(dfn, dfd, n)

    def calculate_sturges(self):
        """Рассчитывает число интервалов по правилу Стерджеса"""
        if self.data is None:
            raise ValueError("No data available")
        return int(math.ceil(1 + math.log2(self.n)))

    def calculate_frequencies(self, bins=None):
        """Рассчитывает абсолютные и относительные частоты"""
        if self.data is None:
            raise ValueError("No data available")

        if bins is None:
            bins = self.calculate_sturges()

        hist, bin_edges = np.histogram(self.data, bins=bins)
        abs_freq = hist.tolist()
        rel_freq = (hist / self.n).tolist()

        return abs_freq, rel_freq, bin_edges.tolist()

    def find_modal_interval(self, rel_freq, bins):
        """Находит модальный интервал"""
        max_index = np.argmax(rel_freq)
        return bins[max_index], bins[max_index + 1], rel_freq[max_index]

    def manual_statistics(self, data=None):
        """Рассчитывает статистики вручную"""
        if data is None:
            if self.data is None:
                raise ValueError("No data available")
            data = self.data
        else:
            data = np.array(data)

        n = len(data)

        # Базовые статистики
        mean = np.mean(data)
        median = np.median(data)
        min_val = np.min(data)
        max_val = np.max(data)

        # Дисперсия и стандартное отклонение
        variance = np.var(data)  # Дисперсия с n в знаменателе
        variance_corrected = np.var(data, ddof=1)  # Исправленная дисперсия (n-1)
        std_dev = np.std(data)

        # Асимметрия и эксцесс
        if n > 1 and std_dev > 0:
            # Используем scipy.stats для корректного расчета
            skewness = stats.skew(data)
            kurtosis = stats.kurtosis(data)  # Excess kurtosis (уже вычтено 3)
        else:
            skewness = 0
            kurtosis = 0

        return {
            'n': n,
            'min': float(min_val),
            'max': float(max_val),
            'mean': float(mean),
            'median': float(median),
            'variance': float(variance),
            'variance_corrected': float(variance_corrected),
            'std_dev': float(std_dev),
            'skewness': float(skewness),
            'kurtosis': float(kurtosis)
        }

    def builtin_statistics(self):
        """Возвращает статистики, рассчитанные встроенными функциями"""
        if self.data is None:
            raise ValueError("No data available")

        return {
            'mean': float(np.mean(self.data)),
            'median': float(np.median(self.data)),
            'variance': float(np.var(self.data)),
            'variance_corrected': float(np.var(self.data, ddof=1)),
            'std_dev': float(np.std(self.data)),
            'min': float(np.min(self.data)),
            'max': float(np.max(self.data))
        }