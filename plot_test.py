import pgplot.plotter as plt
import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 800))

plot_types_list = [
    "scatter",
    "line"
]

plot_labels_list = [
    "plot1",
    "plot2"
]

plot_colours_dict = {
    "background": "#000000",
    "axes": "#E1E0E0",
    0: "#416EB3",
    1: "#FFDA21"
}

plot_surface = pygame.Surface((800, 600))
plotter = plt.Plotter(
    plot_types_list, 
    plot_labels_list=plot_labels_list, 
    custom_colours=True, 
    plot_colours_dict=plot_colours_dict, 
    display_axes=True, 
    display_legend=True
)
plotter.plot(
    plot_surface,
    [
        [
            [0, 1, 3, 6, 8, 9, 12], 
            [5, 2, 6, 8, -4, 2, 4]
        ],
        [
            [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14],
            [5, 9, 2, 4, 5, 3, 7, 5, 9, 8, 9, 5, 4]
        ]
    ]
)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(plot_surface, (50, 50))
    pygame.display.update()