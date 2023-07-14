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
         
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Iris Table"),
            ui.tags.p("Description of each field in the table:"),
            ui.tags.ul(
                ui.tags.li("sep_length: Length of Sepal"),
                ui.tags.li("sep_wid: Width of Sepal"),
                ui.tags.li("pet_len: Length of Petal"),
                ui.tags.li("pet_wid: Width of Petal"),
                ui.tags.li("spec: Species"),
        ),
            ui.output_table("irs_table"),
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )