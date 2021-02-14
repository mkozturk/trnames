# trnames

Random Turkish name generator with realistic probabilities.

Based on Trey Hunner's [names](https://github.com/treyhunner/names) package.

## Installation

The package can be installed using `pip` with the following command

```pip install git+https://github.com/mkozturk/trnames@main```

No other packages are required.

## Usage
Here are examples of all current features:
```
>>> import trnames
>>> trnames.get_full_name()
'Ahmet Harman'
>>> trnames.get_full_name(gender='male')
'Mustafa Berber'
>>> trnames.get_first_name()
'Hasan'
>>> trnames.get_first_name(gender='female')
'Behiye'
>>> trnames.get_last_name()
'Yuksel'
```

## Data
The probabilities of first and last names are parsed from 49,611,709 individuals, 24,534,483 men and 25,077,226 women, born between 1888 and 1991. 

## License

This project is released under an _MIT License_.

