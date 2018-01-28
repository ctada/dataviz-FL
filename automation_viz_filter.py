
import pandas as pd
from bokeh.models import HoverTool, Select, ColumnDataSource
from bokeh.plotting import figure, output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html, components
from bokeh.layouts import row, widgetbox
from bokeh.plotting import curdoc, figure


output_file("filtered_viz.html")

df = pd.read_csv("raw_state_automation_data.csv", sep = ",")
    #names = ["SOC","Occupation","Probability","Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","District of Columbia","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]) 
#df.loc[df[['Company_A', 'Company_B', 'Company_C']].idxmax().unique()] #to get max, query: https://stackoverflow.com/questions/24510898/query-a-csv-using-pandas


# data cleanup
columns = sorted(df.columns)

def create_figure():
    # xs = df["Probability"].values
    # ys = df[y.value].values
    y_title = y.value.title()

    select = {'Probability': df["Probability"],
        'Job Quantity': df[y.value],
        'Occupation':df["Occupation"]}

    source = ColumnDataSource(data=select)

    # kw = dict()
    # kw['y_range'] = sorted(set(ys))
    # kw['title'] = "Risk of Automation in %s" % (y_title)

    plot = figure(title = "Risk of Automation in %s" % (y_title), tools="crosshair,pan,save,wheel_zoom")
    plot.circle(x='Probability', y='Job Quantity', source=source)
    plot.xaxis[0].axis_label = 'Probability of Automation'
    plot.yaxis[0].axis_label = '# of Jobs'
    plot.add_tools(HoverTool( tooltips=[("Occupation", "@Occupation")] ))

    return plot

def update(attr, old, new):
    layout.children[1] = create_figure()


y = Select(title="State", value="Alabama", options=columns)
y.on_change("value", update)

controls = widgetbox([y], width=200)
layout = row(controls, create_figure())

curdoc().add_root(layout)
curdoc().title = "Automation Risk"

