from project.player.player import Player


class Beginner(Player):
    def __init__(self, username):
        super().__init__(username, health=50)


b = Beginner("Daniel")

print(b.username)
print(b.health)