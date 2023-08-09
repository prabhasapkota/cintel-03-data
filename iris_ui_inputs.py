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
        ui.input_slider(
            "IRIS_PETAL_WIDTH_RANGE",
            "Petal Width (cm)",
            min=0,
            max=5,
            value=[0, 5],
        ),
        ui.input_slider(
            "IRIS_SEPAL_LENGTH_RANGE",
            "Sepal Length (cm)",
            min=0,
            max=8,
            value=[0, 8],
        ),
        ui.input_slider(
            "IRIS_SEPAL_WIDTH_RANGE",
            "Sepal Width (cm)",
            min=0,
            max=4,
            value=[0, 4],
        ),
        ui.input_checkbox("IRIS_SPECIES_Setosa", "Setosa", value=True),
        ui.input_checkbox("IRIS_SPECIES_Versicolor", "Versicolor", value=True),
        ui.input_checkbox("IRIS_SPECIES_Virginica", "Virginica", value=True),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )