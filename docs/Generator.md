# class Generator

Manages all processes to generate effieicnt fingering.

효율적인 운지법을 생성하는 모든 과정을 총괄하는 클래스.

## Description

This class manages entire processes with `Music`, `Fingering`, `Hand` objects. Instantiated and used by `main()`.

## Constructor

### Generator
```py
def __init__(self, music_ = None)
```

Instantiates the `Generator` object. Instantiates all member variables and sets `music` value if `Generator` received `music_` value in the format of **list**.

## Member variables

### music
```py
self.__music
```

The `Music` object to use. Manages music sheet data.

### fingering
```py
self.__fingering
```

The `Fingering` object to use. Manages fingering about basic guitar codes.

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

Generates effieicnt fingering and edit fingering information in `music`.