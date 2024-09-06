import re, argparse

def parse_and_replace_markdown(file_path, replacements):
    # 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 정규 표현식을 사용하여 특정 단어 찾기 및 변경
    for search_word, replace_word in replacements.items():
        pattern = re.compile(re.escape(search_word))
        content = pattern.sub(replace_word, content)

    print(content)

    # 변경된 내용을 파일에 다시 쓰기
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print("Text replacements completed.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse and replace text in a Markdown file.')
    parser.add_argument('file_path', type=str, help='Path to the Markdown file')

    replacements = {
        '합니다.': '\n- ',
        '됩니다.': '\n- ',
        '습니다.': '음\n- ',
        '입니다.': '\n- ',
        ':': '\n- '
    }  # 찾고자 하는 단어와 변경할 단어의 딕셔너리

    args = parser.parse_args()
    parse_and_replace_markdown(args.file_path, replacements)