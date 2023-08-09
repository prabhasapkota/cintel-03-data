""" 
Purpose: Provide reactive output for the Penguins dataset.

- Use inputs from the UI Sidebar to filter the dataset.
- Update reactive outputs in the UI Main Panel.

Matching the IDs in the UI Sidebar and function/output names in the UI Main Panel
to this server code is critical. They are case sensitive and must match exactly.

"""
import pathlib
from shiny import render, reactive
import pandas as pd
import seaborn as sns
from shinywidgets import render_widget
import plotly.express as px


from util_logger import setup_logger

logger, logname = setup_logger(__name__)


def get_penguins_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    path_to_data = (
        pathlib.Path(__file__).parent.joinpath("data").joinpath("penguins.xlsx")
    )
    original_df = pd.read_excel(path_to_data)
    total_count = len(original_df)

    # Create a reactive value to hold the filtered pandas dataframe
    reactive_df = reactive.Value()

    # Create a reactive effect to set the reactive value when inputs change
    # List all the inputs that should trigger this update

    @reactive.Effect
    @reactive.event(
        input.PENGUIN_BODY_MASS_RANGE,
        input.PENGUIN_MAX_BILL,
    )

    def _():
        """Reactive effect to update the filtered dataframe when inputs change.
        This is the only way to set a reactive value (after initialization).
        It doesn't need a name, because no one calls it directly."""

        # logger.info("UI inputs changed. Updating penguins reactive df")

        df = original_df.copy()
        
        # Body mass is a range
        input_range = input.PENGUIN_BODY_MASS_RANGE()
        input_min = input_range[0]
        input_max = input_range[1]
        body_mass_filter = (df["body_mass_g"] >= input_min) & (
            df["body_mass_g"] <= input_max
        )
        df = df[body_mass_filter]

        # Bill length is a max number
        bill_length_filter = df["bill_length_mm"] <= input.PENGUIN_MAX_BILL()
        df = df[bill_length_filter]

        
        # logger.debug(f"filtered penguins df: {df}")
        reactive_df.set(df)

    @output
    @render.table
    def penguins_filtered_table():
        filtered_df = reactive_df.get()
        return filtered_df
    
    @output
    @render.text
    def penguins_record_count_string():
        # logger.debug("Triggered: penguins_filter_record_count_string")
        filtered_count = len(reactive_df.get())
        message = f"Showing {filtered_count} of {total_count} records"
        # logger.debug(f"filter message: {message}")
        return message
    @output
    @render_widget
    def penguins_output_widget1():
        df = reactive_df.get()
        plotly_plot = px.scatter(
            df,
            x="bill_length_mm",
            y="body_mass_g",
            color="species",
            title="Penguins Plot (Plotly Express))",
            labels={
                "bill_length_mm": "Bill Length (mm)",
                "body_mass_g": "Body Mass (g)",
            },
            size_max=8,
        )
        return plotly_plot
    
    # return a list of function names for use in reactive outputs
    return [
        penguins_record_count_string,
        penguins_filtered_table,
        penguins_output_widget1,
    ]


   

    # return a list of function names for use in reactive outputs
    return [
        penguins_filtered_table,
        penguins_record_count_string,
    ]
