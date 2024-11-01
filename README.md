# xyz2png

[![PyPI version](
  <https://badge.fury.io/py/xyz2png.svg>
  )](
  <https://badge.fury.io/py/xyz2png>
) [![Maintainability](
  <https://api.codeclimate.com/v1/badges/3f5110d732ac79473f80/maintainability>
  )](
  <https://codeclimate.com/github/eggplants/xyz2png/maintainability>
) [![pre-commit.ci status](
  <https://results.pre-commit.ci/badge/github/eggplants/xyz2png/master.svg>
  )](
  <https://results.pre-commit.ci/latest/github/eggplants/xyz2png/master>
)

[![ghcr latest](
  <https://ghcr-badge.egpl.dev/eggplants/xyz2png/latest_tag?trim=major&label=latest>
 ) ![ghcr size](
  <https://ghcr-badge.egpl.dev/eggplants/xyz2png/size>
)](
  <https://github.com/eggplants/xyz2png/pkgs/container/xyz2png>
)

Convert [`.xyz` file](http://justsolve.archiveteam.org/wiki/XYZ_(RPG_Maker)) into `.png` file

_Reimplementation [vn-tools/xyz2png](https://github.com/vn-tools/xyz2png) in Python3._

## Install

```bash
pip install xyz2png
```

```bash
# OR
pipx install xyz2png
```

## Run

```bash
xyz2png <target dir> <output dir>
```

## Example

```shellsession
$ ls FooBar/GameFiles/Picture/*.xyz
FooBar/GameFiles/Picture/foo1.xyz    FooBar/GameFiles/Picture/bar1.xyz

$ xyz2png FooBar/GameFiles/Picture output_images
Done.

$ ls output_images
foo1.png    bar1.png
```

## Help

```shellsession
$ xyz2png -h
usage: xyz2png [-h] [-o] [-V] IN OUT

Convert .xyz file into .png file.

positional arguments:
  IN               directory of xyz files
  OUT              directory to output png files

options:
  -h, --help       show this help message and exit
  -o, --overwrite  overwrite if png file exists
  -V, --version    show program's version number and exit
```
