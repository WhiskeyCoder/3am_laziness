import pyautogui
import time
import os
import img2pdf

book_name = 'Photographic Memory'
page_count = 2000

def main():
    time.sleep(5)
    for i in range(page_count):
        region = (552, 94, 624, 886)
        pyautogui.screenshot('shots\%d.png' % i, region=region)
        pyautogui.press('right')
        time.sleep(0.1)
    print("Screenshots Taken")
    raw_pages_to_pdf()

def raw_pages_to_pdf():
    file_type = 'pdf'
    dir_name = "screenshots"
    images = []
    for filename in os.listdir(dir_name):
        if not filename.endswith(".png"):
            continue
        path = os.path.join(dir_name, filename)
        if os.path.isdir(path):
            continue
        images.append(path)
    with open("/pdfs/" + book_name + "." + file_type, "wb") as f:
        f.write(img2pdf.convert(images))
        print("PDF Created")

if __name__ == '__main__':
    main()
