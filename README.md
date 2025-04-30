# Theme collection for the KIMMDY Emulators paper

## Install
Install using

```bash
pip install -e ./
```

## Usage

Note: The default figsize is single column width (88 mm) and the fontsize is 7pt as
required by Nature. To get the single/double size in inches for custom manipulation 
do `from kimmdy_paper_theme import single_column, double_column`. The default for new figures
is `figsize=(single_column, single_column/1.3333)`.

To use do either

```python
import kimmdy_paper_theme
plot_colors = kimmdy_paper_theme.auto_init()
[...]
ax.plot(xs, ys, label="Kimmdy values", color=plot_colors["kimmdy"])
```

OR to manually control the settings

```python
import kimmdy_paper_theme

plot_config = kimmdy_paper_theme.default_plot_config  # Load custom plot configs

# If you want to adjust something for your custom figure use
# plot_config['legend.fontsize'] = 5

kimmdy_paper_theme.apply_plot_config(plot_config=plot_config)  # Apply custom matplotlib style

# If you don't have roboto installed, you can manually load it like this
kimmdy_paper_theme.init_roboto_font()

plot_colors = kimmdy_paper_theme.plot_colors  # These are the predefined colors

[...]

ax.plot(xs, ys, label="Kimmdy values", color=plot_colors["kimmdy"])
```

All matplotlib settings can be changed in [kimmdy_paper_theme.py](kimmdy_paper_theme/kimmdy_paper_theme.py)
Specifically with `default_plot_config`.

To convert to RGB mode use
```python
kimmdy_paper_theme.convert_to_rgb("example1.png")
```
like in the example.


## Colors

These can be changed in [kimmdy_paper_theme.py](kimmdy_paper_theme/kimmdy_paper_theme.py)
with `category_color` and `plot_colors`.

Current category colors are:

![color_categories.png](kimmdy_paper_theme/color_categories.png)

The currently available color palette:

![color_palette.png](kimmdy_paper_theme/color_palette.png)



## Example plot from [example_plot.py](example_usage/example_plot.py):

![example1.png](example_usage/example1.png)

![example2.png](example_usage/example2.png)

## SVG

Denis' SVG Icons can be found at [icons](kimmdy_paper_theme/assets/icons)