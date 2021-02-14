from os.path import abspath, join, dirname
import random

full_path = lambda filename: abspath(join(dirname(__file__), filename))

FILES = {
    'first:male': full_path('male_first.csv'),
    'first:female': full_path('female_first.csv'),
    'last': full_path('all_last.csv'),
}


def _get_name(filename):
    selected = random.random()
    with open(filename) as name_file:
        name_file.readline() # skip header line
        for line in name_file:
            name, cumulative = line.split(",")
            if float(cumulative) > selected:
                return name
    return ""  # Return empty string if file is empty


def get_first_name(gender=None):
    if gender is None:
        gender = random.choice(('male', 'female'))
    if gender not in ('male', 'female'):
        raise ValueError("Only 'male' and 'female' are supported as gender")
    return _get_name(FILES['first:%s' % gender]).capitalize()


def get_last_name():
    return _get_name(FILES['last']).capitalize()


def get_full_name(gender=None):
    return "{0} {1}".format(get_first_name(gender), get_last_name())