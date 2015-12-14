from monom import Monom


class Element:

    def __init__(self, element):
        self.element = element
        self.char_dict = {}
        self.index = 0

    def split_element(self):
        for x in self.element:
            if x == '^':
                self.index = 1
            self.check_element(x)
        return self.char_dict

    def check_element(self, char):
        if self.index == 1:
            if char == '^':
                pass
            elif 'power' in self.char_dict:
                self.char_dict['power'] += char
            else:
                self.char_dict['power'] = char
        elif char.isdigit():
            if 'coeff' in self.char_dict:
                self.char_dict['coeff'] += char
            else:
                self.char_dict['coeff'] = char
        else:
            self.char_dict['value'] = char

    def edit_element(self):
        self.split_element()
        if not 'coeff' in self.char_dict:
            self.char_dict['coeff'] = 1
        if not 'value' in self.char_dict:
            self.char_dict['value'] = 'x'
            self.char_dict['power'] = 0
        else:
            if not 'power' in self.char_dict:
                self.char_dict['power'] = 1

    def return_monom(self):
        self.edit_element()
        self.monom = Monom(int(self.char_dict['coeff']), self.char_dict[
                           'value'], int(self.char_dict['power']))
        self.monom.derivative()
        return self.monom
