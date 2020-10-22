class vehicle:
    no_of_wheel = ""
    no_of_lights = ""

    def indrotuceVehicle(self):
        print("I am a simple vehicle with " + self.no_of_wheel + " wheel\n" +"I have " + self.no_of_lights + " lights"  )

    def __add__(self, other):
        temp1 = self.no_of_lights + other.no_of_lights
        temp2 = self.no_of_wheel + other.no_of_wheel
        return [temp1, temp2]

trackters = vehicle()
trackters.no_of_lights =4
trackters.no_of_wheel = 4

trali = vehicle()
trali.no_of_wheel = 2
trali.no_of_lights = 2

trackterstrali = vehicle()
trackterstrali = trackters + trali
print(trackterstrali)