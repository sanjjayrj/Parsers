# 1 ----------------- To Find Closure ----------------

def closure(I,nonT):
    J = I

    for item in J :
        #print(item)
        index = item[1].index('.')
        if(index<(len(item[1])-1) and item[1][index+1] in nonT):
            #print('item : ',item[1][index+1])
            for production in nonT[item[1][index+1]]:
                if( [item[1][index+1],str('.')+str(production)] not in J):
                    J.append([item[1][index+1],str('.')+str(production)])
                    #print([item[1][index+1],str('.')+str(production)])
    return J


# ------------------- Ends --------------------------------



# 2. --------------- Set of Canonical Items ---------------------

def setOfItems(start,nonTer,ter):
    I.append(closure([['start','.'+start+'$']],nonTer))
    #print(I)
    ter += list(nonTer.keys())
    #print("list of inputs : " , ter)
    for conI in I:
        for grammar in ter:
            if(grammar == '$'):
                continue
            #print("grammar : ",grammar)   
            goto = False
            goto1 = False
            shift = False
            shift1 = False
            reduce = False
            close = []
            for item in conI:
                #print("item  : ",item)
                if(item[1].index('.')<(len(item[1])-1) and item[1][item[1].index('.')+1] is grammar):
                    close.append([item[0],item[1][:item[1].index('.')]+grammar+'.'+item[1][item[1].index('.')+2:]])
                #else:
                #    print(item)
            #print("close : ",close)
            l = closure(close,nonTer)
            if(len(l) == 0):
                continue
            #print("closure : ", l)
            if(grammar in nonTer.keys()):
                goto1 = True
            else:
                shift1 = True
            if(l not in I):
                if(goto1):
                    state.append(['g',I.index(conI)+1,len(I)+1,grammar])
                    goto = True
                elif(shift1):
                    shift = True
                    state.append(['s',I.index(conI)+1,len(I)+1,grammar])
                I.append(l)

            else:
               if(goto1):
                    goto = True
                    state.append(['g',I.index(conI)+1,I.index(l)+1,grammar])
               elif(shift1):
                   shift = True
                   state.append(['s',I.index(conI)+1,I.index(l)+1,grammar])
                        

    
# -----------------------------------------------------------------



# 3. -----------------Create a Parse Table ------------------------

def toReduce(rule, accept, start):
    s = ['start',start+'.$']
    reduce = [ [] for _ in range(len(I)) ]
    for parState in I:
        #print(s,parState)
        if(s in parState):
            #print("here;")
            accept = I.index(parState)
        for item in parState:
            if( item in rule):
                reduce[I.index(parState)].append(rule.index(item))
    return accept, reduce

               

# ------------------------------------------------------------------



# 4. --------------------- To Parse --------------------------------

def createParseTable(parseTable, reduce, accept, Follow, rule):
    print(parseTable)
    print(reduce)
    print(Follow)
    print(rule)
    print(state)

    for i in state:
        parseTable[i[1]-1][symbolMap[i[3]]] = i[0]+str(i[2]-1)

    parseTable[accept][symbolMap['$']] = 'a'

    for i in reduce:
        if(len(i)>0):
            for j in Follow[rule[i[0]][0]]:
                parseTable[reduce.index(i)][symbolMap[j]] = 'r'+str(i[0])
    return parseTable

# (i) Stack -------------------------
class Stack:
    def __init__(self):
        self.__storage = []

    def isEmpty(self):
        return len(self.__storage) == 0

    def push(self,p):
        self.__storage.append(p)

    def pop(self):
        return self.__storage.pop()
    def top(self):
        return self.__storage[len(self.__storage) - 1]
    def length(self):
        return len(self.__storage)
    def __str__(self):
        """
        Because of using list as parent class for stack, our last element will
        be first for stack, according to FIFO principle. So, if we will use
        parent's implementation of str(), we will get reversed order of
        elements.
        """
        #: You can reverse elements and use supper `__str__` method, or 
        #: implement it's behavior by yourself.
        #: I choose to add 'stack' in the begging in order to differ list and
        #: stack instances.
        return 'stack [{}]'.format(', '.join([ str(i) for i in reversed(self.__storage) ]))

#--------------------Stack Defn ENDS ------------------------------------------
def parseString(parseTable, rule,string):
    try:
        index = 0
        flag = False
        st = Stack()
        st.push('0')
        while(index < len(string)):
            print(st , string , index , sep = '\t\t ')
            c = parseTable[int(st.top())][symbolMap[string[index]]][0]
            if(c == 'a'):
                flag = True
                break
            pt = parseTable[int(st.top())][symbolMap[string[index]]][1:]
            #print("point : ",pt)
            pt = int(pt)
            if( c == 'r'):
                l = len(rule[pt][1])
                l *= 2
                l -= 2 #'.' is also considered 
                if(l >= st.length()):
                    break
                else:
                    for i in range(l):
                        st.pop()
                    top = int(st.top())
                    st.push(rule[pt][0])
                    st.push(parseTable[top][symbolMap[st.top()]][1:])
            else:
                st.push(string[index])
                st.push(str(pt))
                index+=1
        return flag
    except Exception as e:
        print(e)
        return False    
        
# ------------------------------------------------------------------



# -----------------------First and Follow --------------------------

# (i) ------ First ---------
def first4pro(str):
    fir = []
    flag = False
    for i in str:
        if('@' not in First[i]):
            fir += First[i]
            flag = True
            break
        else:
            fir+=First[i]
            fir.remove('@')
    if(not flag):
        fir+=['@']

    return fir

def first(nT,nonT,checked):
    if(checked[nT]):
        return
    else:
        for i in nonT[nT]:
            #print("production" ,i)
            last = True
            for j in i:
                if(j is nT):
                    continue
                if(checked[j]):
                    if('@' not in First[j]):
                        First[nT] += First[j]
                        last = False
                        break
                    else:
                        First[nT] += First[j]
                        First[nT].remove('@')
                else:
                    first(j,nonT,checked)
                    if('@' not in First[j]):
                        First[nT] += First[j]
                        last = False
                        break
                    else:
                        First[nT] += First[j]
                        First[nT].remove('@')
            if(last):
                First[nT].append('@')
        checked[nT] = True
                    
        
              

def createFirst(ter , nonT ):
    checked = dict()
    # --- initialising the checked
    for i in ter:
        checked[i] = True
        First[i] = [i]
    for i in list(nonT.keys()):
        checked[i] = False
        First[i] = []

    #---- first --------
    for i in list(nonT.keys()):
        if(not checked[i]):
            first(i,nonT,checked)
            First[i] = list(set(First[i]))

    #(ii) ------- Follow------------

def follow(nT,nonT,checked):
    if(checked[nT]):
        return
    else:
        for i in nonT.keys():
            pro = list(nonT[i])
            for j in pro:
               # print(i," -- > ",pro , " to check ",nT , " from : ", j)
                if(nT in j):
                    ind = j.index(nT) + 1
                    while(ind<len(j)):
                        if('@' not in First[j[ind]]):
                            Follow[nT] += First[j[ind]]
                            break
                        else:
                            Follow[nT] += First[j[ind]]
                        ind+=1
                    if(ind == len(j)):
                        if(i == nT):
                            continue
                        follow(i,nonT,checked)
                        Follow[nT] += Follow[i]
        checked[nT] = True
            
    
    
def createFollow(ter , nonT ,S):
    checked = dict()
    # --- Initialising the checked ---
    for i in list(nonT.keys()):
        checked[i] = False
        Follow[i] = []
    Follow[S] = ['$']

    #calling the follow

    for i in list(nonT.keys()):
        if(not checked[i]):
            follow(i,nonT,checked)
            if(len(Follow[i]) == 0):
                checked[i] = False
    for i in list(nonT.keys()):
        Follow[i] = list(set(Follow[i]))
        if('@' in Follow[i]):
            Follow[i].remove('@')


#------------------------ First and Follow ends --------------------


# ---------------------------- Driver Program -------------------------

First = dict()
Follow = dict()
terminals = []
nonTerminals = dict()
symbolMap = dict()
rule = []
accept = -1
state = []
I = []

def slr_parser(prod, term, num_term, start_sym, query):
    terminals = term.split(",")[:num_term]
    
    for i in prod.replace(" ", "").split("\n"):
        nonTerminals[i.split("->")[0]] = i.split("->")[1].split("|")

    S = start_sym
    terminals+=['$']
    print("Productions : ")
    for i in nonTerminals.keys():
        print(i,"-->",end=' ')
        for j in nonTerminals[i]:
            print(j,end= ' | ')
        print()

    setOfItems(S,nonTerminals,terminals)
    print("canonicals Production : ")
    for count , i in enumerate(I):
        print(count+1 , i)

    print("state Transitions : ")
    for count , i in enumerate(state):
        print(count+1, i)

    for i in nonTerminals.keys():
        for j in nonTerminals[i]:
            rule.append([i,j+str('.')])

    print('rule :')
    for i in rule:
        print(i)

    # -------  To find the reduction rules - -- - -- ---
    accept, reduce = toReduce(rule, -1, S)

    print("reduce")
    for count,i in enumerate(reduce):
        print(count+1,i)

    print("accept : ",accept+1)

    # ---  - - - parse Table - -- -- - -- -- - -- - - -- -
    symbols = []
    symbols += terminals

    for count , i in enumerate(symbols):
        symbolMap[i] = count
    print(symbols)

    for i in nonTerminals.keys():
        terminals.remove(i)

    #-------------- First and Follow ----------
    createFirst(terminals,nonTerminals)
    createFollow(terminals,nonTerminals,S)


    parseTable = [ ['-' for i in range(len(symbols))] for j in range(len(I)) ]

    print("{}\t\t\t\t{}\t\t\t\t{}".format('Grammar Rule','First','Follow'))
    for i in nonTerminals.keys():
        print("{}\t\t\t\t{}\t\t\t\t{}".format(i,First[i],Follow[i]))

    #----------------------Done-------------------------------- 
    parseTable = createParseTable(parseTable, reduce, accept, Follow, rule)

    # ---Parse Table-----
    print('Parse Table') 
    print(" \t\t",end='')
    for i in symbols:
        print(i,end= '\t')
    print()
    for count,j in enumerate(parseTable):
        print(count,end='\t\t')
        for i in j:
            print(i,end='\t')
        print()

    query+='$'
    accepted = parseString(parseTable, rule, query)
    if(accepted):
        print("accepted")
    else:
        print("Not accepted")
    return [I, parseTable, accepted, symbols]

#------------------------------------------------------------------------


# Testings
if __name__ == '__main__':
    prod = "E -> E+T | T \n T -> T*F | F \n F -> (E) | # "
    term = "+,(,),*,@,#"
    print(prod.replace(" ", "").split("\n"))
    canonical, parsetable, First, Follow, accept = slr_parser(prod, term, 6, "E", "#+#*#")