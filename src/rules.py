class Rules :

    @staticmethod
    def can_pose(before_card : tuple, submit_card : tuple):
        if before_card[0] != submit_card[0] and before_card[1] != submit_card[1]:
            return False
        return True
    
    @staticmethod
    def more2card(submit_card : tuple, stack : int):
        if submit_card[0] == 10 :
            return (True, (stack+1) * 2)
        else:
            return (False, stack * 2)

    @staticmethod
    def more4card(submit_card : tuple, stack : int):
        if submit_card[0] == 10 :
            return (True, (stack+1) * 2)
        else :
            return (False, stack*2)