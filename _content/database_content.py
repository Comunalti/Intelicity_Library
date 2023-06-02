from andre import *


class DatabaseContent(FileContent):
    """
        representation of a line of a .txt file that is output of an Ai network\n
        \n
        Example is:\n
        1 933 675 671 466 0.704676 Valeta -23.6383339 -46.7367179\n
        Correspond to:\n
        [0] ai_object\n
        [1] pixel_space_center_x \n
        [2] pixel_space_center_y\n
        [3] pixel_space_size_x\n
        [4] pixel_space_size_y\n
        [5] trust\n
        [6] ai_object_name\n
        [7] latitude\n
        [8] longitude\n
    """
    @classmethod
    def create_from_line(cls, string: str, database_container : DatabaseContainer):
        if not cls.validate_line(string):
            return

        segments = string.split(" ")

        ai_object = AiObject.create_from_global_id(int(segments[0]))
        pixel_space_center_x = int(segments[1])
        pixel_space_center_y = int(segments[2])
        pixel_space_size_x = int(segments[3])
        pixel_space_size_y = int(segments[4])
        trust = float(segments[5])

        database_container = database_container

        # ignore the last part of the line, redundant information
        # self.ai_object_name = segments[6]
        # self.latitude = float(segments[7])
        # self.longitude = float(segments[7])

        return cls(ai_object,pixel_space_center_x,pixel_space_center_y,pixel_space_size_x,pixel_space_size_y,trust,database_container)

    def __init__(self, ai_object: AiObject, pixel_space_center_x: int, pixel_space_center_y: int, pixel_space_size_x: int, pixel_space_size_y: int, trust: float, database_container: DatabaseContainer):
        self.ai_object = ai_object
        self.pixel_space_center_x = pixel_space_center_x
        self.pixel_space_center_y = pixel_space_center_y
        self.pixel_space_size_x = pixel_space_size_x
        self.pixel_space_size_y = pixel_space_size_y
        self.trust = trust
        self.database_container = database_container

    def get_ai_object_name(self):
        return AiObject.get_object_name(ai_id=self.ai_object.ai_id)

    def get_latitude(self):
        return self.database_container.latitude

    def get_longitude(self):
        return self.database_container.longitude

    def __str__(self):
        return f"{self.ai_object.get_global_id()} {self.pixel_space_center_x} {self.pixel_space_center_y} {self.pixel_space_size_x} {self.pixel_space_size_y} {self.trust} {self.get_ai_object_name()} {self.get_latitude()} {self.get_longitude()}"

    def get_pixel_space_xyxy(self) -> tuple[int, int, int, int]:
        # todo: convert screen space size and center to xyxy
        ...


    @staticmethod
    def validate_line(string: str) -> bool:
        # todo: evaluate if try catch is better
        ...

    def convert_to_network_output(self) -> NetworkOutputContent:
        (screen_space_center_x, screen_space_center_y, screen_space_size_x, screen_space_size_y) = DatabaseContent.convert_to_screen_space(self.pixel_space_center_x, self.pixel_space_center_y, self.pixel_space_size_x, self.pixel_space_size_y)
        return NetworkOutputContent(self.ai_object,screen_space_center_x, screen_space_center_y, screen_space_size_x, screen_space_size_y, self.trust)

    @staticmethod
    def convert_to_screen_space(pixel_space_center_x, pixel_space_center_y, pixel_space_size_x, pixel_space_size_y) -> tuple[float,float,float,float]:
       #todo: fazer esse metodo
        pass


