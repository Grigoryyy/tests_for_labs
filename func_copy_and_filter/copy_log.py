import os


def copy_passwd() -> str:
    read_file = '/etc/passwd'
    write_file = '/home/lx64/PycharmProjects/tests_for_labs/func_copy_and_filter/passwd.txt'
    with open(read_file, 'r') as fr, open(write_file, 'w') as wf:
        for line in fr:
            line = line.replace(' ', '')
            wf.write(line)
    return "Data passwd copied"


def copy_group() -> str:
    read_file = '/etc/group'
    write_file = '/home/lx64/PycharmProjects/tests_for_labs/func_copy_and_filter/group.txt'
    with open(read_file, 'r') as fr, open(write_file, 'w') as wf:
        for line in fr:
            line = line.replace(' ', '')
            wf.write(line)
    return "Data group copied"

