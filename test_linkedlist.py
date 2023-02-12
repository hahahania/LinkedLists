import pytest
from linkedlist import LinkedList, Node


@pytest.mark.parametrize("test_input,expected", [([], ''), ([1, 2], '1-->2'), ([1, 2, 3], '1-->2-->3')])
def test_show_list(test_input, expected):
    ll = LinkedList()
    ll.insert_list(test_input)
    assert ll.show_list() == expected


@pytest.mark.parametrize("test_input,expected", [([], 0), ([1, 2], 2), ([1, 2, 3], 3)])
def test_list_length(test_input, expected):
    ll = LinkedList()
    ll.insert_list(test_input)
    assert ll.list_lenght() == expected


@pytest.mark.parametrize("test_input,expected", [([], None), ([1, 2], 2), (['str', 2, 3], 3)])
def test_add_at_the_beggining(test_input, expected):
    ll = LinkedList()
    for x in test_input:
        ll.add_at_the_beginning(x)
    assert expected == ll.get(0)


@pytest.mark.parametrize("test_input,expected", [([], None), ([1, 2], 2), ([1, 2, 3], 3)])
def test_add_at_the_end(test_input, expected):
    ll = LinkedList()
    for x in test_input:
        ll.add_at_the_end(x)
    assert ll.get(-1) == expected


@pytest.mark.parametrize("test_input,expected", [([1, 2], 1), ([4, 4], 4), ([2, 3], 2)])
def test_insert_at_index(test_input, expected):
    ll = LinkedList()
    ll.insert_list([1, 2, 3, 4])
    ll.insert_at_index(test_input[0], test_input[1])
    assert ll.get(test_input[1]) == expected


@pytest.mark.parametrize("test_input,expected", [(2, 4), (0, 2), (4, None)])
def test_delete_at_index(test_input, expected):
    ll = LinkedList()
    ll.insert_list([1, 2, 3, 4, 5])
    ll.delete_at_index(test_input)
    assert ll.get(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [([], []), ([1], [1]), ([1, 3, 40], [1, 3, 40])])
def test_insert_list(test_input, expected):
    ll = LinkedList()
    ll.insert_list(test_input)
    llist = []
    for x in range(len(test_input)):
        llist.append(ll.get(x))
    assert llist == expected


@pytest.mark.parametrize("test_input,expected", [(0, 1), (-1, 5), (3, 4)])
def test_get_index(test_input, expected):
    ll = LinkedList()
    ll.insert_list([1, 2, 3, 4, 5])
    assert ll.get(test_input) == expected
