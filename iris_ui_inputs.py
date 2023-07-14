"""
Purpose: Provide user interaction options for the Iris dataset.

"""
from shiny import ui


def get_iris_inputs():
    return ui.panel_sidebar(
        ui.h2("Iris Interaction"),
        ui.tags.hr(),
        ui.input_slider(
            "IRIS_Sepal_LENGTH_RANGE",
            "Sepal Length (cm)",
            min=2,
            max=8,
            value=[2, 8],
        ),
        
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )