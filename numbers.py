class NumberToAscii():
    numer = 0
    size = 0
    max_col = 0
    max_row = 0
    ascii = []
    vertical = '|'
    horizontal = '-'
    space = ' '
    patterns = {}

    number_pattern = {
        0: [5, 3, 3, 5],
        1: [0, 1, 1],
        2: [5, 2, 5, 1, 5],
        3: [4, 2, 4, 2, 4],
        4: [0, 3, 5, 2],
        5: [5, 1, 5, 2, 5],
        6: [5, 1, 5, 3, 5],
        7: [5, 2, 2],
        8: [5, 3, 5, 3, 5],
        9: [5, 3, 5, 2, 5]
    }

    def __init__(self, number, size):
        self.number = number
        self.size = size
        self.max_col = size + 2
        self.max_row = size * 2 + 3
        self.setPatterns()
        self.setAscii()

    def setPatterns(self):
        self.patterns = {
            0: self.space,
            1: self.vertical,
            2: self.space * (self.size + 1) + self.vertical,
            3: self.vertical + self.space * self.size + self.vertical,
            4: self.horizontal * self.size,
            5: self.space + self.horizontal * self.size
        }

        for key in self.patterns:
            self.patterns[key] += self.space \
                                  * (self.max_col - len(self.patterns[key]))

    def setAscii(self):
        self.ascii = []
        for pattern in self.number_pattern[self.number]:
            if self.vertical in self.patterns[pattern]:
                for times in range(self.size):
                    self.ascii.append(self.patterns[pattern])
            else:
                self.ascii.append(self.patterns[pattern])
        while len(self.ascii) != self.max_row:
            self.ascii.append(self.space * self.max_col)


def asciiToStr(list_ascii):
    r = ""
    for row in range(len(list_ascii[0])):
        for ascii in range(len(list_ascii)):
            r += ' '
            r += list_ascii[ascii][row]
        r += '\n'
    return r


if __name__ == "__main__":
    msgErr = "por favor ingrese numeros en el siguente formato: tamanio,numero"
    try:
        size, numbers = input("Ingrese un tamanio y un numero: \n").split(',')
    except ValueError as e:
        print(msgErr)
    else:
        size = int(size)
        numbers = list(map(int, str(numbers)))
        list_ascii = []
        for number in numbers:
            list_ascii.append(NumberToAscii(number, size).ascii)
        print(asciiToStr(list_ascii))
