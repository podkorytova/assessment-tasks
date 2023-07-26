import argparse


def argument_parser_decorator(func):
    def wrapper():
        parser = argparse.ArgumentParser()
        parser.add_argument('-la', '--list_arrays', type=str, nargs='+', action='append')
        parser.add_argument('-t', '--target', type=int)
        namespace = parser.parse_args()
        data_is_correct = True
        for a in namespace.list_arrays:
            if len(a) != 4:
                data_is_correct = False
        if data_is_correct:
            return func(namespace)
        else:
            print('Each array should contains 4 elements. Try again with right data.' )
    return wrapper

@argument_parser_decorator
def find_array_with_target_element(namespace):
    input_list = namespace.list_arrays
    target = namespace.target
    list_arrays_with_target_name = []
    for array in input_list:
        find_target = False
        for i in range(0, 4):
            if array[i] == str(target):
                find_target = True
        if find_target:
            list_arrays_with_target_name.append(array)
    return list_arrays_with_target_name


output = find_array_with_target_element()
print(output)

