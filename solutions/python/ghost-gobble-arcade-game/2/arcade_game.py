"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    if(power_pellet_active == True & touching_ghost == True):
        return True 
    else:
        return False 
 
eat_ghost(False,True)


def score(touching_power_pellet, touching_dot):
    if(touching_power_pellet == True or touching_dot == True):
        return True 
    else:
        return False
   
score(True, True)


def lose(power_pellet_active, touching_ghost):
    if(touching_ghost == True and power_pellet_active == False):
        return True
    else:
        return False
 
lose(False, True)

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if(has_eaten_all_dots == True):
        if(power_pellet_active == True and touching_ghost == True):
            return True 
        elif(power_pellet_active == False and touching_ghost == False):
            return True
        elif(power_pellet_active == False and touching_ghost == True):
            return False
    else:
        return False
    
win(False, True, False)
