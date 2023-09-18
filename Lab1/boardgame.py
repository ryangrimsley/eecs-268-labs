

class BoardGame:
    def __init__(self, name, gibbons_rating, public_rating, year, min_players, max_playtime):
        self.name = name
        self.year = year
        self.gibbons_rating = gibbons_rating
        self.public_rating = public_rating
        self.min_players = min_players
        self.max_playtime = max_playtime

    def __repr__(self):
        return f"BoardGame({self.name},{self.gibbons_rating},{self.public_rating},{self.year},{self.min_players},{self.max_playtime})"

    def __str__(self):
        return f"{self.name} ({self.year}) [GR={self.gibbons_rating},PR={self.public_rating},MP={self.min_players},MT={self.max_playtime}]"

    def __lt__(self,other):
        if self.gibbons_rating < other.gibbons_rating:
            return True
        else:
            return False

    def __gt__(self,other):
        if self.gibbons_rating > other.gibbons_rating:
            return True
        else:
            return False

    def __ge__(self,other):
        if self.gibbons_rating >= other.gibbons_rating:
            return True
        else:
            return False

    def __le__(self,other):
        if self.gibbons_rating <= other.gibbons_rating:
            return True
        else:
            return False

    def __eq__(self,other):
        if self.gibbons_rating == other.gibbons_rating:
            return True
        else:
            return False

    def __ne__(self,other):
        if self.gibbons_rating != other.gibbons_rating:
            return True
        else:
            return False
