import pytest
import numpy as np
from unittest.mock import patch
from statistics_analyzer import DataAnalyzer


def test_initialization():
    """Тест инициализации анализатора"""
    analyzer = DataAnalyzer()
    assert analyzer.data is None
    assert analyzer.n == 0


def test_set_data():
    """Тест установки данных"""
    analyzer = DataAnalyzer()
    test_data = np.array([1, 2, 3])
    analyzer.set_data(test_data)
    assert np.array_equal(analyzer.data, test_data)
    assert analyzer.n == 3


def test_calculate_sturges():
    """Тест правила Стерджеса"""
    analyzer = DataAnalyzer()
    analyzer.set_data(np.array([1, 2, 3, 4, 5]))
    assert analyzer.calculate_sturges() == 4


def test_find_modal_interval():
    """Тест нахождения модального интервала"""
    analyzer = DataAnalyzer()
    rel_freq = [0.1, 0.3, 0.05, 0.4, 0.15]
    bins = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    left, right, freq = analyzer.find_modal_interval(rel_freq, bins)
    assert left == 3.0
    assert right == 4.0
    assert freq == 0.4


def test_manual_statistics_basic():
    """Тест статистик (базовый)"""
    analyzer = DataAnalyzer()
    data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    analyzer.set_data(data)
    stats = analyzer.manual_statistics()
    assert stats['mean'] == 3.0
    assert stats['variance'] == 2.0


@pytest.mark.parametrize("data,expected_mean,expected_variance", [
    (np.array([1, 2, 3, 4, 5]), 3.0, 2.0),
    (np.array([10, 20, 30]), 20.0, 66.66666666666667),
    (np.array([5, 5, 5]), 5.0, 0.0),
])
def test_manual_statistics_parametrized(data, expected_mean, expected_variance):
    """Параметризованный тест для разных наборов данных"""
    analyzer = DataAnalyzer()
    analyzer.set_data(data)
    stats = analyzer.manual_statistics()
    assert stats['mean'] == pytest.approx(expected_mean, rel=1e-10)
    assert stats['variance'] == pytest.approx(expected_variance, rel=1e-10)


def test_generate_f_sample_with_mocks():
    """Тест с моками для F-распределения"""
    analyzer = DataAnalyzer()
    mock_f_data = np.array([1.5, 2.5, 3.5])

    with patch('numpy.random.f') as mock_f:
        mock_f.return_value = mock_f_data
        with patch('numpy.random.seed') as mock_seed:
            result = analyzer.generate_f_sample(dfn=5, dfd=10, n=3, seed=42)
            mock_seed.assert_called_once_with(42)
            mock_f.assert_called_once_with(5, 10, 3)
            assert np.array_equal(result, mock_f_data)


def test_builtin_vs_manual_statistics():
    """Тест сравнения ручной и встроенной статистики"""
    analyzer = DataAnalyzer()
    data = np.random.normal(0, 1, 100)
    analyzer.set_data(data)
    manual_stats = analyzer.manual_statistics()
    builtin_stats = analyzer.builtin_statistics()
    assert manual_stats['mean'] == pytest.approx(builtin_stats['mean'], rel=1e-10)
    assert manual_stats['variance'] == pytest.approx(builtin_stats['variance'], rel=1e-10)


def test_calculate_frequencies():
    """Тест частот"""
    analyzer = DataAnalyzer()
    data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    analyzer.set_data(data)
    abs_freq, rel_freq, bins = analyzer.calculate_frequencies()
    assert np.sum(abs_freq) == len(data)
    assert np.sum(rel_freq) == pytest.approx(1.0, rel=1e-10)


def test_with_invalid_data():
    """Тест обработки ошибок"""
    analyzer = DataAnalyzer()
    with pytest.raises(ValueError):
        analyzer.calculate_frequencies()


# Дополнительные тесты для полного покрытия
def test_generate_normal_sample():
    """Тест генерации нормального распределения"""
    analyzer = DataAnalyzer()
    sample = analyzer.generate_normal_sample(a=10, sigma=2, n=100, seed=42)
    assert len(sample) == 100
    sample2 = analyzer.generate_normal_sample(a=10, sigma=2, n=100, seed=42)
    assert np.array_equal(sample, sample2)


def test_calculate_frequencies_with_bins():
    """Тест расчета частот с заданным числом интервалов"""
    analyzer = DataAnalyzer()
    data = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
    analyzer.set_data(data)
    abs_freq, rel_freq, bins = analyzer.calculate_frequencies(bins=3)
    assert len(bins) == 4
    assert len(abs_freq) == 3
    assert sum(abs_freq) == 10