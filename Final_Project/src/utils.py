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


# def get_max_offset(scopeDict,offset,fun_list):
#     s = scopeDict[0]
#     max_size = {}
#     last = {}
#     cunt = 0
#     for k , v in s.table.items():
#         if(v['type']=='func'):
#             max_size[v['label']] = offset[fun_list[cunt]]
#             cunt+=1
#     print('poiqwnceo', k, v, file=sys.__stdout__)
#     return max_size





def get_offset(scopeDict):
    cunt = 0
    for s in scopeDict:
        cunt+=1

    offset = []
    offset = offset+[0]*(cunt)
    fun_list = []
    # print(cunt)
    var_offset = {}
    for i in range(cunt):
        if(i==0):
            continue
        maxx = 0
        last = {}
        key = 0
        if(bool(scopeDict[i].table)==False):
            continue
        for k , v  in scopeDict[i].table.items():
            var_offset[k] = offset[scopeDict[i].parent]+v['offset']
            maxx = offset[scopeDict[i].parent] + v['offset']
            last = v
            key = k
        curr = i
        extra = 0
        # print('her',file=sys.__stdout__)
        # print(last,key,i,file=sys.__stdout__)



        if(last['type'] == 'int_t'):
            extra = 4
        if (last['type'] == '*int_t'):
            extra = 4*last['size']
        if(scopeDict[i].parent==0):
            fun_list.append(i)
        while(scopeDict[curr].parent != 0):
            offset[scopeDict[curr].parent]=maxx+extra
            curr = scopeDict[curr].parent
        offset[i]=maxx+extra

    s = scopeDict[0]
    max_size = {}
    last = {}
    cunt = 0
    for k , v in s.table.items():
        if(v['type']=='func'):
            max_size[v['label']] = offset[fun_list[cunt]]
            cunt+=1

    # print('poiqwnceo', k, v, file=sys.__stdout__) 
    # print(check_unique)       
    return var_offset,max_size
