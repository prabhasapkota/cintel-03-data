from shiny import ui


def get_titanic_inputs():
    return ui.panel_sidebar(
        ui.h2("Titanic Interaction"),
        ui.tags.hr(),
        ui.input_radio_buttons(
            "Titanic_Sex",
            "Select Sex",
            {"f": "Female", "m": "Male"},
            selected="f",
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )