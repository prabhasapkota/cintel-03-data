"""
Purpose: Use Python to create a continuous intelligence and 



Each Shiny app has two parts: 
- a user interface app_ui object (similar to the HTML in a web page) 
- a server function that provides the logic for the app (similar to JS in a web page).

"""
import shinyswatch
from shiny import App, ui, render

from mtcars_server import get_mtcars_server_functions
from mtcars_ui_inputs import get_mtcars_inputs
from mtcars_ui_outputs import get_mtcars_outputs

from penguins_server import get_penguins_server_functions
from penguins_ui_inputs import get_penguins_inputs
from penguins_ui_outputs import get_penguins_outputs

from util_logger import setup_logger

logger, logname = setup_logger(__name__)

app_ui = ui.page_navbar(
    shinyswatch.theme.lumen(),
    ui.nav(
        "Home",
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.h2("Let's Start Here!"),
                ui.tags.hr(),
                ui.h3("Please, fill out the information"),
                ui.input_text("name_input", "Enter your name", placeholder="Your Name"),
                ui.input_text(
                    "location_input",
                    "Enter your location",
                    placeholder="Enter your location",
                ),
                ui.tags.hr(),
            ),
            ui.panel_main(
                ui.h2("New Data Exploration Tabs (see above)"),
                ui.tags.hr(),
                ui.tags.ul(
                    ui.tags.li(
                        "To explore the MotorTrend Car dataset, click the 'MT_Cars' tab."
                    ),
                    ui.tags.li(
                        "To explore the Penguins Dataset, click the 'Penguins' tab."
                    ),
                    ),
                ui.tags.hr(),
                ui.h2("Main Panel with Reactive Output"),
                ui.tags.hr(),
                ui.output_text_verbatim("welcome_output"),
                ui.output_text_verbatim("insights_output"),
                ui.tags.hr(),
            ),
        ),
    ),
    ui.nav(
        "MT_Cars",
        ui.layout_sidebar(
            get_mtcars_inputs(),
            get_mtcars_outputs(),
        ),
    ),
    ui.nav(
        "Penguins",
        ui.layout_sidebar(
            get_penguins_inputs(),
            get_penguins_outputs(),
        ),
    ),
    
    
    ui.nav(ui.a("About", href="https://github.com/prabhasapkota")),
    ui.nav(ui.a("GitHub", href="https://github.com/prabhasapkota/cintel-03-data")),
    ui.nav(ui.a("App", href="https://prabha23.shinyapps.io/cintel-03-data/")),
    ui.nav(ui.a("Examples", href="https://shinylive.io/py/examples/")),
    ui.nav(ui.a("Themes", href="https://bootswatch.com/")),
    title=ui.h1("PRABHA Dashboard"),
)


def server(input, output, session):
    """Define functions to create UI outputs."""

    @output
    @render.text
    def welcome_output():
        user = input.name_input()
        welcome_string = f"Welcome {user}!"
        return welcome_string

    @output
    @render.text
    def insights_output():
        answer = input.location_input()
        count = len(answer)
        language_string = f"You are from {answer}. That takes {count} characters"
        return language_string

    get_mtcars_server_functions(input, output, session)
    get_penguins_server_functions(input, output, session)
    
    

    
    
# app = App(app_ui, server, debug=True)
app = App(app_ui, server)
