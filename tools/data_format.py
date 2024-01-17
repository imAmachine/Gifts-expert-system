from itertools import repeat


def get_table_str(table_title: str, headers: list, data: list):
    result_str_table = ''
    lines_count = max(map(lambda x: len(x), data))
    cols_width = [max(map(len, col)) + 4 for col in data]
    table_border_hor = ''.join(repeat('=', sum(cols_width) + 5)) + '\n'

    # название таблицы
    result_str_table += table_border_hor
    result_str_table += f'={table_title:^{sum(cols_width) + 3}}=\n'

    # шапка таблицы
    result_str_table += table_border_hor
    for idx, head in enumerate(headers):
        result_str_table += f'={head:^{cols_width[idx]}}'
    result_str_table += '=\n'
    result_str_table += table_border_hor

    # элементы таблицы
    for line in range(lines_count):
        line_str = ''
        for idx, col in enumerate(data):
            if line < len(col):
                line_str += f'={col[line]:^{cols_width[idx]}}'
            else:
                line_str += '=' + ''.join(repeat(' ', cols_width[idx]))

        result_str_table += f"{line_str}=\n"
        result_str_table += table_border_hor

    return result_str_table
