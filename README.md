# Matplotlib Graphs in Pygame

A simple library to easily plot line graphs and scatter plots in a pygame window using matplotlib.

---

## About the Project

When importing matplotlib the package runs
```python
matplotlib.use("agg")
```
This makes it run in the background and not open a window. The plots and graphs are then created normally. When all plots are on there the graph is turned into a raw image, pygame then turns this raw image into a pygame surface using
```python
pygame.image.frombuffer(raw_data, size, "RGBA")
```

## Getting Started

### Installing the Library

**Requires:** Python 3.10 - 3.13  

Install the python package using pip, preferably in a venv.
```
pip install git+https://github.com/IAmDaanE/pygame-plot.git@master
```

### Usage in Code

Importing
```python
import pgplot as pgp
```
Initiating the plotter class
```python
my_plots = ["line", "line", "scatter", "smoothline"] # the plottypes you want
plotter = pgp.Plotter(myplots, display_legend=False)
```
Making the graph surface, the nested array contains all the x and values of the points on the plots.
```python
graph_surface = pygame.Surface((500, 400))
plotter.plot(graph_surface, 
                        [
                        [x_values1, y_values1],
                        [x_values2, x_values2],
                        [x_values3, x_values3],
                        [x_values4, x_values4],
                        ])
```
Blit the graph surface
```python
screen.blit(graph_surface, (200, 50)) # inside game loop
```

## License

This project is open-source and available under the MIT License.