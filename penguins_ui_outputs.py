"""
Purpose: Display outputs for Penguins dataset.

Choose the correct ui method for the type of output you want to display.
Provide the exact name of the server function that will provide the output.

"""
from shiny import ui
from shinywidgets import output_widget




def get_penguins_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Filtered Penguins: Charts"),
            output_widget("penguins_output_widget1"),
            ui.tags.hr(),
            ui.h3("Filtered Penguins Table"),
            ui.output_text("penguins_record_count_string"),
            ui.output_table("penguins_filtered_table"),
            ui.tags.hr(),
        ),
    )
