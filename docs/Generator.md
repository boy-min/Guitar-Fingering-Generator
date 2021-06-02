# class Generator

Manages all processes to generate effieicnt fingering

## Description

This class manages entire processes with `Music`, `Hand` objects. Instantiated and used by `main()`.

## Constructor

### Generator
```py
def __init__(self, music_ = None)
```

Instantiates the `Generator` object. Initializes all member variables and sets `music` value if `Generator` received `music_` value in the format of **guitarpro.models.Song**. Click [here](https://pyguitarpro.readthedocs.io/en/stable/pyguitarpro/api.html) to see documentation about it.

## Member variables

### music
```py
self.__music
```

The `Music` object to use. Manages music sheet data.

### hand
```py
self.__hand
```

The `Hand` object to use. Manages user's hand information.

### weight
```py
self.__weight
```

Weight values to use. It has 10 values, and if follow rules [pull request 23.](https://github.com/boy-min/Guitar-Fingering-Generator/pull/23)

### ratio
```py
self.__ratio
```

Ratio values to use. It has 6 values, and it follow rules [pull request 23.](https://github.com/boy-min/Guitar-Fingering-Generator/pull/23)

## Member functions

### set
```py
def set(self, music_)
```

Sets `music` value to get input in the format of **list** by calling `music.set(music_)`.

### get
```py
def get(self)
```

Returns `music`.

### generate
```py
def generate(self)
```

Generates efficient fingering and edit fingering information in `music`.

### difficulty
```py
def __difficulty(self, notes_1 = None, finger_list_1 = None, notes_2 = None, finger_list_2 = None)
```

Measures the degree of difficulty(= how hard it is to play) between two notes, or one notes, with certain criteria. It uses
`get_pos()`, `get_change_dif()`, `get_dif()` member functions to get difficulty.

### get_pos
```py
def __get_pos(self, notes, finger_list)
```

Estimates 2'th finger's fret number, and returns it.

### get_change_dif
```py
def __get_change_dif(self, sorted_list_1, sorted_list_2)
```

Measures the degree of difficulty between two notes, and returns it.

### get_dif
```py
def __get_dif(self, sorted_list, pos)
```

Measures the degree of difficulty of one notes, and returns it.

### check_twist
```py
def __check_twist(self, notes, finger_list)
```

Checks whether notes is twisted state, or not. If it is, returns `weight[0]`.

### check_highcode
```py
def __check_highcode(self, notes, finger_list)
```

When notes is highcode, checks to see if it meets the requirements of highcode.

