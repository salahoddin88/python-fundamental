
class Home:

    def __init__(self):
        print('Random Song')
    
    
    def LivingRoom(self):
        print('Living Room')
    #methods 


class FirstFloor:

    def __init__(self):
        print('Welcome Song')

    def Gym(self):
        print('Gym')

    #methods 
    def Library(self):
        print('Library')



class GroundFloor(FirstFloor, Home):
    #methods 
    def MasterBedRoom(self):
        print('Master Bed Room')


groundFloor = GroundFloor()
groundFloor.Gym()
groundFloor.LivingRoom()
groundFloor.MasterBedRoom()