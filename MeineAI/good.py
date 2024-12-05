from rich.console import Console
from rich.layout import Layout
from rich.progress import Progress, BarColumn
from rich.panel import Panel
from rich import print as rprint

# Initialize the console
console = Console()
# Example data
data = {
    "AVAILABLE": 70,
    "USED": 30,
}

# Define a layout
layout = Layout()

# Split the layout into sections
layout.split(
    Layout(name="header", size=3),
    Layout(name="body",size=4),
)

# Header content
layout["header"].update(Panel("[bold cyan]System Monitor"))
layout["body"].split_row(Layout(name='left'),Layout(name='right'))


# Footer content

# Progress bars renderable
def create_progress_bar():
    progress_renderable = Progress(
        "[progress.description]{task.description}",
        BarColumn(bar_width=30, complete_style="green"),
        "{task.percentage:>3.0f}%",
        console=console,
    )
    # Add tasks
    available = progress_renderable.add_task(
        "[bold magenta]AVAILABLE %", total=100, completed=data["AVAILABLE"]
    )
    used = progress_renderable.add_task(
        "[bold magenta]USED %", total=100, completed=data["USED"]
    )
    # Update progress
    progress_renderable.update(available, completed=data["AVAILABLE"])
    progress_renderable.update(used, completed=data["USED"])
    return Panel(progress_renderable,style='red on black',border_style='green',)

# Update body with progress bars
layout["body"]['left'].update(create_progress_bar())



# Display the layout
rprint(layout)
