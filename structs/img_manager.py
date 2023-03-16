import pytesseract
from pathlib import Path
from auxilary.constants import IMG_PATH, SAVE_LOC


class ImageManager:
    # Class for managing images
    def __init__(self) -> None:
        pass

    def get_bounding_boxes(self, filename: str) -> list[list]:
        result = pytesseract.image_to_boxes(f'{IMG_PATH}/{filename}')

        bounding_boxes = result.split('\n')

        bounding_boxes = [element[2:] for element in bounding_boxes]
        bounding_boxes = [element.split(' ') for element in bounding_boxes]

        # Convert all coordinates to int and remove null coordinates
        bounding_boxes = [[int(coordinate) if len(coordinate) != 0 else coordinate for coordinate in box] for box in bounding_boxes]

        # Remove all null coordinates
        for i in range(len(bounding_boxes)):
            for coordinate in bounding_boxes[i]:
                if coordinate == '':
                    bounding_boxes.pop(i)
    
        return bounding_boxes

    def parse_img_to_string(self, filename: str) -> str:
        text_from_img = pytesseract.image_to_string(f'{IMG_PATH}/{filename}')
        return text_from_img

    def parse_img_to_pdf(self, option: str = 's', filename: str = '') -> None:
        # Option s - single file | a - all files

        if option == 's':
            pdf = pytesseract.image_to_pdf_or_hocr(f'{IMG_PATH}/{filename}', extension='pdf')
            self.save_file(pdf)
        elif option == 'a':
            for file in IMG_PATH.iterdir():
                print(file)
                pdf = pytesseract.image_to_pdf_or_hocr(str(file), extension='pdf')
                self.save_file(pdf)
        else:
            raise UnboundLocalError()

    def save_file(self, file: bytes) -> None:
        name = len(list(SAVE_LOC.iterdir()))

        with open(f'{SAVE_LOC}/{name}.pdf', 'w+b') as f:
            f.write(file)