from shiny import ui


def get_titanic_inputs():
    return ui.panel_sidebar(
        ui.h2("Titanic Interaction"),
        ui.tags.hr(),
        ui.input_numeric("TITANIC_MAX_AGE", "Max age:", value=55.0),
        ui.tags.hr(),
        ui.tags.section(
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )