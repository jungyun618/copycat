import pymupdf 
## pip install pymupdf
import os

from util import file_selector

pdf_file_path = file_selector()
doc = pymupdf.open(pdf_file_path)

full_text = "".join(page.get_text() for page in doc) ## 문서 페이지를 반복하여 한 문자열로.

pdf_file_name = os.path.basename(pdf_file_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0] ## 확장자 제거

txt_file_path = f"./2_use_automation/output/{pdf_file_name}.txt"
with open(txt_file_path, 'w', encoding='utf-8') as f:
    f.write(full_text)