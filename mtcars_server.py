""" 
Purpose: Provide reactive output for MT Cars dataset.

"""
import pathlib
from shiny import render, reactive
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from plotnine import aes, geom_point, ggplot, ggtitle
from shinywidgets import render_widget
import plotly.express as px



from util_logger import setup_logger

logger, logname = setup_logger(__name__)


def get_mtcars_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    path_to_data = pathlib.Path(__file__).parent.joinpath("data").joinpath("mtcars.csv")
    original_df = pd.read_csv(path_to_data)

    # Use the len() function to get the number of rows in the DataFrame.
    total_count = len(original_df)

    reactive_df = reactive.Value()

    @reactive.Effect
    @reactive.event(
        input.MTCARS_MPG_RANGE,
        input.MTCARS_MAX_HP,
    )
    def _():
        df = original_df.copy()

        input_range = input.MTCARS_MPG_RANGE()
        input_min = input_range[0]
        input_max = input_range[1]
        
        """
        Filter the dataframe to just those greater than or equal to the min
        and less than or equal to the max
        """

        mtcars_mpg_filter = (df["mpg"] >= input_min) & (df["mpg"] <= input_max)
        df = df[mtcars_mpg_filter]

        horse_power_filter = df["hp"] < input.MTCARS_MAX_HP()
        df = df[horse_power_filter]


        # Set the reactive value
        reactive_df.set(df)


    @output
    @render.table
    def mtcars_filtered_table():
        filtered_df = reactive_df.get()
        return filtered_df
    
    @output
    @render.text
    def mtcars_record_count_string():
        filtered_df = reactive_df.get()
        filtered_count = len(filtered_df)
        message = f"Showing {filtered_count} of {total_count} records"
        # logger.debug(f"filter message: {message}")
        return message
    
    @output
    @render.plot
    def mtcars_plot1():
        df = reactive_df.get()
        matplotlib_fig, ax = plt.subplots()
        plt.title("MT Cars with matplotlib")
        ax.scatter(df["wt"], df["mpg"])
        return matplotlib_fig

    @output
    @render.plot
    def mtcars_plot2():
        df = reactive_df.get()
        plotnine_plot = (
            ggplot(df, aes("wt", "mpg"))
            + geom_point()
            + ggtitle("MT Cars with plotnine")
        )

        return plotnine_plot


    # return a list of function names for use in reactive outputs
    return [
        mtcars_record_count_string,
        mtcars_filtered_table,
        mtcars_plot1,
        mtcars_plot2,
    ]
 
