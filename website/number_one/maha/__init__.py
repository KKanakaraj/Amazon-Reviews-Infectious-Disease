import os
import pandas as pd

from flask import Flask, g, render_template, Markup, request, url_for, redirect
from flask_table import Table, Col

app = Flask(__name__)

#%% FUNCTIONS
def get_autocomplete_list(db_name):
    df = read_in_df(db_name)
    df = list(df.winner_name.unique())
    df = [x.lower() for x in df]
    return df
    
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

def get_df_to_query(name):
    out_df = pd.read_csv(all_db_filenames[name])
    return out_df

def dataframe_to_show():
    in_df = get_df_to_query("tennis")
    search_query = unique_search_query
    if search_query is not None:
        search_query = search_query.lower()
        out_df = in_df[in_df.winner_name.transform(lambda x: x.lower())==search_query].iloc[:30,10:13].to_dict('records')
    else:
        out_df = pd.DataFrame().to_dict('records')
    return out_df

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
        out = dataframe_to_show()
        return out # returns a dict of the dataframe

    @classmethod
    def get_sorted_by(cls, sort, reverse=False): # sorts something
        return sorted(
            cls.get_elements(),
            key=lambda x: x[str(sort)], #getattr(x, sort),
            reverse=reverse)
"""
"""


#%% WEB-PAGES

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
@app.route('/main', methods=['GET','POST']) # maybe just '/' or '/index'
def main():
    # from this page you should reach all other pages and this page
    # should be reachable from all other pages.
    # it does redirection
    if request.method == 'POST':
        text = request.form['text']
    
    asdf = 8
    test = 5
    test_2 = asdf + test
    return render_template("index.html", test=asdf, test_2=test_2)

@app.route('/project', methods=['GET','POST'])
def project():
    # in this page there should be the desired view of the databases,
    # the search bar and the graph depicting...
    
    # define table entries via get_elements
    global unique_search_query 
    unique_search_query = None
    
    if request.method == 'POST':
        unique_search_query = request.form['text']
    
    
    sort = request.args.get('sort', 'winner_name')  # returns the sort and id values after the ? in the url, e.g. ?sort=id&direction=asc 
    reverse = (request.args.get('direction', 'asc') == 'desc') # true if the current direction is 'desc' ???
    table = SortableTable(Item.get_sorted_by(sort, reverse),
                          sort_by=sort,
                          sort_reverse=reverse)
    return render_template("project.html",db_dummy=table)

