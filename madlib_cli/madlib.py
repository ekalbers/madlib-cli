def read_template(file):
    with open(file) as reader:
        output = reader.read()
    return output


def parse_template(string):
    parts = []
    part = ''
    no_parts = ''
    is_part = False
    for char in string:
        if char == '}':
            is_part = False
            parts.append(part)
        if is_part:
            part = part + char
        else:
            no_parts = no_parts + char
        if char == '{':
            is_part = True
            part = ''

    return no_parts, tuple(parts)


def merge(string, parts):
    list_string = string.split(' ')
    list_string_counter = 0
    parts_counter = 0
    for x in list_string:
        if '{}' in x:
            list_string[list_string_counter] = parts[parts_counter]
            if len(x) > 2:
                list_string[list_string_counter] += x[2:]
            parts_counter += 1
        list_string_counter += 1

    new_string = ''
    for x in list_string:
        new_string = new_string + x + ' '

    return new_string.strip()


def create_file(string):
    with open('assets/copy_make_me_a_video_game_template.txt', 'w') as writer:
        writer.write(string)


def main():
    text, parts = parse_template(read_template('assets/make_me_a_video_game_template.txt'))
    parts_input = ()
    print('*************')
    print('***MADLIBS***')
    print('*************')
    print('\nSubmit words that match the word types requested!\n')
    for x in parts:
        parts_input += (input(f'{x}:'),)
    new_file = merge(text, parts_input)
    create_file(new_file)
    print(f'\n{new_file}')


if __name__ == '__main__':
    main()
