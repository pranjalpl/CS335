import sys
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


def get_max_offset(scopeDict,var_offset):
    s = scopeDict[0]
    max_size = {}
    last = {}
    for k , v in s.table.items():
        if(v['type']=='func'):
            for k1 , v1 in v['child'].table.items():
                maxx = var_offset[k1]
                last = v1
            extra = 0
            if(last['type'] == 'int_t'):
                extra = 4
            if (last['type'] == '*int_t'):
                extra = 4*last['size']
            max_size[v['label']] = maxx+extra
    print('poiqwnceo', k, v, file=sys.__stdout__)
    return max_size





def get_offset(scopeDict):
    cunt = 0
    for s in scopeDict:
        cunt+=1

    offset = []
    offset = offset+[0]*(cunt)
    # print(cunt)
    print(cunt)
    var_offset = {}
    for i in range(cunt):
        if(i==0):
            continue
        maxx = 0
        last = {}
        for k , v  in scopeDict[i].table.items():
            var_offset[k] = offset[scopeDict[i].parent]+v['offset']
            maxx = offset[scopeDict[i].parent] + v['offset']
            last = v
        curr = i
        extra = 0
        if(last['type'] == 'int_t'):
            extra = 4
        if (last['type'] == '*int_t'):
            extra = 4*last['size']
        while(scopeDict[curr].parent != 0):
            offset[scopeDict[curr].parent]=maxx+extra
            curr = scopeDict[curr].parent
        offset[i]=maxx+extra
    print('poiqwnceo', k, v, file=sys.__stdout__) 
    # print(check_unique)       
    return var_offset