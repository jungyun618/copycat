import tkinter as tk
from tkinter import filedialog

def file_selector():
    # 루트 윈도우 숨기기
    root = tk.Tk()
    root.withdraw()

    # 파일 선택 창 열기
    file_path = filedialog.askopenfilename(
        title="파일 선택",
        filetypes=[("모든 파일", "*.*"), ("텍스트 파일", "*.txt"), ("CSV 파일", "*.csv"), ("PDF 파일", "*.pdf")]
    )

    return file_path