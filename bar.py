class Bar:
    def __init__(self):
        self.chart_title = ""
        self.bar_count = 0
        self.gridline_interval = 0
        self.y_label = ""
        self.bars = {}

    def set_chart_title(self, chart_title):
        self.chart_title = chart_title

    def bar_count_prompt(self):
        bar_count = int(input("Enter the number of bars (2 to 6): "))
        if bar_count < 2 or bar_count > 6:
            print("Invalid number of bars. Please enter a number between 2 and 6")
            self.bar_count_prompt()
        self.bar_count = bar_count

    def gridline_interval_prompt(self):
        gridline_interval = int(input("Enter the gridline interval (10 to 100): "))
        if gridline_interval < 10 or gridline_interval > 100:
            print("Invalid gridline interval. Please enter a number between 10 to 100")
            self.gridline_interval_prompt()
        self.gridline_interval = gridline_interval

    def label_y_prompt(self):
        y_label = input("Enter the label for the Y-Axis: ")
        self.y_label = y_label

    def bar_label_value_prompt(self):
        for current_count in range(0, self.bar_count):
            label = input("Label bar {0}: ".format(current_count+1))
            self.bars[label] = input("Enter the value of bar {0}: ".format(label))

    def create_chart(self):
        import SimpleGraphics
        colours = [
            (255, 0, 0),
            (0, 255, 0),
            (255, 160, 122),
            (255, 255, 0),
            (0, 255, 255),
            (128, 0, 0),
            (0, 128, 128),
            (255, 69, 0),
            (184, 134, 11),
            (173, 255, 47)
        ]
        # Chart Title
        SimpleGraphics.setWindowTitle(self.chart_title)
        SimpleGraphics.text(400, 20, self.chart_title)

        # Chart Canvas
        SimpleGraphics.setFill(255,255,255)
        canvas_x = 100
        canvas_y = 50
        canvas_width = 600
        canvas_height = 400
        SimpleGraphics.rect(canvas_x,canvas_y, canvas_width, canvas_height)

        # Y Label
        y_label_x = 50
        y_label_y = 250
        SimpleGraphics.text(y_label_x, y_label_y, self.y_label)

        # Grid Lines
        line_x1 = 100
        line_x2 = 700

        for line_y2 in range(450,60, -self.gridline_interval):
            SimpleGraphics.line(line_x1, line_y2, line_x2, line_y2)

        # Scale
        text_x = 720
        text_y = self.gridline_interval

        for scale in range(self.gridline_interval*int(400/(self.gridline_interval)),-1 ,-self.gridline_interval):
            SimpleGraphics.text(text_x,text_y,scale)
            text_y += self.gridline_interval

        # Graph
        bar_x = 120
        bar_y = 50
        bar_index = 0
        space = canvas_width / (5*self.bar_count)
        bar_width = (canvas_width - (bar_x+space) ) / self.bar_count

        for bar_value, bar_height in self.bars.items():
            bar_height = int(bar_height)
            bar_y += (canvas_height - bar_height)
            SimpleGraphics.setFill(colours[bar_index][0], colours[bar_index][1],colours[bar_index][2],)
            SimpleGraphics.rect(bar_x, bar_y, bar_width, bar_height)
            SimpleGraphics.text(bar_x+(bar_width/2),bar_y+10,bar_height)
            SimpleGraphics.text(bar_x+(bar_width/2),canvas_height+75,bar_value)
            bar_y = 50
            bar_x += (bar_width + space)
            bar_index +=1

        print("Your chart is completed.")


