# 1 ----------------- To Find Closure ----------------

def closure(canonical,nonT):
    J = canonical
    # iterate through all the non terminals and add to canonical grammar
    for item in J :
        """
            Adding closure operator to the productions,
            and creating canonical grammar and appending to J,
            by iterating through production in base grammar
        """
        index = item[1].index('.')
        if(index<(len(item[1])-1) and item[1][index+1] in nonT):
            # iterates through all production of non terminal
            # and appends to list
            for production in nonT[item[1][index+1]]:
                if( [item[1][index+1],str('.')+str(production)] not in J):
                    J.append([item[1][index+1],str('.')+str(production)])
    return J


# ------------------- Ends --------------------------------



# 2. --------------- Set of Canonical Items ---------------------

def setOfItems(start,nonTer,ter):
    canonical.append(closure([['start','.'+start+'$']],nonTer))
    ter += list(nonTer.keys())
    # ter variable contains all the inputs acceptable by the grammar
    for conI in canonical:
        for symbol in ter:
            if(symbol == '$'):
                continue
            #print("grammar : ",grammar)
            goto = False
            shift = False
            close = []
            """
                iterating through all production rules,
                and moving the closure operator to the right.
            """
            for item in conI:
                if(item[1].index('.')<(len(item[1])-1) and item[1][item[1].index('.')+1] is symbol):
                    close.append([item[0],item[1][:item[1].index('.')] + symbol + '.' + item[1][item[1].index('.') + 2:]])

            l = closure(close,nonTer)
            if(len(l) == 0):
                continue
            """
                Based on where the keys are terminal or not, 
                the parse table is filled with shift values or goto respectively
                with the state number, and length of the canonical respectively,
                followed by that grammar
            """
            if(symbol in nonTer.keys()):
                goto = True
            else:
                shift = True
            if(l not in canonical):
                if(goto):
                    state.append(['G',canonical.index(conI)+1,len(canonical)+1,symbol])
                elif(shift):
                    state.append(['S',canonical.index(conI)+1,len(canonical)+1,symbol])
                canonical.append(l)

            else:
               if(goto):
                    state.append(['G',canonical.index(conI)+1,canonical.index(l)+1,symbol])
               elif(shift):
                   state.append(['S',canonical.index(conI)+1,canonical.index(l)+1,symbol])
                        

    
# -----------------------------------------------------------------



# 3. -----------------Create a Parse Table ------------------------

def toReduce(rule, accept,start):
    s = ['start',start+'.$']
    reduce = [ [] for i in range(len(canonical)) ]
    for parState in canonical:
        if(s in parState):
            #print("here;")
            accept = canonical.index(parState)
        for item in parState:
            if( item in rule):
                reduce[canonical.index(parState)].append(rule.index(item))

    return accept, reduce

               

# ------------------------------------------------------------------



# 4. --------------------- To Parse --------------------------------

def createParseTable(parseTable, reduce, accept,  ter):
    for i in state:
        parseTable[i[1]-1][symbolMap[i[3]]] = i[0]+str(i[2]-1)

    parseTable[accept][symbolMap['$']] = 'a'

    for i in reduce:
        if(len(i)>0):
            for j in ter:
                parseTable[reduce.index(i)][symbolMap[j]] = 'R'+str(i[0])
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
    print(symbolMap)
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
            pt = int(pt)
            if( c == 'R'):
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



# ---------------------------- Driver Program -------------------------
terminals = []
nonTerminals = dict()
rule = []
state = []
canonical = []
accept = -1
symbols = []
symbolMap = dict()

def lr_parser(prod, term, num_term, start_sym, query):
    terminals = term.lower().split(",")[:num_term]
    """
        Splitting non terminals from the input grammar
        and storing to dictionary with the non terminal
        as key.
    """
    for i in prod.replace(" ", "").split("\n"):
        nonTerminals[i.split("->")[0]] = i.split("->")[1].split("|")
    
    Start = start_sym
    terminals+=['$']

    print("Input Grammar:")
    for i in nonTerminals.keys():
        print(i,"->",end=' ')
        for j in nonTerminals[i]:
            print(j,end= ' | ')
        print()

    # creating canonical grammar tree
    setOfItems(Start,nonTerminals,terminals)
    print("canonicals Production : ")
    for count , i in enumerate(canonical):
        print(count+1 , i)

    print("State Transition Values: ")
    for count , i in enumerate(state):
        print(count+1, i)

    for i in nonTerminals.keys():
        for j in nonTerminals[i]:
            rule.append([i,j+str('.')])

    print('Final Rule:')
    for i in rule:
        print(i)

    # -------  To find the reduction rules - -- - -- ---
    reduce = [ [] for _ in range(len(canonical)) ]
    accept, reduce = toReduce(rule,-1,Start)

    print("reduce")
    for count,i in enumerate(reduce):
        print(count+1,i)

    print("accept : ",accept+1)

    # ---  - - - parse Table - -- -- - -- -- - -- - - -- -
    symbols = []
    symbols += terminals

    for count , i in enumerate(symbols):
        symbolMap[i] = count
    print(symbolMap)
    for i in nonTerminals.keys():
        terminals.remove(i)

    parseTable = [ ['-' for _ in range(len(symbols))] for _ in range(len(canonical)) ]
    parseTable = createParseTable(parseTable, reduce, accept, terminals)

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
    return [canonical, parseTable, accepted, symbols]

#------------------------------------------------------------------------


# Testings
if __name__ == '__main__':
    prod = "E -> E+T | T \n T -> T*F | F \n F -> (E) | #"
    term = "+,(,),*,@,#"
    #print(prod.replace(" ", "").split("\n"))
    canonical, parsetable, accept, symbols = lr_parser(prod, term, 6, "E", "#+#*#")
