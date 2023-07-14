from shiny import ui


def get_iris_inputs():
    return ui.panel_sidebar(
        ui.h2("Iris Interaction"),
        ui.tags.hr(),
        ui.input_slider(
            "IRIS_PETAL_LENGTH_RANGE",
            "Petal Length (cm)",
            min=0,
            max=10,
            value=[0, 10],
       ),
        ui.input_checkbox("IRIS_SPECIES_Setosa", "Setosa", value=True),
        ui.input_checkbox("IRIS_SPECIES_Versicolor", "Versicolor", value=True),
        ui.input_checkbox("IRIS_SPECIES_Virginica", "Virginica", value=True),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )