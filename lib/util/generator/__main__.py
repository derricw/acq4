import os, sys, user
md = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(md, '..'))

import pyqtgraph as pg
import SequenceRunner
from PyQt4 import QtCore, QtGui
if not hasattr(QtCore, 'Signal'):
    QtCore.Signal = QtCore.pyqtSignal
from StimGenerator import *
app = QtGui.QApplication([])
sg = StimGenerator()
sg.show()

sg.setMeta('x', units='s', dec=True, minStep=1e-6, step=0.5, siPrefix=True)
sg.setMeta('y', units='W', dec=True, minStep=1e-3, step=0.5, siPrefix=True)
sg.setMeta('xy', units='J', dec=True, minStep=1e-9, step=0.5, siPrefix=True)

plot = pg.PlotWidget()
plot.show()

def plotData():
    rate = 1e3
    nPts = 100
    plot.clear()

    params = {}
    paramSpace = sg.listSequences()
    for k in paramSpace:
        params[k] = range(len(paramSpace[k]))

    global seqPlots
    seqPlots = []
    SequenceRunner.runSequence(lambda p: seqPlots.append(sg.getSingle(rate, nPts, p)), params, params.keys())
    
    for i, w in enumerate(seqPlots):
        if w is not None:
            plot.plot(w, pen=pg.intColor(i, len(seqPlots)*1.5))

    data = sg.getSingle(rate, nPts)
    plot.plot(data, pen=pg.mkPen('w', width=2))


sg.sigDataChanged.connect(plotData)


sg.loadState({
    'simpleMode': False,
    'function': 'pulse(30*ms, 15*ms, amp)',
    'params': {
        'amp':  {
            'default': '10*mV',
            'sequence': 'range',
            'start': '20*mV',
            'stop': '30*mV',
            'steps': 5
        }
    }
})
state1 = sg.saveState()

sg.loadState({
    'simpleMode': True,
    'stimuli': {
        'pulse 1': {
            'type': 'pulse',
            'start': {
                'value': 0.1,
                'sequence': 'off'},
            'length': {
                'value': 0.01,
                'sequence': 'off'},
            'amplitude': {
                'value': 0.1,
                'sequence': 'off'},
            }
        }
    }
)
                



if sys.flags.interactive == 0:
    app.exec_()