import quite


class CustomWidget(quite.Widget):
    def paint(self, painter: quite.Painter):
        painter.setFont(quite.QFont("Courier New", 14.0))
        painter.draw_text_bottom_right(quite.PointF(0, 0), "Custom Widget")
        painter.end()

main_window = quite.MainWindow()
custom_widget = CustomWidget(parent=main_window)
main_window.set_central_widget(custom_widget)
main_window.exec()
