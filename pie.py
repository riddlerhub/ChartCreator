

class Pie:
    def __init__(self):
        self.chart_title = ""
        self.sector_count = 0
        self.sector_total_value = 0
        self.sectors = {}

    def set_chart_title(self, chart_title):
        self.chart_title = chart_title

    def sector_count_prompt(self):
        sector_count = int(input("Enter the number of sectors (2 to 6): "))
        if sector_count < 2 or sector_count > 6:
            print("Invalid number of sectors. Please enter a number between 2 and 6")
            self.sector_count_prompt()
        self.sector_count = sector_count

    def sector_total_value_prompt(self):
        sector_total_value = int(input("Enter the total value of all sectors: "))
        self.sector_total_value = sector_total_value

    def sector_labels_and_value_prompt(self):
        for current_count in range(0, self.sector_count):
            label = input("Label sector {0}: ".format(current_count+1))
            while label == "":
                print("Label cannot be empty!")
                label = input("Label sector {0}: ".format(current_count + 1))
            if label != "":
                if current_count == self.sector_count-1:
                    value = 360 - sum(self.sectors.values())
                else:
                    value = int(input("Enter the value of the {0} sector: ".format(label)))
                if sum(self.sectors.values()) < 360:
                    if current_count == self.sector_count-1:
                        self.sectors[label] = value
                    else:
                        self.sectors[label] = (value/self.sector_total_value) * 360
                    label = ""
                    value = 0

    def create_chart(self):
        colours = [
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 128),
            (255, 255, 0),
            (0, 255, 255),
            (128, 0, 0)
        ]
        import SimpleGraphics
        SimpleGraphics.setWindowTitle(self.chart_title)
        SimpleGraphics.text(400, 20, self.chart_title)
        x = 200
        y = 40
        width = 400
        height = 400
        SimpleGraphics.ellipse(x,y,width, height)  # Drawing Canvas
        SimpleGraphics.setFill(0,0,0)  # Set colour as Black
        prev_angle = 0
        #  Drawing Pie Slices
        for index, value in enumerate(self.sectors.values()):
            if index != 0:
                s = prev_angle
            else:
                s = 0
            e = value
            prev_angle = s+e
            SimpleGraphics.setFill(colours[index][0], colours[index][1], colours[index][2])
            SimpleGraphics.pieSlice(x,y,width,height,s,e)

        #  Legend Settings
        legend_item_x = 700  # Default Legend Item X Position
        legend_text_x = 720  # Default Legend Item Y Position
        legend_item_y = 100  # Default Legend Text X Position
        legend_text_y = 150  # Default Legend Text Y Position

        for index,key in enumerate(self.sectors.keys()):
            SimpleGraphics.setFill(colours[index][0], colours[index][1], colours[index][2])
            SimpleGraphics.rect(legend_item_x,legend_item_y, 40,40)
            SimpleGraphics.text(legend_text_x, legend_text_y, key)
            legend_text_y += 60
            legend_item_y +=60

    print("Your chart is completed.")



