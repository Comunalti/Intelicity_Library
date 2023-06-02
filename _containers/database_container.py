from containers import *


class DatabaseContainer(Container):

    @classmethod
    def create_from_line_list(cls, lines: list[str]) -> "DatabaseContainer":
        contents = [DatabaseContent(line) for line in lines]
        latitude = float(lines[0].split(" ")[7])
        longitude = float(lines[0].split(" ")[8])

        return cls(contents, latitude, longitude)

    @classmethod
    def create_from_values(cls, lines: list[str], latitude: float, longitude: float) -> "DatabaseContainer":
        contents = [DatabaseContent(line) for line in lines]
        latitude = latitude
        longitude = longitude

        return cls(contents, latitude, longitude)

    def __init__(self, contents: list[DatabaseContent], latitude: float, longitude: float):
        super().__init__(contents)
        self.latitude = latitude
        self.longitude = longitude

    def concatenate(self, database_container: "DatabaseContainer") -> None:
        """
        concatenate 2 DatabaseContainers together on the first one
        """
        for content in database_container.contents:
            self.contents.append(content)

    def convert_to_network_output_container(self, screen_width, screen_height):
        new_contents: list[NetworkOutputContent] = []

        network_output_container = NetworkOutputContainer(new_contents)

        content: DatabaseContent
        for content in self.contents:
            converted_content = content.convert_to_network_output(screen_width, screen_height)
            new_contents.append(converted_content)
        return network_output_container

    def add(self, databaseContent: DatabaseContent) -> None:
        self.contents.append(databaseContent)
