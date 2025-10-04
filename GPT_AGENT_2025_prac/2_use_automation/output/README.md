    with open(f"{파일 경로}, 'w', encoding='utf-8') as f:
    f.write(summary)
- w 옵션은 해당 경로의 '파일'이 없으면 자동으로 생성하게 됨.
- 그러나 폴더 경로는 자동으로 생성되지 않음.