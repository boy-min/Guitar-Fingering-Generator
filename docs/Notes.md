# class Notes

Manages note data played at the same time.

## Description

This class has all note data played at the same time.

## Constructor

### Notes
```py
def __init__(self, notes_ = None)
```

Instantiates the `Notes` object. Initializes member variable `notes` if parameter `notes_` is in the format of **list**.

## Member variables

### notes
```py
self.__notes
```

The list of `Note` objects. All `Note` should be played at the same time.

## Member functions

### set
```py
def set(self, notes_)
```

Sets `notes` variable if parameter `notes_` is in the format of **list**.

### get
```py
def get(self)
```

Returns `notes` variable.

### show
```py
def show(self, index = -1)
```
Shows part of `Note` by calling `Note.show()`. If index value is not given, shows all `Note`.
