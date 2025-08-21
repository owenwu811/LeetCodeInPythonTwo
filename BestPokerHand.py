#2347
#easy

#You are given an integer array ranks and a character array suits. You have 5 cards where the ith card has a rank of ranks[i] and a suit of suits[i].

#The following are the types of poker hands you can make from best to worst:

#"Flush": Five cards of the same suit.
#"Three of a Kind": Three cards of the same rank.
#"Pair": Two cards of the same rank.
#"High Card": Any single card.
#Return a string representing the best type of poker hand you can make with the given cards.

#Note that the return values are case-sensitive.


#correct python3 solution (could not solve):

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        c = Counter(ranks)
        #if 
        print(c.values())
        if len(set(suits)) == 1:
            return "Flush"
        ##    return "High Card"
        if max(c.values()) >= 3:
            return "Three of a Kind"
        if max(c.values()) >= 2:
            return "Pair"
        #if max(c.values()) == 5:
        #    return "Flush"
        return "High Card"
