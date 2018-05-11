from string import punctuation

f1 = open("f", "r")
f2 = open("f2", "r")
f1_txt = f1.read()
f2_txt = f2.read()


def main(name1, name2, slice):
    f1 = open(name1, "r")
    f2 = open(name2, "r")
    f1_txt = f1.read()
    f2_txt = f2.read()
    ff1 = []
    ff2 = []

    _clean_text(f1_txt.split(), ff1)
    _clean_text(f2_txt.split(), ff2)
    result = []
    j=0
    res=_more_clean_result(_get_similarty(ff1, ff2, slice))
    for i in res:
        s=""
        for h in i:

           s+= h+" "
        result.append(s)
    return result , res


def _clean_text(text, f):
    for i in text:
        s = ""
        for a in i:
            if a not in punctuation:
                #   if not a.isdigit():
                s += a
        f.append(s)


def _convert_list_to_2d(list, append):
    l = []
    for i in range(len(list)):
        ll = []
        if len(list) - i >= 5:
            for a in list[i:i + append]:
                ll.append(a)
            l.append(ll)
    return l


def _get_similarty(f11, f22, slice):
    got = []
    file1 = _convert_list_to_2d(f11, slice)
    file2 = _convert_list_to_2d(f22, slice)
    for i in range(len(file2)):
        a = file2[i]

        for q in range(len(file1)):
            b = file1[q]
            w = 0
            for f in range(len(b)):
                if (b[f] == a[f]):
                    w += 1
            if w == 5:
                got.append(a)
    return got


def _more_clean_result(list):
    l = []
    l.append(list[0])

    j = 0
    for i in range(len(list) - 1):

        if list[i + 1][0] in l[j]:
            for a in list[i + 1]:
                if a not in l[j]:

                    l[j].append(a)
        else:
            j += 1
            l.append(list[i + 1])
    return l
