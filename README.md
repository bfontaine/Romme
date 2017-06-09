# Romme

**Romme** is a Python library to convert dates between the
[French Republican calendar][rep] and the [Gregorian one][greg]. It’s named
after [Gilbert Romme][gilbert], who developed the former.

[rep]: https://en.wikipedia.org/wiki/French_Republican_Calendar
[greg]: https://en.wikipedia.org/wiki/Gregorian_calendar
[gilbert]: https://en.wikipedia.org/wiki/Gilbert_Romme

The French Republican calendar was briefly used in France between 1792 and
1806. The population didn’t widely use it, but official documents did; we can
see it used in some [open datasets][parisdata]. Dealing with two different
calendars is a pain, so this library allows you to translate from one to
another.

[parisdata]: https://opendata.paris.fr/explore/dataset/voiesactuellesparis2012/information/

## Usage

```python
from romme import RepublicanDate

rd = RepublicanDate(5, 1, 1)  # first day of the year V

rd.to_date()  # gives you a datetime.date object for the 1796/09/22

rd2 = RepublicanDate.from_gregorian(1796, 9, 22)
print(rd == rd2)  # True
```

## Features

- [x] Convert from French Republican to Gregorian calendar
- [ ] Convert from Gregorian to French Republican calendar
- [ ] Parse French Republican dates (e.g. `"3 prairial, an VIII"`)
