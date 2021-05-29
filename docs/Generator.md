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
def __difficulty(self, notes1 = None, fingers1 = None, notes2 = None, fingers2 = None)
```

Measures the degree of difficulty(= how hard it is to play) between two notes, or one notes, with certain criteria.
