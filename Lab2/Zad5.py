# -*- utf-8 -*-

from treelib import Tree, Node
import time

# reachable_states = {"Gdansk": [["Gdynia", 24], ["Koscierzyna", 58], ["Tczew", 33], ["Elbląg", 63]],
#                     "Gdynia": [["Gdansk", 24], ["Lebork", 60], ["Wladyslawowo", 33]],
#                     "Elblag": [["Gdansk", 63], ["Tczew", 53]],
#                     "Hel": ["Wladyslawowo", 35],
#                     "Wladyslawowo": [["Leba", 66], ["Hel", 35], ["Gdynia", 42]],
#                     "Tczew": [["Koscierzyna", 59], ["Gdansk", 33], ["Elbląg", 53]],
#                     "Leba": [["Ustka", 64], ["Lebork", 29], ["Wladyslawowo", 66]],
#                     "Lebork": [["Leba", 29], ["Slupsk", 55], ["Koscierzyna", 58], ["Gdynia", 60]],
#                     "Koscierzyna": [["Chojnice", 70], ["Bytow", 40], ["Lebork", 58], ["Gdansk", 58], ["Tczew", 59]],
#                     "Ustka": [["Leba", 64], ["Slupsk", 21]],
#                     "Slupsk": [["Ustka", 21], ["Lebork", 55], ["Bytow", 70]],
#                     "Bytow": [["Slupsk", 70], ["Koscierzyna", 40], ["Chojnice", 65]],
#                     "Chojnice": [["Bytow", 65], ["Koscierzyna", 70]]}


def reachable_states(state):
    if state == "Gdansk":
        return [["Gdynia", 24], ["Koscierzyna", 58], ["Tczew", 33], ["Elblag", 63]]
    if state == "Gdynia":
        return [["Gdansk", 24], ["Lebork", 60], ["Wladyslawowo", 33]]
    if state == "Elblag":
        return [["Gdansk", 63], ["Tczew", 53]]
    if state == "Hel":
        return ["Wladyslawowo", 35]
    if state == "Wladyslawowo":
        return [["Leba", 66], ["Hel", 35], ["Gdynia", 42]]
    if state == "Tczew":
        return [["Koscierzyna", 59], ["Gdansk", 33], ["Elblag", 53]]
    if state == "Leba":
        return [["Ustka", 64], ["Lebork", 29], ["Wladyslawowo", 66]]
    if state == "Lebork":
        return [["Leba", 29], ["Slupsk", 55], ["Koscierzyna", 58], ["Gdynia", 60]]
    if state == "Koscierzyna":
        return [["Chojnice", 70], ["Bytow", 40], ["Lebork", 58], ["Gdansk", 58], ["Tczew", 59]]
    if state == "Ustka":
        return [["Leba", 64], ["Slupsk", 21]]
    if state == "Slupsk":
        return [["Ustka", 21], ["Lebork", 55], ["Bytow", 70]]
    if state == "Bytow":
        return [["Slupsk", 70], ["Koscierzyna", 40], ["Chojnice", 65]]
    if state == "Chojnice":
        return [["Bytow", 65], ["Koscierzyna", 70]]
    return []
def duplicate_node_path_check(tree, node):
    check_node = tree.get_node(node)
    current_node = check_node
    while not current_node.is_root():
        current_node = tree.parent(current_node.identifier)
        if check_node.tag == current_node.tag:
            return True
    return False
def breadth_first_search(start_state, target_state):
    # do budowy drzewa potrzebujemy dla kazdego wierzcholka id
    # bedziemy je pozniej inkrementowac
    id = 0
    # wrzucenie stanu startowego do drzewa (korzen) i kolejki
    tree = Tree()
    current_node = tree.create_node(start_state, id)
    fifo_queue = []
    fifo_queue.append(current_node)
    # petla szukajaca sciezki do stnau koncowego
    # robimy ograniczenie na max wierzcholkow (id<200000)
    while id < 200000:
        # jesli kolejka pusta to znaczy ze nie da sie dojsc do stanu koncowego
        # drukowanie kolejki: print(fifo_queue)
        if len(fifo_queue) == 0:
            tree.show()
            print("failed to reach the target state")
            return 1
        # jesli kolejka niepusta to wez pierwszy stan z kolejki
        current_node = fifo_queue[0]
        # jesli ten stan jest koncowy to zakoncz program z sukcesem
        if current_node.tag == target_state:
            tree.show()
            print("the target state "+str(current_node.tag)+" with id = "+str(current_node.identifier) +
                  "has been reached!")
            return 0
        # jesli stan niekoncowy to usun go z kolejki
        del(fifo_queue[0])
        # a nastepnie dodaj stany osiagalne z niego
        # na koniec kolejki i do drzewa
        if not duplicate_node_path_check(tree, id):
            for elem in reachable_states(current_node.tag):
                id += 1
                new_elem = tree.create_node(elem[0], id, parent=current_node.identifier)
                fifo_queue.append(new_elem)
                print("time limit exceeded")
print('def breadth_first_search')
start = time.time()
breadth_first_search("Gdansk", "Ustka")
end = time.time()
print(end - start)