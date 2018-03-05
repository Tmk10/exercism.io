def is_paired(input_string):
    stack = []
    open_brackets = ("(", "[", "{")
    close_brackets = (")", "]", "}")
    for item in input_string:
        if item in open_brackets:
            stack.append(item)
        elif item in close_brackets  and len(stack) >= 1:
            current_bracket_position = close_brackets.index(item)
            last_bracket_position = open_brackets.index(stack.pop())
            if current_bracket_position == last_bracket_position:
                continue
            else:
                return False

    return not stack


