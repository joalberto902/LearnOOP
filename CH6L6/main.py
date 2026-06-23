class Sword:
    def __init__(self, sword_type: str) -> None:
        self.sword_type = sword_type
    def __add__(self, other: "Sword") -> "Sword":
        if (self.sword_type != other.sword_type 
            or self.sword_type == "steel"
            or other.sword_type == "steel"):
            raise Exception("cannot craft")
        if self.sword_type == "iron":
            return Sword("steel")
        if self.sword_type == "bronze":
            return Sword("iron")
