# -*- coding: utf-8 -*-
"""
Модуль для игры в теннис.
Содержит несколько реализаций класса TennisGame с разными подходами.
"""

from typing import Dict, Any


class TennisGameDefactored1:
    """
    Первая версия реализации игры в теннис.
    Использует словари для хранения соответствий счета.
    """

    def __init__(self, player1_name: str, player2_name: str) -> None:
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name: str) -> None:
        """Добавляет очко указанному игроку."""
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score(self) -> str:
        """Возвращает текущий счет игры в строковом формате."""
        if self.player1_score == self.player2_score:
            return self._get_tie_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self._get_end_game_score()
        else:
            return self._get_ongoing_game_score()

    def _get_tie_score(self) -> str:
        """Возвращает счет при равных очках."""
        tie_scores = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
            3: "Forty-All",
        }
        return tie_scores.get(self.player1_score, "Deuce")

    def _get_end_game_score(self) -> str:
        """Возвращает счет при преимуществе или победе."""
        score_difference = self.player1_score - self.player2_score

        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _get_ongoing_game_score(self) -> str:
        """Возвращает счет обычной игры (до 40-40)."""
        score_names = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }
        player1_score_name = score_names[self.player1_score]
        player2_score_name = score_names[self.player2_score]
        return f"{player1_score_name}-{player2_score_name}"


class TennisGameDefactored2:
    """
    Вторая версия реализации игры в теннис.
    Использует множество условных операторов.
    """

    def __init__(self, player1_name: str, player2_name: str) -> None:
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name: str) -> None:
        """Добавляет очко указанному игроку."""
        if player_name == self.player1_name:
            self._increment_player1_score()
        else:
            self._increment_player2_score()

    def score(self) -> str:
        """Возвращает текущий счет игры в строковом формате."""
        result = ""

        if self._is_tie() and self.player1_score < 4:
            result = self._get_tie_score_name()
            result += "-All"
        if self._is_tie() and self.player1_score >= 3:
            result = "Deuce"

        player1_score_name = self._get_player_score_name(self.player1_score)
        player2_score_name = self._get_player_score_name(self.player2_score)

        if self.player1_score > 0 and self.player2_score == 0:
            result = f"{player1_score_name}-Love"
        if self.player2_score > 0 and self.player1_score == 0:
            result = f"Love-{player2_score_name}"

        if (self.player1_score > self.player2_score and
                self.player1_score < 4 and self.player2_score >= 1):
            result = f"{player1_score_name}-{player2_score_name}"
        if (self.player2_score > self.player1_score and
                self.player2_score < 4 and self.player1_score >= 1):
            result = f"{player1_score_name}-{player2_score_name}"

        if (self.player1_score > self.player2_score and
                self.player2_score >= 3):
            result = f"Advantage {self.player1_name}"
        if (self.player2_score > self.player1_score and
                self.player1_score >= 3):
            result = f"Advantage {self.player2_name}"

        if (self.player1_score >= 4 and self.player2_score >= 0 and
                (self.player1_score - self.player2_score) >= 2):
            result = f"Win for {self.player1_name}"
        if (self.player2_score >= 4 and self.player1_score >= 0 and
                (self.player2_score - self.player1_score) >= 2):
            result = f"Win for {self.player2_name}"

        return result

    def _is_tie(self) -> bool:
        """Проверяет, равны ли очки игроков."""
        return self.player1_score == self.player2_score

    def _get_tie_score_name(self) -> str:
        """Возвращает название счета при ничьей."""
        if self.player1_score == 0:
            return "Love"
        elif self.player1_score == 1:
            return "Fifteen"
        elif self.player1_score == 2:
            return "Thirty"
        else:
            return "Forty"

    def _get_player_score_name(self, score: int) -> str:
        """Возвращает название счета для указанного количества очков."""
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        else:
            return "Forty"

    def _increment_player1_score(self) -> None:
        """Увеличивает счет первого игрока на 1."""
        self.player1_score += 1

    def _increment_player2_score(self) -> None:
        """Увеличивает счет второго игрока на 1."""
        self.player2_score += 1


class TennisGameDefactored3:
    """
    Третья версия реализации игры в теннис.
    Самая компактная реализация.
    """

    def __init__(self, player1_name: str, player2_name: str) -> None:
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name: str) -> None:
        """Добавляет очко указанному игроку."""
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score(self) -> str:
        """Возвращает текущий счет игры в строковом формате."""
        if self._is_regular_game():
            return self._get_regular_score()
        else:
            return self._get_end_game_score()

    def _is_regular_game(self) -> bool:
        """Проверяет, является ли игра обычной (без преимущества)."""
        return self.player1_score < 4 and self.player2_score < 4

    def _get_regular_score(self) -> str:
        """Возвращает счет обычной игры."""
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        player1_score_name = score_names[self.player1_score]

        if self.player1_score == self.player2_score:
            return f"{player1_score_name}-All"
        else:
            player2_score_name = score_names[self.player2_score]
            return f"{player1_score_name}-{player2_score_name}"

    def _get_end_game_score(self) -> str:
        """Возвращает счет при преимуществе или победе."""
        if self.player1_score == self.player2_score:
            return "Deuce"

        leading_player = (self.player1_name if self.player1_score > self.player2_score
                          else self.player2_name)
        score_difference = abs(self.player1_score - self.player2_score)

        if score_difference == 1:
            return f"Advantage {leading_player}"
        else:
            return f"Win for {leading_player}"


# Константы для обозначения счета
LOVE = "Love"
FIFTEEN = "Fifteen"
THIRTY = "Thirty"
FORTY = "Forty"
DEUCE = "Deuce"
ALL = "All"
ADVANTAGE = "Advantage"
WIN_FOR = "Win for"

# Константы для бизнес-логики
MIN_SCORE_FOR_ADVANTAGE = 4
MIN_WIN_DIFFERENCE = 2
ADVANTAGE_DIFFERENCE = 1


class TennisGameRefactored:
    """
    Рефакторинг версия игры в теннис.

    Эта версия была создана в результате рефакторинга для улучшения:
    - Читаемости кода
    - Поддерживаемости
    - Тестируемости
    - Соблюдения принципов SOLID
    """

    def __init__(self, player1_name: str, player2_name: str) -> None:
        """
        Инициализирует новую игру в теннис.

        Args:
            player1_name: Имя первого игрока
            player2_name: Имя второго игрока
        """
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name: str) -> None:
        """
        Добавляет очко указанному игроку.

        Args:
            player_name: Имя игрока, который выиграл очко
        """
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score(self) -> str:
        """
        Возвращает текущий счет игры в строковом формате.

        Returns:
            Строковое представление счета (например, "Fifteen-Love")
        """
        if self._is_equal_score():
            return self._get_equal_score()
        elif self._is_advantage_or_win_situation():
            return self._get_advantage_or_win_score()
        else:
            return self._get_regular_score()

    def _is_equal_score(self) -> bool:
        """
        Проверяет, равны ли очки игроков.

        Returns:
            True если очки равны, иначе False
        """
        return self.player1_score == self.player2_score

    def _is_advantage_or_win_situation(self) -> bool:
        """
        Проверяет, является ли ситуация преимуществом или победой.

        В теннисе преимущество возможно только когда оба игрока
        набрали минимум 3 очка (40) и разница составляет 1 очко.

        Returns:
            True если ситуация преимущества или победы, иначе False
        """
        return (self.player1_score >= MIN_SCORE_FOR_ADVANTAGE or
                self.player2_score >= MIN_SCORE_FOR_ADVANTAGE)

    def _get_equal_score(self) -> str:
        """
        Обрабатывает ситуации равного счета.

        Returns:
            Строковое представление равного счета
        """
        if self.player1_score < 4:
            score_names = [LOVE, FIFTEEN, THIRTY, FORTY]
            score_name = score_names[self.player1_score]
            return f"{score_name}-{ALL}"
        return DEUCE

    def _get_advantage_or_win_score(self) -> str:
        """
        Обрабатывает ситуации преимущества и победы.

        Returns:
            Строковое представление счета при преимуществе или победе
        """
        score_difference = self.player1_score - self.player2_score

        if abs(score_difference) == ADVANTAGE_DIFFERENCE:
            leading_player = (self.player1_name if score_difference > 0
                              else self.player2_name)
            return f"{ADVANTAGE} {leading_player}"
        elif abs(score_difference) >= MIN_WIN_DIFFERENCE:
            winning_player = (self.player1_name if score_difference > 0
                              else self.player2_name)
            return f"{WIN_FOR} {winning_player}"

    def _get_regular_score(self) -> str:
        """
        Обрабатывает обычные ситуации счета (до 40-40).

        Returns:
            Строковое представление обычного счета
        """
        score_names = [LOVE, FIFTEEN, THIRTY, FORTY]
        player1_score_name = score_names[self.player1_score]
        player2_score_name = score_names[self.player2_score]
        return f"{player1_score_name}-{player2_score_name}"


def create_tennis_game(player1_name: str, player2_name: str,
                       implementation: str = "refactored") -> Any:
    """
    Фабричный метод для создания экземпляра игры в теннис.

    Args:
        player1_name: Имя первого игрока
        player2_name: Имя второго игрока
        implementation: Реализация игры. Возможные значения:
            - "refactored": Рефакторинг версия (по умолчанию)
            - "v1": Первая версия (TennisGameDefactored1)
            - "v2": Вторая версия (TennisGameDefactored2)
            - "v3": Третья версия (TennisGameDefactored3)

    Returns:
        Экземпляр игры в теннис выбранной реализации

    Raises:
        ValueError: Если указана неизвестная реализация
    """
    implementations: Dict[str, Any] = {
        "refactored": TennisGameRefactored,
        "v1": TennisGameDefactored1,
        "v2": TennisGameDefactored2,
        "v3": TennisGameDefactored3
    }

    if implementation not in implementations:
        raise ValueError(
            f"Неизвестная реализация: {implementation}. "
            f"Доступные реализации: {list(implementations.keys())}"
        )

    game_class = implementations[implementation]
    return game_class(player1_name, player2_name)


# Сохранение обратной совместимости для существующих тестов
TennisGame = TennisGameDefactored1