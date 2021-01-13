import argparse
import sys

from fitz import Document, Pixmap, Rect


def main(args):
    with open(args.pdf_file_name, "rb") as f:
        pdf_data = Document(stream=f.read(), filetype="pdf")

    with open(args.img_file_name, "rb") as f:
        pixmap = Pixmap(f.read())

    position = Rect(args.x, args.y, args.x + pixmap.width, args.y + pixmap.height)
    page = pdf_data[args.page]

    page.insertImage(position, pixmap=pixmap)

    with open(args.o, "wb") as f:
        f.write(pdf_data.write())


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_file_name")
    parser.add_argument("img_file_name")

    parser.add_argument("-x", type=int, default=0)
    parser.add_argument("-y", type=int, default=0)
    parser.add_argument("-o", default="out.pdf")
    parser.add_argument("-p", "--page", type=int, default=0)

    args = parser.parse_args()

    sys.exit(main(args))
