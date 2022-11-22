import re
import json


lab1_data = {}


def get_data_json(input_data='/home/lx64/PycharmProjects/tests_for_labs/func_copy_and_filter/data_lab1.json'):
    global lab1_data
    with open(input_data) as i_d:
        templates = json.load(i_d)
    lab1_data = templates.copy()


def filter_users():
    get_data_json()
    result = []
    global lab1_data
    with open('/home/lx64/PycharmProjects/tests_for_labs/func_copy_and_filter/passwd.txt', 'r') as pas_res:
        result = pas_res.readlines()
        try:
            for i in range(len(result)):
                if re.match(lab1_data["users"][0], result[i]):
                    return 'true'
                    break
        except KeyError:
            print('Value not defined')


def filter_group():
    get_data_json()
    global lab1_data
    result_g = []
    with open('/home/lx64/PycharmProjects/tests_for_labs/func_copy_and_filter/group.txt', 'r') as group_res:
        result_g = group_res.readlines()
        try:
            for i in range(len(result_g)):
                filter_data = re.match(lab1_data["groups"][0], result_g[i])
                if filter_data:
                    return 'true-g'
                    break
        except KeyError:
            print('Value not defined')

