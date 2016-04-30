__author__ = 'Timmy'
import random

#Problem 1
def CycD(bv):
    if bv[0]:
        return True
    else:
        return False
def Rb(bv):
    if (bv[5] and (not bv[0]) and (not bv[9])) or ((not bv[0]) and (not bv[3]) and (not bv[4]) and (not bv[9])):
        return True
    else:
        return False
def E2F(bv):
    if (bv[5] and (not bv[1]) and bv[9]) or ((not bv[1]) and (not bv[4]) and (not bv[9])):
        return True
    else:
        return False
def CycE(bv):
    if bv[2] and (not bv[1]):
        return True
    else:
        return False
def CycA(bv):
    if (bv[2] and (not bv[6]) and (not bv[1]) and (not (bv[7] and bv[8]))) or (bv[1] and bv[4] and bv[6] and (not(bv[7] and bv[8]))):
        return True
    else:
        return False
def p27(bv):
    if ((not bv[0]) and (not bv[3]) and (not bv[4]) and (not bv[9])) or (bv[5] and (not (bv[3] and bv[4])) and (not bv[9]) and bv[0]):
        return True
    else:
        return False
def Cdc20(bv):
    if bv[9]:
        return True
    else:
        return False
def Cdhl(bv):
    if ((not bv[4]) and (not bv[9])) or bv[6] or (bv[5] and (not bv[9])):
        return True
    else:
        return False
def UbcH10(bv):
    if (not bv[7]) or (bv[7] and bv[8] and (bv[4] or bv[6] or bv[9])):
        return True
    else:
        return False
def CycB(bv):
    if (not bv[6]) or (not bv[7]):
        return True
    else:
        return False
#S0=[CycD, Rb, E2F, CycE, CycA, p27, Cdc20, Cdhl, UbcH10, CycB]
def Generate_State_Transitions(s0, t):
    if t > 0:
        status = [CycD(s0), Rb(s0), E2F(s0), CycE(s0), CycA(s0), p27(s0), Cdc20(s0), Cdhl(s0), UbcH10(s0), CycB(s0)]
        t -= 1
        print status
        Generate_State_Transitions(status,t)

#Problem2
def pick():
    v = random.randint(0,1)
    if v == 0:
        return True
    else:
        return False
test = [pick(),pick(),pick(),pick(),pick(),pick(),pick(),pick(),pick(),pick()]
print "This is test"
print test
print
Generate_State_Transitions(test,20)

#This is the attractor cycles
#[True, False, False, False, False, False, True, True, True, True]
#[True, False, False, False, False, False, True, True, True, False]
#[True, False, True, False, False, False, False, True, True, False]
#[True, False, True, True, False, False, False, True, False, True]
#[True, False, False, True, True, False, True, False, False, True]
#

#Problem3
#Blooen nest work can also use at make schedule.
#need to consider about time aviable and event aviable.

