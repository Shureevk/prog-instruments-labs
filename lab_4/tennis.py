# -*- coding: utf-8 -*-

class TennisGameDefactored1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        result = ""
        tempScore = 0
        if (self.p1points == self.p2points):
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
                3: "Forty-All",
            }.get(self.p1points, "Deuce")
        elif (self.p1points >= 4 or self.p2points >= 4):
            minusResult = self.p1points - self.p2points
            if (minusResult == 1):
                result = "Advantage " + self.player1Name
            elif (minusResult == -1):
                result = "Advantage " + self.player2Name
            elif (minusResult >= 2):
                result = "Win for " + self.player1Name
            else:
                result = "Win for " + self.player2Name
        else:
            for i in range(1, 3):
                if (i == 1):
                    tempScore = self.p1points
                else:
                    result += "-"
                    tempScore = self.p2points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[tempScore]
        return result


class TennisGameDefactored2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        result = ""
        if (self.p1points == self.p2points and self.p1points < 4):
            if (self.p1points == 0):
                result = "Love"
            if (self.p1points == 1):
                result = "Fifteen"
            if (self.p1points == 2):
                result = "Thirty"
            if (self.p1points == 3):
                result = "Forty"
            result += "-All"
        if (self.p1points == self.p2points and self.p1points > 3):
            result = "Deuce"

        P1res = ""
        P2res = ""
        if (self.p1points > 0 and self.p2points == 0):
            if (self.p1points == 1):
                P1res = "Fifteen"
            if (self.p1points == 2):
                P1res = "Thirty"
            if (self.p1points == 3):
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.p2points > 0 and self.p1points == 0):
            if (self.p2points == 1):
                P2res = "Fifteen"
            if (self.p2points == 2):
                P2res = "Thirty"
            if (self.p2points == 3):
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res

        if (self.p1points > self.p2points and self.p1points < 4):
            if (self.p1points == 2):
                P1res = "Thirty"
            if (self.p1points == 3):
                P1res = "Forty"
            if (self.p2points == 1):
                P2res = "Fifteen"
            if (self.p2points == 2):
                P2res = "Thirty"
            result = P1res + "-" + P2res
        if (self.p2points > self.p1points and self.p2points < 4):
            if (self.p2points == 2):
                P2res = "Thirty"
            if (self.p2points == 3):
                P2res = "Forty"
            if (self.p1points == 1):
                P1res = "Fifteen"
            if (self.p1points == 2):
                P1res = "Thirty"
            result = P1res + "-" + P2res

        if (self.p1points > self.p2points and self.p2points >= 3):
            result = "Advantage " + self.player1Name

        if (self.p2points > self.p1points and self.p1points >= 3):
            result = "Advantage " + self.player2Name

        if (self.p1points >= 4 and self.p2points >= 0 and (self.p1points - self.p2points) >= 2):
            result = "Win for " + self.player1Name
        if (self.p2points >= 4 and self.p1points >= 0 and (self.p2points - self.p1points) >= 2):
            result = "Win for " + self.player2Name
        return result

    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        self.p1points += 1

    def P2Score(self):
        self.p2points += 1


class TennisGameDefactored3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1) else "Win for " + s


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


class TennisGameRefactored:
    """Рефакторинг версия игры в теннис."""

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        """Добавляет очко указанному игроку."""
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score(self):
        """Возвращает текущий счет игры."""
        if self._is_equal_score():
            return self._get_equal_score()
        elif self._is_advantage_or_win_situation():
            return self._get_advantage_or_win_score()
        else:
            return self._get_regular_score()

    def _is_equal_score(self):
        """Проверяет, равны ли очки игроков."""
        return self.player1_score == self.player2_score

    def _is_advantage_or_win_situation(self):
        """Проверяет, является ли ситуация преимуществом или победой."""
        return (self.player1_score >= MIN_SCORE_FOR_ADVANTAGE or
                self.player2_score >= MIN_SCORE_FOR_ADVANTAGE)

    def _get_equal_score(self):
        """Обрабатывает ситуации равного счета."""
        if self.player1_score < 4:
            scores = [LOVE, FIFTEEN, THIRTY, FORTY]
            return f"{scores[self.player1_score]}-{ALL}"
        return DEUCE

    def _get_advantage_or_win_score(self):
        """Обрабатывает ситуации преимущества и победы."""
        score_difference = self.player1_score - self.player2_score

        if abs(score_difference) == 1:
            leading_player = (self.player1_name if score_difference > 0
                              else self.player2_name)
            return f"{ADVANTAGE} {leading_player}"
        elif abs(score_difference) >= MIN_WIN_DIFFERENCE:
            winning_player = (self.player1_name if score_difference > 0
                              else self.player2_name)
            return f"{WIN_FOR} {winning_player}"

    def _get_regular_score(self):
        """Обрабатывает обычные ситуации счета (до 40-40)."""
        scores = [LOVE, FIFTEEN, THIRTY, FORTY]
        return f"{scores[self.player1_score]}-{scores[self.player2_score]}"


def create_tennis_game(player1_name, player2_name, implementation="refactored"):
    """
    Фабричный метод для создания экземпляра игры в теннис.

    Args:
        player1_name: Имя первого игрока
        player2_name: Имя второго игрока
        implementation: Реализация игры. Возможные значения:
            - "refactored": Рефакторинг версия (по умолчанию)
            - "v1": Первая версия
            - "v2": Вторая версия
            - "v3": Третья версия

    Returns:
        Экземпляр игры в теннис
    """
    implementations = {
        "refactored": TennisGameRefactored,
        "v1": TennisGameDefactored1,
        "v2": TennisGameDefactored2,
        "v3": TennisGameDefactored3
    }

    game_class = implementations.get(implementation, TennisGameRefactored)
    return game_class(player1_name, player2_name)


# Сохранение обратной совместимости
TennisGame = TennisGameDefactored1