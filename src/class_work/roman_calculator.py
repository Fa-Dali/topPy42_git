class RomanCalculator:
    ROMAN_VALUES = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
        'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
        'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
        'M': 1000
    }

    ARABIC_TO_ROMAN = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def __init__(self, value=None):
        """Инициализирует объект либо числом, либо римской цифрой."""
        if isinstance(value, int):
            self._value = value
        elif isinstance(value, str):
            self._value = self.__roman_to_arabic(value)
        else:
            raise TypeError("Некорректный тип аргумента. Должен быть string или integer.")

    @property
    def arabic(self):
        """Возвращает арабское представление числа."""
        return self._value

    @property
    def roman(self):
        """Возвращает римское представление числа."""
        return self.__arabic_to_roman(self._value)

    def __roman_to_arabic(self, s):
        """Преобразует римское число в арабское."""
        res = 0
        index = 0
        length = len(s)
        while index < length:
            if index + 1 < length and s[index : index + 2] in self.ROMAN_VALUES:
                res += self.ROMAN_VALUES[s[index : index + 2]]
                index += 2
            else:
                res += self.ROMAN_VALUES[s[index]]
                index += 1
        return res

    def __arabic_to_roman(self, n):
        """Преобразует арабское число в римское."""
        result = []
        for value, symbol in self.ARABIC_TO_ROMAN:
            while n >= value:
                result.append(symbol)
                n -= value
        return ''.join(result)

    def __add__(self, other):
        """Операция сложения."""
        new_value = self.arabic + other.arabic
        return RomanCalculator(new_value)

    def __sub__(self, other):
        """Операция вычитания."""
        new_value = self.arabic - other.arabic
        return RomanCalculator(new_value)

    def __mul__(self, other):
        """Операция умножения."""
        new_value = self.arabic * other.arabic
        return RomanCalculator(new_value)

    def __truediv__(self, other):
        """Операция деления."""
        new_value = self.arabic // other.arabic  # Целочисленное деление
        return RomanCalculator(new_value)

    def __str__(self):
        """Строковое представление римского числа."""
        return self.roman

    def __repr__(self):
        """Официальное строковое представление объекта."""
        return f"RomanCalculator({self.roman})"

# Демонстрация работы:
if __name__ == "__main__":
    r1 = RomanCalculator("XVIII")  # 18
    print(r1.arabic)
    r2 = RomanCalculator(7)        # VII

    add_result = r1 + r2           # XVIII + VII = XXV (25)
    sub_result = r1 - r2           # XVIII - VII = XI (11)
    mul_result = r1 * r2           # XVIII * VII = CXXVI (126)
    div_result = r1 / r2           # XVIII ÷ VII ≈ II (2)

    print(r1)                      # XVIII
    print(r2)                      # VII
    print(add_result)              # XXV
    print(sub_result)              # XI
    print(mul_result)              # CXXVI
    print(div_result)              # II