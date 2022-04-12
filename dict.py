
# book={
# 1:"python programming",
# 2:"core python programming",
#'A':"advance python programming"
# }
# print(book[2])#core python programming
# print(book[23])#KeyError:23

# h={1:"",2: "python", 3: 7, 4: 6.2,
# 5: [1,4], 6: (4,3),7: {1,2},
# 8: {3: "world"}}
# print(h[1],type(h[1]))#str
# print(h[2],type(h[2]))#python str
# print(h,type(h))#{1:"",2: "python", 3: 7, 4: 6.2,5: [1,4], 6: (4,3),7: {1,2},8: {3: "world"}} dict
# print(h.keys())#dict_keys([1,2,3,4,5,6,7,8])
# print(h.values())#dict_values(['', 'python', 7, 6.2, [1, 4], (4, 3), {1, 2}, {3: 'world'}])
# print(h.items())#dict_items([(1, ''), (2, 'python'), (3, 7), (4, 6.2), (5, [1, 4]), (6, (4, 3)), (7, {1, 2}), (8, {3: 'world'})])

# k={1:"",2: "python",3: 7, 4: 6.2,
# 5: [1,4], 6: (4,3),7: {1,2}, 8: {3: "world"}}
# k.clear()
# print(k)#{}

# a=[101,102,103,104,105]
# b=dict.fromkeys(a)
# print(b,type(b))#{101: None, 102: None, 103: None, 104: None, 105: None} dict
# print(dict.fromkeys(a,23))#{101: 23, 102: 23, 103: 23, 104: 23, 105: 23}

# h={1:"",2: "python", 3: 7, 4: 6.2,
# 5: [1,4], 6: (4,3),7: {1,2},8: {3: "world"}}
# print(h[2])#python
# print(h[24])#KeyError:24
# print(h.get(2))#python
# print(h.get(23))#None
# h.pop(4)
# print(h)#{1: '', 2: 'python', 3: 7, 5: [1, 4], 6: (4, 3), 7: {1, 2}, 8: {3: 'world'}}
# h.pop()
# print(h)#TypeError:pop executed al least 1 argument,got 0
# h.popitem()
# print(h)#{1: '', 2: 'python', 3: 7, 4: 6.2, 5: [1, 4], 6: (4, 3), 7: {1, 2}}

# h={1:"",2: "python", 3: 7, 4: 6.2,
# 5: [1,4], 6: (4,3),7: {1,2},8: {3: "world"}}
# h.update({8: 'core python'})
# print(h)#{1: '', 2: 'python', 3: 7, 4: 6.2, 5: [1, 4], 6: (4, 3), 7: {1, 2}, 8: 'core python'}
# h.update({9: 'advance python'})
# print(h)#{1: '', 2: 'python', 3: 7, 4: 6.2, 5: [1, 4], 6: (4, 3), 7: {1, 2}, 8: {3: 'world'}, 9: 'advance python'}

# h={1:"",2: "python", 3: 7, 4: 6.2,
# 5: [1,4], 6: (4,3),7: {1,2},8: {3: "world"}}
# h.setdefault(8, 'devops')
# print(h)#{1: '', 2: 'python', 3: 7, 4: 6.2, 5: [1, 4], 6: (4, 3), 7: {1, 2}, 8: {3: 'world'}}
# h.setdefault(10, 'devops')
# print(h)#{1: '', 2: 'python', 3: 7, 4: 6.2, 5: [1, 4], 6: (4, 3), 7: {1, 2}, 8: {3: 'world'}, 10: 'devops'}

# print(dir(dict))#['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# print(len(['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'])) #11






