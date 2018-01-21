
import pandas as pd
from bokeh.models import HoverTool
from bokeh.plotting import figure, output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html, components
from bokeh.models import ColumnDataSource

# output_file("viz.html")

data = pd.read_csv("raw_state_automation_data.csv", sep = ",")
	#names = ["SOC","Occupation","Probability","Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","District of Columbia","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]) 
select = {'Probability': data["Probability"],
        'Job Quantity': data["Alabama"],
        'Occupation':data["Occupation"]}

source = ColumnDataSource(data=select)

plot = figure(title="Risk of Automation in Alabama",tools="crosshair,pan,save,wheel_zoom")
plot.circle(x='Probability', y='Job Quantity', source = source)
plot.xaxis[0].axis_label = 'Probability of Automation'
plot.yaxis[0].axis_label = '# of Jobs'
plot.add_tools(HoverTool( tooltips=[("Occupation", "@Occupation")] ))

html = file_html(plot, CDN, "my plot")
# script, div = components(plot)
show(plot)
