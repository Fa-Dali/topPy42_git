class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(
            self.real + other.real,
            self.imag + other.imag
        )

    def __sub__(self, other):
        return Complex(
            self.real - other.real,
            self.imag - other.imag
        )

    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )

    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        return Complex(
            (self.real * other.real + self.imag * other.imag) / denominator,
            (self.imag * other.real - self.real * other.imag) / denominator
        )

    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f'{self.real} {sign} {abs(self.imag)}i'

num1 = Complex(3, 4)  # Комплексное число 3 + 4i
num2 = Complex(-1, 2) # Комплексное число -1 + 2i

sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
div_result = num1 / num2

print(sum_result)  # 2 + 6i
print(diff_result) # 4 + 2i
print(prod_result) # -11 + 10i
print(div_result)  # 0.4 - 1.6i