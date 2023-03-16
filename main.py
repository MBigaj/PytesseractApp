from structs.img_manager import ImageManager
from structs.img_plotter import Plotter
from pathlib import Path
from auxilary.constants import IMG_PATH


def main():
    Manager = ImageManager()
    Plot = Plotter()
    img = 'sample_text.jpg'

    # Manager.parse_img_to_pdf('a')

    bounding_boxes = Manager.get_bounding_boxes(img)
    Plot.plot_with_boxes(img, bounding_boxes)

if __name__ == '__main__':
    main()
