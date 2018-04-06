# without TransposeTests.test_mixed_line_length testcase
from itertools import zip_longest

def transpose(input_lines):
    if input_lines.count("\n") == 0:
        return "\n".join(list(input_lines))
    elif input_lines.count("\n") > 0:
        result = [list(element) for element in list(zip_longest(*input_lines.split("\n")))]
        for element in result:
            for item in element:
                if item is None:
                    element[element.index(item)] = " "
        result = ["".join(element) for element in result]
        return "\n".join(result).rstrip()



