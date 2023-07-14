from shiny import ui


def get_iris_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Iris: Seaborn Scatter Plot"),
            ui.output_plot("iris_scatterplot"),
            ui.tags.hr(),
            ui.h3("Iris Table"),
            ui.output_text("iris_record_count_string"),
            ui.output_table("iris_table"),
            ui.tags.hr(),
        ),
    )