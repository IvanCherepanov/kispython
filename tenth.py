class Modlist:
    indexBad = -1

    def __init__(self, listLine):
        self.matrix = listLine

    def deleteDuplicateColumns(self):
        for i in range(len(self.matrix[0]) - 2):
            for j in range(i+1, len(self.matrix[0])):
                if self.matrix[0][i] == self.matrix[0][j]:
                    self.indexBad = j
                    break
        rows = len(self.matrix)
        for i in range(rows):
            _ = self.matrix[i].pop(self.indexBad)

    def deleteDuplicateRows(self):
        for i in range(len(self.matrix) - 2):
            for j in range(i+1, len(self.matrix)):
                if self.matrix[i][0] == self.matrix[j][0]:
                    self.indexBad = j
                    break
        _ = self.matrix.pop(self.indexBad)

    def normalizeData(self):
        for i in range(len(self.matrix)):
            self.matrix[i][0] = (self.matrix[i][0]).split(" ")[0]
            self.matrix[i][1] = "{0:.3f}".format((float(self.matrix[i][1])))
            self.matrix[i][2] = (self.matrix[i][2]).replace("/", "-")
            self.matrix[i][3] = (self.matrix[i][3]).split("[")[0]

    def transpose(self):
        res = [
            [self.matrix[j][i] for j in range(len(self.matrix))]
            for i in range(len(self.matrix[0]))
        ]
        return res


def main(list1):
    o = Modlist(list1)
    o.deleteDuplicateColumns()
    o.deleteDuplicateRows()
    o.normalizeData()
    return o.transpose()

    
list2 = [['Шишов Ю.Ш.','0.25','13/07/04','sisov39[at]yandex.ru','sisov39[at]yandex.ru'],
['Шасучев Д.У',	'0.97',	'26/04/02',	'sasucev76[at]mail.ru',	'sasucev76[at]mail.ru'],
['Зучий Ю.К.',	'0.29',	'11/06/02',	'zucij57[at]mail.ru',	'zucij57[at]mail.ru'],
['Шасучев Д.У.'	,'0.97',	'26/04/02',	'sasucev76[at]mail.ru',	'sasucev76[at]mail.ru']]

list3 = [
['Сазафак Н.З.','0.83','06/03/01','sazafak77[at]rambler.ru','sazafak77[at]rambler.ru'],
['Русичов А.О.','0.71', '10/04/99'	,'rusicov67[at]yahoo.com','rusicov67[at]yahoo.com'],
['Русичов А.О.','0.71', '10/04/99'	,'rusicov67[at]yahoo.com','rusicov67[at]yahoo.com'],
['Нифянц Г.Р.',	'0.40',	'13/06/02',	'nifanz35[at]gmail.com','nifanz35[at]gmail.com'],
['Мекев М.Т.','1.00',	'27/03/99',	'mekev49[at]yandex.ru',	'mekev49[at]yandex.ru']
]

list4 = [['Решак В.Ч.', '0.12', '20/10/03', 'resak42[at]yahoo.com', 'resak42[at]yahoo.com'], ['Загянц Л.Н.', '0.82', '04/06/00', 'zaganz2[at]mail.ru', 'zaganz2[at]mail.ru'], ['Решак В.Ч.', '0.12', '20/10/03', 'resak42[at]yahoo.com', 'resak42[at]yahoo.com'], ['Федулян П.Л.', '0.70', '24/12/02', 'fedulan60[at]gmail.com', 'fedulan60[at]gmail.com']]
print(*main(list2), sep = '\n')
print(*main(list3), sep = '\n')
print(*main(list4),sep = '\n')
