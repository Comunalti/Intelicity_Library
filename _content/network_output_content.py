from andre import *


class NetworkOutputContent(FileContent):
    """
        representation of a line of a .txt file that is output of an Ai network\n
        \n
        exemple is:\n
        1 0.730469 0.719792 0.539062 0.48125 0.649228\n
        correspond to:\n
        [0] ai_object\n
        [1] screen_space_center_x\n
        [2] screen_space_center_y\n
        [3] screen_space_size_x\n
        [4] screen_space_size_y\n
        [5] trust\n
    """

    def __init__(self, ai_object: AiObject, screen_space_center_y: float, screen_space_center_x: float, screen_space_size_x: float,
                 screen_space_size_y: float,
                 trust: float):
        self.ai_object = ai_object
        self.screen_space_center_y = screen_space_center_y
        self.screen_space_center_x = screen_space_center_x
        self.screen_space_size_x = screen_space_size_x
        self.screen_space_size_y = screen_space_size_y
        self.trust = trust

    @classmethod
    def create_from_line(cls, string: str) -> "NetworkOutputContent":
        if not cls.validate_line(string):
            return None

        segments = string.split(" ")

        ai_object = AiObject.create_from_global_id(int(segments[0]))
        screen_space_center_y = int(segments[2])
        screen_space_center_x = int(segments[1])
        screen_space_size_x = int(segments[3])
        screen_space_size_y = int(segments[4])
        trust = float(segments[5])

        return cls(ai_object, screen_space_center_y, screen_space_center_x, screen_space_size_x, screen_space_size_y, trust)

    def __str__(self):
        return f"{self.ai_object.get_global_id()} {self.screen_space_center_x} {self.screen_space_center_y} {self.screen_space_size_x} {self.screen_space_size_y} {self.trust}"

    def convert_to_database(self, database_container: DatabaseContainer) -> DatabaseContent:
        (pixel_space_center_x, pixel_space_center_y, pixel_space_size_x, pixel_space_size_y) = NetworkOutputContent.convert_to_pixel_space(self.screen_space_center_x, self.screen_space_center_y, self.screen_space_size_x, self.screen_space_size_y)
        return DatabaseContent(self.ai_object, pixel_space_center_x, pixel_space_center_y, pixel_space_size_x, pixel_space_size_y, self.trust, database_container)
    @staticmethod
    def validate_line(string: str) -> bool:
        #todo: fazer essa função
        pass

    @staticmethod
    def convert_to_pixel_space(screen_space_center_x: float, screen_space_center_y: float, screen_space_size_x: float, screen_space_size_y: float) -> tuple[int,int,int,int]:
        #todo: fazer essa conta
        return 1,2,3,4

