
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

def get_offset(scopeDict):
    cunt = 0
    for s in scopeDict:
        cunt+=1

    offset = []
    offset = offset+[0]*(cunt)
    # print(cunt)
    var_offset = {}
    for i in range(cunt):
        if(i==0):
            continue
        maxx = 0
        for k , v  in scopeDict[i].table.items():
            var_offset[k] = offset[scopeDict[i].parent]+v['offset']
            maxx = v['offset']
        if(scopeDict[i].parent != 0):
            offset[scopeDict[i].parent]+=maxx+100
        offset[i]=maxx+100

    return var_offset
