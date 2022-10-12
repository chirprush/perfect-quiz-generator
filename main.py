from typing import Dict
from random import randint, uniform, choice
from enum import Enum, auto

def gen_sign() -> int:
    return -1 if uniform(0, 1) <= 0.3 else 1

def gen_integer(lower: int, upper: int) -> int:
    is_negative = uniform(0, 1) <= 0.3
    n = randint(lower, upper)

    return -n if is_negative else n

def gen_constant(zero_chance: float = 0.7) -> int:
    return 0 if uniform(0, 1) <= zero_chance else gen_integer(1, 15)

def format_coefficient(co: int) -> str:
    return "" if co == 1 else "-" if co == -1 else str(co)

def format_constant(constant: int) -> str:
    return "" if constant == 0 else "+ " + str(constant) if constant > 0 else str(constant)

def gen_definition_polynomial() -> str:
    leading_coefficient = gen_integer(1, 13)
    power = randint(2, 3)
    constant = gen_constant()

    return "%sx^{%s} %s" % (format_coefficient(leading_coefficient), power, format_constant(constant))

def gen_definition_rational() -> str:
    constant = gen_constant()

    return "\\dfrac{%s}{x %s}" % ("1", format_constant(constant))

def gen_definition_radical() -> str:
    constant = gen_constant()

    return "\\sqrt{x %s}" % (format_constant(constant))

def gen_definition() -> Dict[str, str]:
    choice = uniform(0, 1)

    if choice < 0.6:
        return { "def_equation" : gen_definition_polynomial() }
    elif choice < 0.8:
        return { "def_equation" : gen_definition_rational() }
    else:
        return { "def_equation" : gen_definition_radical() }

def gen_alternative_polynomial() -> str:
    power = randint(2, 3)
    constant = gen_constant()

    if power == 3:
        coefficient = gen_integer(1, 5)

        return "%sx^3 %s" % (format_coefficient(coefficient), format_constant(constant))
    elif power == 2:
        coefficient = gen_integer(1, 5)
        linear_term = uniform(0, 1) <= 0.2

        return "%sx^2 %s %s" % (format_coefficient(coefficient), "+ %sx" % format_coefficient(randint(1, 5)) if linear_term else "", format_constant(constant))

def gen_alternative_rational() -> str:
    constant = gen_constant()

    return "\\dfrac{%s}{x %s}" % ("1", format_constant(constant))

def gen_alternative_radical() -> str:
    constant = gen_constant()

    return "\\sqrt{x %s}" % (format_constant(constant))

def gen_alternative() -> Dict[str, str]:
    choice = uniform(0, 1)
    equation = None

    if choice < 0.6:
        equation = gen_alternative_polynomial()
    elif choice < 0.8:
        equation = gen_alternative_rational()
    else:
        equation = gen_alternative_radical()

    x = randint(1, 5)

    return {
        "alt_equation" : equation,
        "alt_x" : str(x)
    }

def gen_sdq_linear() -> str:
    coefficient = randint(1, 7)
    constant = gen_constant(0.0)

    return "%sx %s" % (format_coefficient(coefficient), format_constant(constant))

def gen_sdq_quadratic() -> str:
    coefficient = randint(1, 7)
    constant = gen_constant(0.2)

    return "%sx^2 %s" % (format_coefficient(coefficient), format_constant(constant))

def gen_sdq() -> Dict[str, str]:
    choice = uniform(0, 1)
    equation = None

    if choice < 0.3:
        equation = gen_sdq_linear()
    else:
        equation = gen_sdq_quadratic()

    x = randint(1, 5)

    return {
        "sdq_equation" : equation,
        "sdq_x" : str(x)
    }

def gen_prod() -> Dict[str, str]:
    first_power = randint(2, 9)
    second_power = randint(2, 9)

    if uniform(0, 1) < 0.3:
        first_coefficient = randint(2, 4)
        first_constant = first_coefficient * randint(1, 7)

        second_coefficient = randint(1, 9)
        second_constant = randint(1, 9)
    elif uniform(0, 1) < 0.6:
        first_coefficient = randint(1, 9)
        first_constant = randint(1, 9)

        second_coefficient = randint(2, 4)
        second_constant = second_coefficient * randint(1, 7)
    else:
        first_coefficient = randint(1, 9)
        first_constant = randint(1, 9)

        second_coefficient = randint(1, 9)
        second_constant = randint(1, 9)

    first_constant *= gen_sign()
    second_constant *= gen_sign()

    return {
        "prod_equation" : ("\\left( %sx %s \\right)^{%s} \\left( %sx %s \\right)^{%s}" % (
             format_coefficient(first_coefficient),
            format_constant(first_constant),
            first_power,
            format_coefficient(second_coefficient),
            format_constant(second_constant),
            second_power
        ))
    }

def gen_quot() -> Dict[str, str]:
    first_power = randint(2, 9)
    second_power = randint(2, 9)

    if uniform(0, 1) < 0.3:
        first_coefficient = randint(2, 4)
        first_constant = first_coefficient * randint(1, 7)

        second_coefficient = randint(1, 9)
        second_constant = randint(1, 9)
    elif uniform(0, 1) < 0.6:
        first_coefficient = randint(1, 9)
        first_constant = randint(1, 9)

        second_coefficient = randint(2, 4)
        second_constant = second_coefficient * randint(1, 7)
    else:
        first_coefficient = randint(1, 9)
        first_constant = randint(1, 9)

        second_coefficient = randint(1, 9)
        second_constant = randint(1, 9)

    first_constant *= gen_sign()
    second_constant *= gen_sign()

    return {
        "quot_equation" : ("\\dfrac{\\left( %sx %s \\right)^{%s}}{\\left( %sx %s \\right)^{%s}}" % (
             format_coefficient(first_coefficient),
            format_constant(first_constant),
            first_power,
            format_coefficient(second_coefficient),
            format_constant(second_constant),
            second_power
        ))
    }

def gen_trig_func() -> str:
    return "\\%s{x}" % (choice(["sin", "cos", "tan"]))

def gen_logdiff_func(const_chance: float) -> str:
    trig = uniform(0, 1) <= 0.5

    if trig:
        coefficient = randint(1, 3)
        constant = gen_constant(1 - const_chance)

        return "%s%s %s" % (format_coefficient(coefficient), gen_trig_func(), format_constant(constant))
    else:
        power = randint(2, 5)
        coefficient = randint(1, 5)
        constant = gen_constant(1 - const_chance)

        return "%sx^{%s} %s" % (format_coefficient(coefficient), power, format_constant(constant))

def gen_logdiff() -> Dict[str, str]:
    base = gen_logdiff_func(0.8)
    exponent = gen_logdiff_func(0.0)

    return {
        "logdiff_equation" : "\\left( %s \\right)^{%s}" % (base, exponent)
    }

with open("template.tex", "r") as f:
    template = f.read()

for i in range(500):
    options = {
        **gen_definition(),
        **gen_alternative(),
        **gen_sdq(),
        **gen_prod(),
        **gen_quot(),
        **gen_logdiff(),
        "form" : str(i + 1)
    }

    with open("bin/quiz" + str(i) + ".tex", "w") as f:
        f.write(template % options)
