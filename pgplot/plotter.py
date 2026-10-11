import pygame
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
from .colours import default_colours
from scipy.interpolate import make_interp_spline

pygame.init()

class Plotter:
    def __init__(self, plot_types_list, plot_labels_list=[], custom_colours=False, plot_colours_dict=None, display_axes=True, display_legend=False, dpi=100): # plot_types_list = ["scatter", "line", "smoothline", "trendline"], plot_labels_list = ["name1", "name2", "name3", "name4"]
        self.plot_types_list = plot_types_list
        self.plot_labels_list = plot_labels_list
        self.custom_colours = custom_colours
        self.plot_colours_dict = plot_colours_dict
        self.display_axes = display_axes
        self.display_legend = display_legend
        self.dpi = dpi

    def plot(self, surface, nested_input_array): # nested_input_array is regular python array
        
        # size calculation
        width = surface.get_width()
        height = surface.get_height()
        inch_width = width / self.dpi
        inch_height = height / self.dpi

        # creating graph
        fig, ax = plt.subplots(figsize=(inch_width, inch_height), dpi=self.dpi)

        # plotting
        for i, plot_type in enumerate(self.plot_types_list):
            x_values = np.array(nested_input_array[i][0])
            y_values = np.array(nested_input_array[i][1])
            label = None
            color = None
            if self.display_legend:
                label = self.plot_labels_list[i]
            if self.custom_colours:
                color = self.plot_colours_dict[i]
            else:
                color = default_colours[i]

            # line
            if plot_type == "line":
                ax.plot(x_values, y_values, color=color, label=label)
            # dots
            elif plot_type == "scatter":
                ax.scatter(x_values, y_values, color=color, label=label)
            # smoothline
            elif plot_type == "smoothline":
                print(x_values)
                print(y_values)
                print(i)
                print(nested_input_array[i])
                spline = make_interp_spline(x_values, y_values, k=3)
                x_smooth = np.linspace(x_values.min(), x_values.max(), 300) 
                y_smooth = spline(x_smooth)
                ax.plot(x_smooth, y_smooth, color=color, label=label)
            # trendline
            elif plot_type == "trendline":
                pass

        # configuring graph
        if not self.display_axes:
            ax.axis("off")
        if self.display_legend:
            ax.legend(loc='best', frameon=True, facecolor='white', edgecolor='gray')
        if self.custom_colours:
            kleur_kader_en_tekst = self.plot_colours_dict["axes"]
            kleur_grafiek_vlak = self.plot_colours_dict["background"]
            fig.patch.set_facecolor(kleur_grafiek_vlak)
            ax.set_facecolor(kleur_grafiek_vlak)
            for spine in ax.spines.values():
                spine.set_color(kleur_kader_en_tekst)
            ax.tick_params(colors=kleur_kader_en_tekst, which='both')

        # blit to pygame
        fig.tight_layout(pad=0)
        fig.canvas.draw()
        raw_data = fig.canvas.buffer_rgba()
        size = fig.canvas.get_width_height()
        plot_surface = pygame.image.frombuffer(raw_data, size, "RGBA")
        surface.blit(plot_surface, (0, 0))
        plt.close(fig)