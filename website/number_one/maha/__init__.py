import os
import pandas as pd

from flask import Flask, g, render_template, Markup, request, url_for
from flask_table import Table, Col

app = Flask(__name__)

# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'

# an About page
@app.route('/about')
def about():
    # call some text from a file which contains information like
    # EPFL, ADA, Data-Saviours, objective of the webpage, ...
    return render_template("about.html")

# a help page that shows how to use the website
@app.route('/help')
def helppage():
    # call some text, maybe images or videos from files to explain 
    # how to use the website
    return render_template("helppage.html")

# the main page
@app.route('/main') # maybe just '/' or '/index'
def main():
    # from this page you should reach all other pages and this page
    # should be reachable from all other pages.
    # it does redirection
    asdf = 8
    test = 5
    test_2 = 7 + test
    return render_template("index.html", test=asdf, test_2=test_2)

all_db_filenames = {"tennis": "atp_matches_2018.csv"}
def read_in_df(db_name):
    """
    reads one  csv file and converts to pandas df
    db_name: string (field of dict "all_db_filenames") 
    df: pandas df
    """
    df = pd.read_csv(all_db_filenames[db_name])
    return df

def edit_df(df):
    """
    takes a pandas df and returns a pandas df
    if input is not a pandas df, return None
    template function for other editing functions
    """
    if str(type(df)) == "<class 'pandas.core.frame.DataFrame'>":
        out_df = df
    else:
        out_df = None
    return out_df

def df_to_html(df):
    """
    takes a pandas df and convert it to html 
    """
    html = df.to_html()
    return html


"""
"""
class SortableTable(Table):
    winner_name = Col('winner_name')
    winner_hand = Col('winner_hand')
    winner_ht = Col('winner_ht')
    allow_sort = True

    def sort_url(self, col_key, reverse=False): # col_key is id, name or description / reverse=true-> direction="desc" and vice versa
                                                # creates the url for e.g. /projects/name/desc
        if reverse:
            direction = 'desc'
        else:
            direction = 'asc'
        return url_for('project', sort=col_key, direction=direction) # 'index' to be replaced by desired url

class Item(object):
    """ a little fake database """ # defines the columns of the Item/table/dataframe
    def __init__(self, winner_name, winner_hand, winner_ht):
        self.winner_name = winner_name
        self.winner_hand = winner_hand
        self.winner_ht = winner_ht

    @classmethod
    def get_elements(cls):
        df = read_in_df("tennis")
        out = df.iloc[520:540,10:13].to_dict('records')
        return out # returns a dict of the dataframe

    @classmethod
    def get_sorted_by(cls, sort, reverse=False): # sorts something
        return sorted(
            cls.get_elements(),
            key=lambda x: x[str(sort)], #getattr(x, sort),
            reverse=reverse)
"""
"""
@app.route('/project')
def project():
    # in this page there should be the desired view of the databases,
    # the search bar and the graph depicting...
    
    # define table entries via get_elements
    
    sort = request.args.get('sort', 'winner_name')  # returns the sort and id values after the ? in the url, e.g. ?sort=id&direction=asc 
    reverse = (request.args.get('direction', 'asc') == 'desc') # true if the current direction is 'desc' ???
    table = SortableTable(Item.get_sorted_by(sort, reverse),
                          sort_by=sort,
                          sort_reverse=reverse)
    return render_template("project.html",db_dummy=table)

