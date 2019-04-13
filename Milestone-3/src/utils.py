
def genVarListFromSymTable(st, arr):
    d = st.table
    for k, v in dict.items(d):
        if (v['type'] == 'int_t' or v['type'] == 'float_t'):
            v['name'] = k
            arr.append(v)
        if 'child' in dict.keys(v):
            genVarListFromSymTable(v['child'], arr)

def offsetOf(name, l):
    for x in l[0]:
        if x['name'] == name:
            return x['offset']