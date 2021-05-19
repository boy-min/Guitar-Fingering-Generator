# class Note

Manages note data.

## Description

This class has three data (string, fret, finger) about certain note. Instantiated and used by `Notes`.

## Constructor

### Notes
```py
def __init__(self, note_ = None)
```

Instantiates the `Note` object. Initializes all member variables, and if `note_` is not `None`, set values by using member function `set()`.

## Member variables

### string
```py
self.__string
```

The information about string number. Indicates which string to press on the guitar.

### fret
```py
self.__fret
```

The information about fret number. Indicates which fret to press on the guitar.

### finger
```py
self.__finger
```

The information about finger number. Indicates which finger to press on the guitar.

## Member functions

### set_finger
```py
def set_finger(self, finger)
```
Sets `finger` variables. Used by `Fingering` class.


### set
```py
def set(self, string, fret, finger)
```

Sets `string`, `fret`, `finger` variables.

### get
```py
def get(self, key = None)
```

Returns member variable according to the value of `key`. If `key` is `None`, returns dictionary of member variables.

### show
```py
def show(self)
```
Shows all member variables.
