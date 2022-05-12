import re


def main(text):
    keys = re.findall(r'"(.*?)"', text) 

    values = re.findall(r' -?\d+ ', text)
    for i in range(len(values)):
        j = values[i].replace(" ",'')
        values[i] = int(j)
    temp = dict(zip([data for data in keys], [data for data in values]))
    return temp
    
text1='( .do make 1832 to @"lelete".end, .do make -6969 to @"gedi" .end, .do make 9134 to @"soxe_736" .end,)'
print(main(text1))
text2 = '( .do make 5067 to @"disoqu_265".end, .do make -2856 to @"atgequ_673".end,.do make -3759 to @"onso".end, )'
print(main(text2))
