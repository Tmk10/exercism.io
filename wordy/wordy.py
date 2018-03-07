def calculate(question):
    operator_count=[]
    digits_count=0
    operators={"plus":"+","minus":"-","multiplied":"*","divided":"/"}
    question = question.replace("?","").split()
    result=[]
    for word in question:
        if word in operators:
            result.append(operators[word])
            operator_count.append(operators[word])
        elif word.startswith("-"):
            result.append(word)
            digits_count+=1
        elif word.isdigit():
            result.append(word)
            digits_count+=1
    if digits_count-len(operator_count) !=1 or len(operator_count) ==0:
        raise ValueError("Error in question")
    if len(operator_count) >1:
        result.insert(0,"(")
        result.insert(result.index(operator_count[1]),")")
    return int(eval("".join(result)))
