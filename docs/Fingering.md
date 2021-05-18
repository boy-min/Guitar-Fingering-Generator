# class Fingering

Manages fingering about basic guitar codes.

## Description

This class manages fingering about basic guitar codes. Instantiated and used by `Generator`.

## Constructor

### Fingering
```py
def __init__(self)
```

Instantiates the `Fingering` object. Initializes member variable `fingering` and sets value by using `append` function.

## Member variables

### fingering
```py
self.__fingering
```

The list of `Notes` objects. Each notes have the information about certain guitar code.

## Member functions

### append
```py
def __append(self, code)
```

Append guitar code at `fingering` variable in the format of `Notes`.

### delete
```py
def __delete(self, index)
```

Delete guitar code from `fingering`.

### find_similar_code
```py
def __find_similar_code(self, n)
```
Finds and returns guitar code most similar to `n` by using `fingering` variable.


### get
```py
def get(self)
```

Returns `fingering` variable.

### set
```py
def set(self, n)
```

Finds most similar guitar code by using `find_similar_code`, and sets initial fingering.
