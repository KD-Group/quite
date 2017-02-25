import os
from quite import *


class CustomWidget(Widget):
    def paint(self, painter: Painter):
        w, _ = self.size
        painter.setFont(QFont("Courier New", 14.0))
        painter.draw_text_bottom_right(PointF(0, 0), "So Cool!")
        painter.draw_text_bottom_left(PointF(w, 0), "From Custom Widget")
        painter.end()


main_window = load_ui(filename=os.path.join(os.path.dirname(__file__), 'main_window.ui'))
main_window.set_central_widget(CustomWidget(parent=main_window))
main_window.exec()
