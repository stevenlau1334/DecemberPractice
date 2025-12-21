class Animal:
    noise = "Rrrr"
    color = "Red"

    def make_noise(self):
        print(f"{self.noise}")
    def set_noise(self, new_noise):
        self.noise = new_noise
    def get_color(self):
        return self.noise
    def set_solor(self, new_color):
        self.new_noise = new_color
        return self.color
    
class Wolf(Animal):
    noise = "grrrr"

class BabyWolf(Wolf):
    color = "yellow"