import dash
import dash_html_components as html

# Make dash instance 
app = dash.Dash(__name__)

app.layout = html.H1("Hello, World!")

if __name__=="__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8000)