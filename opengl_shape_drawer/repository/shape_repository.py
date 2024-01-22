import abc


class ShapeRepository(abc.ABC):
    @abc.abstractmethod
    def create_rectangle(self, color, vertices):
        pass

    # @abc.abstractmethod
    # def process_border(self, is_draw_border):
    #     pass


