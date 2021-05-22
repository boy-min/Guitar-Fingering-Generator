# Guitar-Fingering-Generator

2021 CAUSE Open Source Software Project TEAM 05

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
```
pip install PyGuitarPro
```

## Documentation

[PyGuitarPro](https://pyguitarpro.readthedocs.io/en/stable/) : Documentation of PyGuitarPro package.

[docs/README.md](docs/README.md) : Documentation of the program design.

## Final report

[OSS project proposal final report.docx](OSSProjectProposalFinalReport.docx) : Final report about project

## Team Members

강현준, 김도균, 박상엽, 손현민

## License

[MIT License](LICENSE)
