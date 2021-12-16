class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 直接用index找索引序号法：
        for i in range(len(s)):    #for循环写，比较多
            if [s.index(s[i])] == [t.index(t[i])]:
                return True
        return False
'''
有index函数遍历了，可以直接用map函数取代for循环，而且不用考虑s,t为空了
'''
        return list(map(s.index,s))==list(map(t.index,t))


        #哈希表字典法：
        hashmaps = {}
        hashmapt = {}
        for i in range(len(s)):
            if s[i] not in hashmaps: hashmaps[s[i]] = i  #分别记录两张表的值，如果一个表出现已有的字符，则值会不等
            if t[i] not in hashmapt: hashmapt[t[i]] = i
            
            if (hashmaps.get(s[i]) != hashmapt.get(t[i])): return False #get求对应键的值

        return True


        #一张表：
        hashtable={}
        for i in range(len(s)):
            if s[i] not in hashtable:
                if t[i] in list(hashtable.values()):
                    return False
                else:
                    hashtable[s[i]]=t[i]
            else:
                if hashtable[s[i]] != t[i]:
                    return False
        return True
