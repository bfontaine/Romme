# Romme

**Romme** is a Python library to convert dates between the
[French Republican calendar][rep] and the [Gregorian one][greg]. It’s named
after [Gilbert Romme][gilbert], who developed the former.

[rep]: https://en.wikipedia.org/wiki/French_Republican_Calendar
[greg]: https://en.wikipedia.org/wiki/Gregorian_calendar
[gilbert]: https://en.wikipedia.org/wiki/Gilbert_Romme

The French Republican calendar was briefly used in France between 1792 and
1806. The population didn’t widely use it, but official documents did. It can
be found in some [open datasets][parisdata]. Dealing with two different
calendars is a pain so this library allows you to translate from one to
another.

[parisdata]: https://opendata.paris.fr/explore/dataset/voiesactuellesparis2012/information/

## Usage

```python3
from romme import RepublicanDate

rd = RepublicanDate(5, 1, 1)  # first day of the year V

print("%s -> %s" % (rd, rd.to_date()))
# output: 1 vendémiaire, an V -> 1796-09-22

```
