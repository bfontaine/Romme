# -*- coding: UTF-8 -*-

from romme.romans import decimal_to_roman

months = (
    "",
    "Vendémiaire",
    "Brumaire",
    "Frimaire",
    "Nivôse",
    "Pluviôse",
    "Ventôse",
    "Germinal",
    "Floréal",
    "Prairial",
    "Messidor",
    "Thermidor",
    "Fructidor",
)

sans_culottides = (
    "",
    "de la vertue",
    "du génie",
    "du travail",
    "de l'opinion",
    "des récompenses",
    "de la révolution",
)


def republican_year_string(year):
    return decimal_to_roman(year)


def republican_day_string(year, month, day):
    year_string = republican_year_string(year)

    if month >= len(months):
        # sans-culottide
        return "jour %s, an %s" % (sans_culottides[day], year_string)

    return "%d %s, an %s" % (day, months[month], year_string)
