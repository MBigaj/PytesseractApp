from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path
from auxilary.constants import IMG_PATH


class Plotter:
    def __init__(self) -> None:
        pass

    def plot_with_boxes(self, filename, boxes):
        # Display boxes on found letters
        img = Image.open(Path.joinpath(IMG_PATH, filename))

        _, ax = plt.subplots()

        ax.imshow(img)

        for box in boxes:
            rect = patches.Rectangle((box[0], box[1]), box[2], box[3], linewidth=1, edgecolor='r', facecolor='none')
            ax.add_patch(rect)

        plt.show()
