# class Hand

Manages user's hand information.

## Description

This class has two data (size, length) about user's hand. Instantiated and used by `Generator`.

## Constructor

### Hand
```py
def __init__(self, size = 0, length = 0)
```

Instantiates the `Hand` object. Initializes all member variables.

## Member variables

### size
```py
self.__size
```

The information about hand size.

### length
```py
self.__length
```

The information about finger length.

## Member functions

### set
```py
def set(self, size, length)
```

Sets `size`, `finger` variables.

### get
```py
def get(self, key = None)
```

Returns member variable according to the value of `key`. If `key` is `None`, returns dictionary of member variables.
