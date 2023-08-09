"""_summary_
We are creating a new tab for our shiny app to display the iris dataset loaded earlier.
The CSV file is loaded into a pandas DataFrame and the number of rows is counted.
The server functions are defined in the get_iris_server_functions() function.

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


def get_iris_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    path_to_data = pathlib.Path(__file__).parent.joinpath("data").joinpath("iris.csv")
    original_df = pd.read_csv(path_to_data)

    # Use the len() function to get the number of rows in the DataFrame.
    total_count = len(original_df)

    reactive_df = reactive.Value()

    @reactive.Effect
    @reactive.event(input.IRIS_SEPAL_LENGTH_RANGE,)

    def _():
        df = original_df.copy()

        input_range = input.MTCARS_MPG_RANGE()
        input_min = input_range[0]
        input_max = input_range[1]
        
        iris_sepal_length_filter = (df["sepal_length"] >= input_min) & (df["sepal_length"] <= input_max)
        df = df[iris_sepal_length_filter]

         # Set the reactive value
        reactive_df.set(df)

    @output
    @render.table
    def iris_filtered_table():
        filtered_df = reactive_df.get()
        return filtered_df


    @output
    @render.text
    def iris_record_count_string():
        filtered_df = reactive_df.get()
        filtered_count = len(filtered_df)
        message = f"Showing {filtered_count} of {total_count} records"
        #logger.debug(f"filter message: {message}")
        return message
    
    @output
    @render_widget
    def iris_output_widget1():
        df = reactive_df.get()
        plotly_express_plot = px.scatter(df, x="sepal_length", y="sepal_width", color="petal_length", size="petal_width")
        plotly_express_plot.update_layout(title="Iris with Plotly Express")
        return plotly_express_plot

    @output
    @render.plot
    def iris_plot1():
        df = reactive_df.get()
        matplotlib_fig, ax = plt.subplots()
        plt.title("Iris Cars with matplotlib")
        ax.scatter(df["sepal_length"], df["sepal_width"])
        return matplotlib_fig

    @output
    @render.plot
    def iris_plot2():
        df = reactive_df.get()
        plotnine_plot = (
            ggplot(df, aes("sepal_length", "sepal_width"))
            + geom_point()
            + ggtitle("Iris with plotnine")
        )

        return plotnine_plot


    

    # Return a list of function names for use in reactive outputs
    functions = [
        iris_filtered_table,
        iris_record_count_string,
        iris_output_widget1,
        iris_plot1,
        iris_plot2,
    ]