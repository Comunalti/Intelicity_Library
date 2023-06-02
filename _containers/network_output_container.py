from andre import *


class NetworkOutputContainer(Container):
    @classmethod
    def create_from_line_list(cls, lines: list[str]) -> "NetworkOutputContainer":
        contents = [NetworkOutputContent(line) for line in lines]
        return NetworkOutputContainer(contents)

    def __init__(self, contents: list[NetworkOutputContent]):
        super().__init__(contents)

    def concatenate(self, network_output_container: "NetworkOutputContainer") -> None:
        """
        concatenate 2 NetworkOutputContainer together on the first one
        """
        content: NetworkOutputContent
        for content in network_output_container.contents:
            self.contents.append(content)

    def convert_to_database_container(self, latitude: float, longitude: float):
        new_contents: list[DatabaseContent] = []

        database_container = DatabaseContainer(new_contents, latitude, longitude)

        content: NetworkOutputContent
        for content in self.contents:
            new_contents.append(content.convert_to_database(database_container))
        return database_container

    def add(self, network_output_content: NetworkOutputContent) -> None:
        self.contents.append(network_output_content)

    pass
