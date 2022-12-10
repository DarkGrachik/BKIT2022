
def field(items, *args):
    if (len(items) == 0):
        print("List of dicts is empty")

    assert (len(items) > 0)
    if (len(args) == 1):
        result = []
        for i in range(len(items)):
            for key in items[i]:
                if key in args:
                    result.append(items[i][key])
    else:
        result = [{} for i in range(len(items))]
        for i in range(len(items)):
            for key in items[i]:
                if key in args:
                    result[i].update({key:items[i][key]})
    return result


#Пример:
#goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
#]
#print(field(goods, 'title')) #должен выдавать 'Ковер', 'Диван для отдыха'
#print(field(goods, 'title', 'price')) #должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}