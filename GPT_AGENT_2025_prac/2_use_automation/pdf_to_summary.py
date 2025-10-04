import pymupdf 
## pip install pymupdf
from openai import OpenAI
from dotenv import load_dotenv
import os

from util import file_selector

pdf_file_path = file_selector()



load_dotenv()
api_key = os.getenv()

def summarize_pdf(file_path: str):
    client = OpenAI(api_key=api_key)

    # pdf 내용 추출.
    doc = pymupdf.open(pdf_file_path)
    full_text = "".join(page.get_text() for page in doc) ## 문서 페이지를 반복하여 한 문자열로.
    ## 줄마다 개행되어있는 부분. 수정 필요..

    system_prompt = f"다음 글을 요약하라.\n 아래 글에서 저자의 주장과 상황을 파악하여 주요 내용을 간결하게 요약하라\n\n{full_text}"

    #print(system_prompt)
    #print("="*25)

    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.5,
        messages=[
            {"role": "system", "content": system_prompt},
        ]
    )
    return response.choices[0].message.content


file_path = file_selector()

pdf_file_name = os.path.basename(pdf_file_path)
pdf_file_name, ext = os.path.splitext(pdf_file_name)

# pdf 예외 처리
if ext.lower() != '.pdf':
    raise ValueError("선택한 파일이 PDF 파일이 아닙니다.")
else:
    summary = summarize_pdf(file_path)
#print(summary)

with open(f"./2_use_automation/output/{pdf_file_name}_summary.txt", 'w', encoding='utf-8') as f:
    f.write(summary)