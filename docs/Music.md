# class Music

Manages music sheet data.

## Description

This class manages music data. Instantiated and used by `Generator`.

## Constructor

### Music
```py
def __init__(self, music_ = None)
```

Instantiates the `Music` object. Initializes member variable `music` and sets value if parameter `music_` is in the format of **list**.

## Member variables

### music
```py
self.__music
```

The list of `Notes` objects. Each notes have all note data played at the same time.

## Member functions

### set
```py
def set(self, music_)
```

Sets `music` value by calling `notes.Notes()`.

### get
```py
def get(self)
```

Returns `music` variable.

### show
```py
def show(self, index = -1)
```

Shows part of `Notes` in `music` variable  by calling `Notes.show()`. If index value is not given, shows all `Notes`.
