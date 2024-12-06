from Operators.Asterisk import Asterisk
from Operators.Caret import Caret
from Operators.Slash import Slash
from Operators.Minus import Minus
from Operators.Plus import Plus

operators_dictionary = {
    '+': Plus(),
    '-': Minus(),
    '*': Asterisk(),
    '/': Slash(),
    '^': Caret(),
    '%': 4,
    '$': 5,
    '&': 5,
    '@': 5,
    '~': 6,
    '!': 6,
}