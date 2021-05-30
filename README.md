# Guitar-Fingering-Generator

Input a desired music and the generator will generate efficient fingering via a dynamic programming algorithm.
You don't have to worry about which fingering to choose. This project will provide guidelines for people who are struggling with how to play the guitar.

## Introduction

This project uses `PyGuitarPro` to get music.

`PyGuitarPro` is a package to read, write and manipulate GP3, GP4 and GP5 files.

Reading .gp5 files is as easy as:
```py
import guitarpro
ProTab = guitarpro.parse('music_title_1.gp5')
```

Writing .gp5 files isn't that hard as well:
```py
guitarpro.write(ProTab, 'music_title_2.gp5')
```

## Installation

Install `PyGuitarPro`:
```sh
pip install PyGuitarPro
```

Cloning this project:
```sh
git clone https://github.com/boy-min/Guitar-Fingering-Generator.git
```

Put your music in `Guitar-Fingering-Generator\code\Main\Resources` folder.
And follow the command line:
```sh
cd Guitar-Fingering-Generator\code\Main
python main.py
```

## Program Example

Implementation example of `main.py`

```
Music title : twilight.gp5
Your hand size (0 : normal, 1 : small, 2 : big) : 0
Your finger length (0 : normal, 1 : short, 2 : long) : 0
Generating...
Success to write file : Finger_twilight.gp5
Exit the program.
```

After `Music title :`, you should write music's title which you want to generate fingering about.
It's format must be `.gp*`, and it should be in the `Resources` folder, which exists in the folder where `main.py` is located.
And according to your hand & finger, you will enter the number 0 ~ 2.
After generating is over, music containing efficient fingering, whose name is `Finger_ + "your music title"`,
will be stored in the `Resources` folder.

## Documentation

[PyGuitarPro](https://pyguitarpro.readthedocs.io/en/stable/) : Documentation of PyGuitarPro package.

[docs/README.md](docs/README.md) : Documentation of the program design.

## Contribution guidelines

If you want to contribute to our project, be sure to review the [code of conduct.](CODE_OF_CONDUCT.md) By participating,
you are expected to uphold this code.
We use [GitHub issues](https://github.com/boy-min/Guitar-Fingering-Generator/issues) for tracking requests and bugs, and you should follow
[PEP-8](https://www.python.org/dev/peps/pep-0008/) coding convention rules.
Contributing will make our project more valuable. If you want to do, contribute in the following order.

1. Forking our repository.
2. Creating a branch.
3. Adding commits.
4. Opening a [pull request.](https://github.com/boy-min/Guitar-Fingering-Generator/pulls)

If you open a pull request, we will review the codes, develop it, and merge when it is determined to be a good code.

## License

[MIT License](LICENSE)

## Team Members

2021 CAUSE Open Source Software Project TEAM 05

강현준, 김도균, 박상엽, 손현민
