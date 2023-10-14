import openpyxl
from utils import PropertyOfProduct
from pathlib import Path

CATEGORY_LINK = "https://santehnika-online.ru/ajax/react/productList/"
ABSOLUTE_PATH = Path(__file__).parent
EXCEL_PATH = ABSOLUTE_PATH.joinpath("propertys_vanny.xlsx")
PARSING_BRANDS = ABSOLUTE_PATH.joinpath("brands.txt")

if __name__ == "__main__":
    all_links = PropertyOfProduct.get_all_links(CATEGORY_LINK)
    workbook = openpyxl.load_workbook(EXCEL_PATH)
    sheet = workbook.active
    PropertyOfProduct.first_sheet(sheet)
    workbook.save(EXCEL_PATH)
    brands = PropertyOfProduct.get_parsing_brands(PARSING_BRANDS)
    row = 2
    for i, product in enumerate(all_links, start=1):
        link, title, brand = product
        if not brand:
            print(f"Ссылка № {i}. Брэнд отсутствует.")
            continue
        if brand.lower() in brands:
            data = PropertyOfProduct.get_product(link)
            propertys = PropertyOfProduct()
            propertys.get_property(data)
            all_propertys = propertys.get_all_property()
            PropertyOfProduct.save_to_excel(title, link, brand, all_propertys, row, sheet)
            workbook.save(EXCEL_PATH)
            print(f"Ссылка № {i}. Добавлен товар № {row - 1}")
            row += 1
        else:
            print(f"Ссылка № {i}. Товар не интересует. Брэнд {brand}")
