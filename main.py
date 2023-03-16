from structs.img_manager import ImageManager
from structs.img_plotter import Plotter


def main():
    Manager = ImageManager()
    Plot = Plotter()
    img = 'img26.jpg'

    # Manager.parse_img_to_pdf('a')

    bounding_boxes = Manager.get_bounding_boxes(img)

    print(Manager.parse_img_to_string(img))

    Plot.plot_with_boxes(img, bounding_boxes)


if __name__ == '__main__':
    main()
