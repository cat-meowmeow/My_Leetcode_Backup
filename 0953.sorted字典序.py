class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words,key = lambda word:[order.index(i) for i in word])

'''
sorted 的参数 key 可传入一个函数，sorted 函数会将每个元素作为输入，输入到 key 函数并获得返回值，整个序列将按此值的大小来排序。
此处 key 函数为lambda w: [order.index(x) for x in w]，其为words中每个单词 word 返回一个 list，list 中每个元素为单词中字母 x 在 order 中的索引。
比如当 order 为 ‘abcde……’ 时，单词 ‘cba’ 将返回 [3, 2, 1]
'''

        hashmap={c:i for i,c in enumerate(order)}    # 获取每一个字母的字典序索引
        return words == sorted(words, key=lambda word: [hashmap[x] for x in word])  # 列表中的每一个单词排序，规则为word的每一个x(c)
