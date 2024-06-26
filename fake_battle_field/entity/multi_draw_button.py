from image_shape.non_background_image import NonBackgroundImage
from pre_drawed_image_manager.pre_drawed_image import PreDrawedImage

class MultiDrawButton:
    __pre_drawed_image_instance = PreDrawedImage.getInstance()

    def __init__(self, local_translation=(0, 0), scale=1):
        self.multi_draw_button = None
        self.local_translation = local_translation
        self.scale = scale

        self.total_width = None
        self.total_height = None

        self.width_ratio = 1
        self.height_ratio = 1

    def set_total_window_size(self, width, height):
        self.total_width = width
        self.total_height = height

    def set_width_ratio(self, width_ratio):
        self.width_ratio = width_ratio

    def set_height_ratio(self, height_ratio):
        self.height_ratio = height_ratio

    def get_multi_draw_button(self):
        return self.multi_draw_button

    def change_local_translation(self, _translation):
        self.local_translation = _translation

    def create_multi_draw_button(self, image_data, vertices):
        self.multi_draw_button = NonBackgroundImage(image_data=image_data,
                                                       vertices=vertices)

    def init_multi_draw_button(self):
        left_x_point = self.total_width * 0.783
        right_x_point = self.total_width * 0.848
        top_y_point = self.total_height * 0.668
        bottom_y_point = self.total_height * 0.741

        self.create_multi_draw_button(
            # TODO -> Battle Field Background로 변경 (이미지 준비되면)
            image_data=self.__pre_drawed_image_instance.get_pre_draw_multi_draw_button(),
            vertices=[
                (left_x_point, top_y_point),
                (right_x_point, top_y_point),
                (right_x_point, bottom_y_point),
                (left_x_point, bottom_y_point)
            ])

    def is_point_inside_multi_draw_button(self, point):
        point_x, point_y = point
        point_y *= -1

        muligun_reset_button = self.get_multi_draw_button()

        translated_vertices = [
            (x * self.width_ratio + muligun_reset_button.local_translation[0] * self.width_ratio, y * self.height_ratio + muligun_reset_button.local_translation[1] * self.height_ratio)
            for x, y in muligun_reset_button.get_vertices()
        ]

        if not (translated_vertices[0][0] <= point_x <= translated_vertices[2][0] and
                translated_vertices[1][1] <= point_y <= translated_vertices[0][1]):
            print("multi draw button click -> False")
            return False

        print("multi draw button click -> True")
        return True
