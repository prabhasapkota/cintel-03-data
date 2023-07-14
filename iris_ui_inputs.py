"""
Purpose: Provide user interaction options for the Iris dataset.

"""
from shiny import ui


def get_iris_inputs():
    return ui.panel_sidebar(
        ui.h2("Iris Interaction"),
        ui.tags.hr(),
        ui.input_slider(
            "IRIS_PETAL_LENGTH_RANGE",
            "Petal Length (cm)",
            min=10,
            max=35,
            value=[10, 35],
        ),
        
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )