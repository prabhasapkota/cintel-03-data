"""
Purpose: Display outputs for MT Cars dataset.

Choose the correct ui method for the type of output you want to display.
Provide the exact name of the server function that will provide the output.
"""
from shiny import ui
from shinywidgets import output_widget




def get_mtcars_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Filtered Cars: Charts"),
            output_widget("mtcars_output_widget1"),
            ui.output_plot("mtcars_plot1"),
            ui.output_plot("mtcars_plot2"),
            ui.tags.hr(),
            ui.h3("Filtered MT Cars Table"),
            ui.output_text("mtcars_record_count_string"),
            ui.output_table("mtcars_filtered_table"),
            ui.tags.hr(),
        ),
    )
