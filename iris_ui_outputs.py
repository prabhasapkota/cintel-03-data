"""
Purpose: Display outputs for Iris dataset.

Choose the correct ui method for the type of output you want to display.
Provide the exact name of the server function that will provide the output.
"""
from shiny import ui
from shinywidgets import output_widget


def get_iris_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Output (Reactive)"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Filtered Iris: Charts"),
            output_widget("iris_output_widget1"),
            ui.output_plot("iris_plot1"),
            ui.output_plot("iris_plot2"),
            ui.tags.hr(),
            ui.h3("Filtered Iris Table"),
            ui.output_text("iris_record_count_string"),
            ui.output_table("iris_filtered_table"),
            ui.tags.hr(),
        ),
    )