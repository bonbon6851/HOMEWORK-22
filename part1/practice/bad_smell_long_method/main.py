# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = read_data(csv)
    sort_data = sort_data_desc(data)
    return filtration_data(sort_data)


def read_data(csv):
    data = [{'name': line.split(';')[0], 'age': int(line.split(';')[1])} for line in csv.split('\n')]
    return data


def sort_data_desc(data):
    sort_data = sorted(data, key=lambda x: int(x['age']))
    return sort_data


def filtration_data(sort_data):
    result_data = list(filter(lambda x: x['age'] > 10, sort_data))
    return result_data


if __name__ == '__main__':
    print(get_users_list())
