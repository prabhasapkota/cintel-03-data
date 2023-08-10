""" 
Purpose: Provide reactive output for the Titanic dataset.

- Use inputs from the UI Sidebar to filter the dataset.
- Update reactive outputs in the UI Main Panel.


"""
import pathlib
from shiny import render, reactive
import matplotlib.pyplot as plt
import pandas as pd
from plotnine import aes, geom_point, ggplot, ggtitle
from shinywidgets import render_widget
import plotly.express as px

from util_logger import setup_logger

logger, logname = setup_logger(__name__)

def get_titanic_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    p = pathlib.Path(__file__).parent.joinpath("data").joinpath("titanic.csv")
    # logger.info(f"Reading data from {p}")
    original_df = pd.read_csv(p)
    total_count = len(original_df)

    reactive_df = reactive.Value()

    @reactive.Effect
    @reactive.event(input.TITANIC_MAX_AGE)


    def _():

        df = original_df.copy()

        age_filter = df["age"] < input.TITANIC_MAX_AGE()
        df = df[age_filter]

        # logger.debug(f"filtered penguins df: {df}")
        reactive_df.set(df)

    @output
    @render.text
    def titanic_record_count_string():
        # logger.debug("Triggered: titanic_filter_record_count_string")
        filtered_count = len(reactive_df.get())
        message = f"Showing {filtered_count} of {total_count} records"
        # logger.debug(f"filter message: {message}")
        return message
    
    @output
    @render.table
    def titanic_filtered_table():
        filtered_df = reactive_df.get()
        return filtered_df
    
    @output
    @render_widget
    def titanic_output_widget1():
        df = reactive_df.get()
        plotly_express_plot = px.scatter(df, x="age", y="pclass", color="survived", size="fare")
        plotly_express_plot.update_layout(title="Titanic with Plotly Express")
        return plotly_express_plot
    
    # return a list of function names for use in reactive outputs
    return [
        titanic_record_count_string,
        titanic_filtered_table,
        titanic_output_widget1,
    ]