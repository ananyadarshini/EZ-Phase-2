def add_node(v):
    if v in graph:
        print(f"the given node {v} is already present in the graph")                                                                                                                                                          
    else:
        graph[v]=[]
def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,"is not present")
    if v2 not in graph:
        print(v2,"is not present")
    else:
        list1=[v2,cost]
        list2=[v1,cost]
        graph[v1].append(v2)
        graph[v2].append(v1)
def delete_node(v):
    if v not in graph:
        print(f"the given node {v} is not present in the graph")
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            if v in list1:
                list1.remove(v)
graph={}
print(graph)
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A","B",1)                          
add_edge("A","D",6)
add_edge("A","E",3)   
add_edge("A","C",2)
delete_node("B")
print(graph)
