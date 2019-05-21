from flask import Flask, Response
import os
import fnmatch
from os import listdir, path
from os.path import isfile, join
import random
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import csv
import matplotlib.pyplot as plt

import flask_silk
from flask_autoindex import AutoIndex

app = Flask(__name__)
# root_dir = os.path.curdir
root_dir = '/data'
AutoIndex(app, browse_root=root_dir)

@app.route('/plot/')
@app.route('/plot')
def plot():
    onlyfiles = [f for f in listdir(root_dir) if isfile(join(root_dir, f)) and fnmatch.fnmatch(f, '*.csv')]
    onlyfiles.sort()
    output = '<html><head><title>Heat Test Plotting</title></head><body>'
    output += '<table border=1><tr><th>File (click to download)</th><th>Actions</th></tr>'
    for file in onlyfiles:
        output += '<tr><td><a href="/{0}">{0}</a></td><td><a href="/plot/{0}">plot</a></td></tr>'.format(file)
    output += '</table><div>Full file listing at <a href="/">root</a>.</body></html>'
    return output, 200


@app.route('/plot/<filename>')
def plot_file(filename):
    fig = create_figure(filename)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png'), 200

def load_stuff(filename, offset):
    x = []
    y = []
    z = []

    with open(join(root_dir, filename),'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            try:
                if len(x) < 1:
                    start = int(row[0])
                    x.append(offset)
                else:
                    x.append(int(row[0])-start+offset)
                y.append(float(row[1]))
                z.append(int(row[2])/1e6)
            except ValueError:
                pass
            # if x[-1] > 3000:
            #     break

    return (x, y, z)

def create_figure(filename):
    fig = Figure(figsize=(8, 10))
    x, y, z = load_stuff(filename, 0)

    axis1 = fig.add_subplot(2, 1, 1)
    axis1.set_title(filename)
    axis1.plot(x, y)
    axis1.set_xlabel('Time (s)')
    axis1.set_ylabel('Temperature (C)')

    axis2 = fig.add_subplot(2, 1, 2)
    axis2.plot(x, z)
    axis2.set_xlabel('Time (s)')
    axis2.set_ylabel('Core Frequency (MHz)')
    return fig

if __name__ == '__main__':
    port = int(os.getenv('PORT', "80"))
    app.run(port=port, host='0.0.0.0')