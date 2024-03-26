from __future__ import annotations

import argparse
import io
import struct
import sys
import zlib
from pathlib import Path
from typing import NoReturn

from PIL import Image

from . import __version__


def convert_image(xyz_path: Path) -> Image.Image | bytes:
    with xyz_path.open("rb") as f:
        magic = f.read(4)
        if magic != b"XYZ1":
            return magic

        width, height = struct.unpack("=HH", f.read(4))

        body = io.BytesIO(zlib.decompress(f.read()))
        palette = [struct.unpack("=3B", body.read(3)) for x in range(256)]

        image = Image.new("RGBA", (width, height))
        pixels = image.load()

        for y in range(height):
            for x in range(width):
                pixels[x, y] = palette[ord(body.read(1))]

        return image


def parse_args(test: list[str] | None = None) -> argparse.Namespace:
    """Parse arguments."""
    parser = argparse.ArgumentParser(
        prog="xyz2png",
        description="Convert .xyz file into .png file.",
    )
    parser.add_argument(
        "xyz_dir_path",
        metavar="IN",
        type=str,
        help="directory of xyz files",
    )
    parser.add_argument(
        "png_dir_path",
        metavar="OUT",
        type=str,
        help="directory to output png files",
    )
    parser.add_argument(
        "-o",
        "--overwrite",
        action="store_true",
        help="overwrite if png file exists",
    )
    parser.add_argument("-V", "--version", action="version", version=__version__)

    if test:
        return parser.parse_args(test)
    return parser.parse_args()


def main() -> None:
    def print_err_and_exit(message: str) -> NoReturn:
        print(message, file=sys.stderr)  # noqa: T201
        sys.exit(1)

    args = parse_args()

    xyz_dir_path = Path(args.xyz_dir_path)
    png_dir_path = Path(args.png_dir_path)
    overwrite = bool(args.overwrite)

    if png_dir_path.exists() and not png_dir_path.is_dir():
        print_err_and_exit(f"Given output path is not dir: {png_dir_path}")
    png_dir_path.mkdir(exist_ok=True)

    for xyz_file_path in xyz_dir_path.glob("**/*.xyz"):
        png_file_path = png_dir_path / f"{xyz_file_path.stem}.png"
        if not overwrite and png_file_path.exists():
            print(f"File already exists: {png_file_path.name}")  # noqa: T201
            continue

        image = convert_image(xyz_file_path)
        if isinstance(image, bytes):
            print(f"File is not xyz file: {image!r}")  # noqa: T201
            continue

        image.save(png_file_path)

    print("Done.")  # noqa: T201


if __name__ == "__main__":
    main()
