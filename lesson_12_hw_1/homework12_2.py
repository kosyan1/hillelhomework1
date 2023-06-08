import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    html = codecs.open(html_file, 'r', 'utf-8').read()

    cleaned_text = ''
    inside_tag = False

    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            cleaned_text += char

    lines = cleaned_text.split('\n')

    non_empty_lines = []

    for line in lines:
        if line.strip():
            non_empty_lines.append(line)

    cleaned_text = '\n'.join(non_empty_lines)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text)

delete_html_tags('draft.html', 'cleaned.txt')
