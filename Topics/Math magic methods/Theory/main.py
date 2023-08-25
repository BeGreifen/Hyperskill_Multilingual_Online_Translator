class ComplexNumber:
    def __init__(self, real_part, im_part):
        self.real_part = real_part
        self.im_part = im_part

    def __add__(self, other):
        real = self.real_part + other.real_part
        imaginary = self.im_part + other.im_part
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        real = self.real_part - other.real_part
        imaginary = self.im_part - other.im_part
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        real = self.real_part * other.real_part - self.im_part * other.im_part
        imaginary = self.real_part * other.im_part + other.real_part * self.im_part
        return ComplexNumber(real, imaginary)

    def __pow__(self, exponent):
        if isinstance(exponent, int):
            if exponent == 0:
                return ComplexNumber(1, 0)
            elif exponent < 0:
                reciprocal = ComplexNumber(1, 0) / self
                return reciprocal.__pow__(-exponent)

            result = ComplexNumber(1, 0)
            for _ in range(exponent):
                result *= self
            return result
        else:
            raise ValueError("Exponent must be an integer")

    def __eq__(self, other):
        return ((self.real_part == other.real_part) and
                (self.im_part == other.im_part))

    def __str__(self):
        if self.im_part < 0:
            sign = "-"
        else:
            sign = "+"
        string = "{} {} {}i".format(self.real_part, sign, abs(self.im_part))
        return string



