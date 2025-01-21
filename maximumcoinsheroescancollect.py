
#2838
#medium

#There is a battle and n heroes are trying to defeat m monsters. You are given two 1-indexed arrays of positive integers heroes and monsters of length n and m, respectively. heroes[i] is the power of ith hero, and monsters[i] is the power of ith monster.

#The ith hero can defeat the jth monster if monsters[j] <= heroes[i].

#You are also given a 1-indexed array coins of length m consisting of positive integers. coins[i] is the number of coins that each hero earns after defeating the ith monster.

#Return an array ans of length n where ans[i] is the maximum number of coins that the ith hero can collect from this battle.

#Notes

#The health of a hero doesn't get reduced after defeating a monster.
#Multiple heroes can defeat a monster, but each monster can be defeated by a given hero only once.
 

#Example 1:

#Input: heroes = [1,4,2], monsters = [1,1,5,2,3], coins = [2,3,4,5,6]
#Output: [5,16,10]
#Explanation: For each hero, we list the index of all the monsters he can defeat:
#1st hero: [1,2] since the power of this hero is 1 and monsters[1], monsters[2] <= 1. So this hero collects coins[1] + coins[2] = 5 coins.
#2nd hero: [1,2,4,5] since the power of this hero is 4 and monsters[1], monsters[2], monsters[4], monsters[5] <= 4. So this hero collects coins[1] + coins[2] + coins[4] + coins[5] = 16 coins.
#3rd hero: [1,2,4] since the power of this hero is 2 and monsters[1], monsters[2], monsters[4] <= 2. So this hero collects coins[1] + coins[2] + coins[4] = 10 coins.
#So the answer would be [5,16,10].


#my own solution using python3:

#keep two dictionaries to track the sum of the prices so far and also mapping the monster to the award, and then binary search on the monsters array for each heroes element

class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        d = defaultdict(list)
        for i, m in enumerate(monsters):
            d[m].append(coins[i])
        d = dict(sorted(d.items(), key=lambda x: x[0]))
        res = []
        print(d)
        #{1: [2, 3], 2: [5], 3: [6], 5: [4]}
        sumd = dict()
        sumuptothispoint = 0
        for k in d:
            sumuptothispoint += sum(d[k])
            sumd[k] = sumuptothispoint
        print(sumd)
        #{1: 5, 2: 10, 3: 16, 5: 20}
        #heroes = [1,4,2], monsters = [1,1,5,2,3], coins = [2,3,4,5,6]
        monsters.sort()
        #[1, 4, 2], [1, 1, 2, 3, 5]
        print(heroes)
        print(monsters)
        for h in heroes:
            l, r = 0, len(monsters) - 1
            possible = 0
            while l <= r:
                mid = (l + r) // 2
                if monsters[mid] > h:
                    r = mid - 1
                else:
                    #print(monsters[mid])
                    possible = max(possible, monsters[mid])
                    l = mid + 1
            print(possible)
            if possible in sumd:
                res.append(sumd[possible])
            else:
                res.append(0)

            print("nextturn!")
        return res
