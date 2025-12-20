# -*- coding: utf-8 -*-
"""
Тесты для игры в теннис.
Тестирует все доступные реализации игры.
"""

import pytest
from tennis import (
    create_tennis_game,
    TennisGameRefactored,
    TennisGameDefactored1,
    TennisGameDefactored2,
    TennisGameDefactored3
)

from tennis_unittest import test_cases, play_game


class TestTennisRefactored:
    """Тесты для рефакторинг версии игры."""

    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score_refactored(self, p1Points, p2Points, score, p1Name, p2Name):
        """Тестирует рефакторинг версию игры."""
        game = create_tennis_game(p1Name, p2Name, "refactored")
        for i in range(max(p1Points, p2Points)):
            if i < p1Points:
                game.won_point(p1Name)
            if i < p2Points:
                game.won_point(p2Name)
        assert score == game.score()


class TestTennisVersion1:
    """Тесты для первой версии игры."""

    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score_v1(self, p1Points, p2Points, score, p1Name, p2Name):
        """Тестирует первую версию игры."""
        game = create_tennis_game(p1Name, p2Name, "v1")
        for i in range(max(p1Points, p2Points)):
            if i < p1Points:
                game.won_point(p1Name)
            if i < p2Points:
                game.won_point(p2Name)
        assert score == game.score()


class TestTennisVersion2:
    """Тесты для второй версии игры."""

    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score_v2(self, p1Points, p2Points, score, p1Name, p2Name):
        """Тестирует вторую версию игры."""
        game = create_tennis_game(p1Name, p2Name, "v2")
        for i in range(max(p1Points, p2Points)):
            if i < p1Points:
                game.won_point(p1Name)
            if i < p2Points:
                game.won_point(p2Name)
        assert score == game.score()


class TestTennisVersion3:
    """Тесты для третьей версии игры."""

    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score_v3(self, p1Points, p2Points, score, p1Name, p2Name):
        """Тестирует третью версию игры."""
        game = create_tennis_game(p1Name, p2Name, "v3")
        for i in range(max(p1Points, p2Points)):
            if i < p1Points:
                game.won_point(p1Name)
            if i < p2Points:
                game.won_point(p2Name)
        assert score == game.score()


class TestTennisFactory:
    """Тесты фабричного метода."""

    def test_create_refactored_game(self):
        """Тестирует создание рефакторинг версии."""
        game = create_tennis_game("Player1", "Player2", "refactored")
        assert isinstance(game, TennisGameRefactored)

    def test_create_v1_game(self):
        """Тестирует создание первой версии."""
        game = create_tennis_game("Player1", "Player2", "v1")
        assert isinstance(game, TennisGameDefactored1)

    def test_create_v2_game(self):
        """Тестирует создание второй версии."""
        game = create_tennis_game("Player1", "Player2", "v2")
        assert isinstance(game, TennisGameDefactored2)

    def test_create_v3_game(self):
        """Тестирует создание третьей версии."""
        game = create_tennis_game("Player1", "Player2", "v3")
        assert isinstance(game, TennisGameDefactored3)

    def test_create_default_game(self):
        """Тестирует создание игры по умолчанию."""
        game = create_tennis_game("Player1", "Player2")
        assert isinstance(game, TennisGameRefactored)

    def test_invalid_implementation(self):
        """Тестирует обработку неверной реализации."""
        with pytest.raises(ValueError):
            create_tennis_game("Player1", "Player2", "invalid")


# Сохранение обратной совместимости для существующих тестов
class TestTennis:

    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score(self, p1Points, p2Points, score, p1Name, p2Name):
        game = play_game(p1Points, p2Points, p1Name, p2Name)
        assert score == game.score()