from abc import abstractmethod
class Selection():
    def get_sel(num, top, ran):
        if num == 0 :
            return Top50(top)
        elif num == 1:
            return Tournament(ran)

    @abstractmethod
    def choose_parent(self, females):
        pass

class Top50(Selection):
    def __init__(
        self,
        top
    ):
        super().__init__()
        self.top = top

    def choose_parent(self, females):
        """
        Choose the top ?% of females as the parent
        """
        females.sort(reverse=True)
        parent = []
        for x in range(int(len(females)*self.top)):
            parent.append(females[x])
        return parent


class Tournament(Selection):
    def __init__(
        self,
        ran
    ):
        super().__init__()
        self.ran = ran

    def choose_parent(self, females):
        """
        Use the tournament selection to choose parent
        """
        self.females.sort(reverse=True)
        parent = []
        for x in range(int(len(females)/2)):
            index1 = self.ran.ranInt(len(females))
            index2 = self.ran.ranInt(len(females))
            if(index1 == index2):
                index2 = self.ran.ranInt(len(females))
            if(females[index1].fitness >= females[index2].fitness):
                parent.append(females[index1])
            else:
                parent.append(females[index2])
        return parent