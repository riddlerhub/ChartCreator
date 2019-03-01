import pie,bar
pie = pie.Pie()
bar = bar.Bar()


def chart_selection_prompt():
    user_choice = 0
    print("Please choose a Chart: \n1. Pie Chart\n2. Bar Chart")
    user_choice = int(input("Select your Preference : "))
    if (user_choice != 1) and (user_choice != 2):
        print(user_choice)
        print("Wrong Choice! Try Again..\n")
        chart_selection_prompt()
    return user_choice


def chart_title_prompt():
    chart_title = input("Enter the title of the chart: ") #  Gets Chart Title as a string
    return chart_title


def startup():
    print("Chart Creator Version 1.0")
    print("--------------------------")
    user_choice = chart_selection_prompt()  # Prompts the user to select the chart
    chart_title = chart_title_prompt()  # Prompts user to input a chart title
    if user_choice == 1:  # User Selects to draw a Pie Chart
        pie.set_chart_title(chart_title)
        pie.sector_count_prompt()  # Prompts user to enter the number of sectors
        pie.sector_total_value_prompt()  # Prompts user to enter total value of Sectors
        pie.sector_labels_and_value_prompt()  # Prompts user to enter sector names and values
        pie.create_chart()
    if user_choice == 2:
        bar.set_chart_title(chart_title)
        bar.bar_count_prompt()
        bar.gridline_interval_prompt()
        bar.label_y_prompt()
        bar.bar_label_value_prompt()
        bar.create_chart()




if __name__ == "__main__":
    startup()
    # pie.chart_title = "Fruit"
    # pie.sector_count = 4
    # pie.sector_total_value = 240
    # pie.sectors = {
    #     "Orange": 225,
    #     "Apple": 75,
    #     "Banana": 30,
    #     "Others": 30
    # }
    # pie.create_chart()
    # bar.chart_title = "​Jacket Sales in Q1 of 2019"
    # bar.bar_count = 4
    # bar.gridline_interval = 50
    # bar.y_label = "Sales"
    # bar.bars = {
    #     "Jan" : 380,
    #     "Feb" : 250,
    #     "Mar" : 200,
    #     "Apr" : 50,
    # }
    # bar.create_chart()
