import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")

with app.setup:
    import io

    import marimo as mo
    from PIL import Image

    from png2svg.core import image_to_svg


@app.cell
def _():
    mo.md(r"""
    # PNG to SVG Converter

    Upload a PNG image and convert it into a scalable hexagonal SVG wallpaper.
    """)
    return


@app.cell
def _():
    file = mo.ui.file(filetypes=[".png"], label="Pick a PNG image")
    size = mo.ui.slider(4, 30, value=10, label="Hexagon size")
    mo.vstack([file, size])
    return file, size


@app.cell
def _(file, size):
    if file.value:
        img = Image.open(io.BytesIO(file.contents()))
        svg = image_to_svg(img, size=size.value, radius=3)
        output = mo.Html(svg)
    else:
        output = mo.md("*Pick a PNG file above to see the result.*")
    output
    return


if __name__ == "__main__":
    app.run()
