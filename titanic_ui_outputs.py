from shiny import ui
from shinywidgets import output_widget


def get_titanic_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Filtered Titanic: Charts"),
            output_widget("titanic_output_widget1"),
            ui.tags.hr(),
            ui.h3("Filtered Titanic Table"),
            ui.output_text("titanic_record_count_string"),
            ui.output_table("titanic_filtered_table"),
            ui.tags.hr(),
        ),
    )