#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: multiplexaPAM
# Author: Daniela_Brayan
# Copyright: Daniela_Brayan
# GNU Radio version: 3.10.5.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from ModulacionPAM import ModulacionPAM  # grc-generated hier_block
from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class multiplexaPAM(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "multiplexaPAM", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("multiplexaPAM")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "multiplexaPAM")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100000
        self.fs = fs = 1000
        self.fm = fm = 100
        self.d3 = d3 = 0
        self.d2 = d2 = 0
        self.d1 = d1 = 0
        self.d = d = 10
        self.am = am = 1

        ##################################################
        # Blocks
        ##################################################

        self._fs_range = Range(0, 10000, 1, 1000, 200)
        self._fs_win = RangeWidget(self._fs_range, self.set_fs, "frecuencia pulsos", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fs_win)
        self._fm_range = Range(0, 1000, 10, 100, 200)
        self._fm_win = RangeWidget(self._fm_range, self.set_fm, "frecuencia mensaje", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fm_win)
        self._d3_range = Range(0, 100, 1, 0, 200)
        self._d3_win = RangeWidget(self._d3_range, self.set_d3, "retardo 3", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._d3_win)
        self._d2_range = Range(0, 100, 1, 0, 200)
        self._d2_win = RangeWidget(self._d2_range, self.set_d2, "retardo 2", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._d2_win)
        self._d1_range = Range(0, 100, 1, 0, 200)
        self._d1_win = RangeWidget(self._d1_range, self.set_d1, "retardo 1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._d1_win)
        self._d_range = Range(0, 50, 1, 10, 200)
        self._d_win = RangeWidget(self._d_range, self.set_d, "ancho pulso", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._d_win)
        self._am_range = Range(0, 10, 100e-3, 1, 200)
        self._am_win = RangeWidget(self._am_range, self.set_am, "amplitud mensaje", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._am_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            (1024*4), #size
            samp_rate, #samp_rate
            "", #name
            5, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(5):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.blocks_delay_2 = blocks.delay(gr.sizeof_float*1, d3)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_float*1, d2)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, d1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_3 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, fm, am, 0, 0)
        self.analog_sig_source_x_2 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, fm, am, 0, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_TRI_WAVE, fm, am, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fm, am, 0, 0)
        self.ModulacionPAM_0_1_0 = ModulacionPAM(
            D=d,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModulacionPAM_0_1 = ModulacionPAM(
            D=d,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModulacionPAM_0_0 = ModulacionPAM(
            D=d,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModulacionPAM_0 = ModulacionPAM(
            D=d,
            fs=fs,
            samp_rate=samp_rate,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.ModulacionPAM_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.ModulacionPAM_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.ModulacionPAM_0_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.ModulacionPAM_0_1, 0), (self.blocks_delay_1, 0))
        self.connect((self.ModulacionPAM_0_1_0, 0), (self.blocks_delay_2, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.ModulacionPAM_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.ModulacionPAM_0_0, 0))
        self.connect((self.analog_sig_source_x_2, 0), (self.ModulacionPAM_0_1, 0))
        self.connect((self.analog_sig_source_x_3, 0), (self.ModulacionPAM_0_1_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0, 4))
        self.connect((self.blocks_delay_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_delay_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_delay_1, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_delay_2, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_delay_2, 0), (self.qtgui_time_sink_x_0, 3))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "multiplexaPAM")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.ModulacionPAM_0.set_samp_rate(self.samp_rate)
        self.ModulacionPAM_0_0.set_samp_rate(self.samp_rate)
        self.ModulacionPAM_0_1.set_samp_rate(self.samp_rate)
        self.ModulacionPAM_0_1_0.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_3.set_sampling_freq(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_fs(self):
        return self.fs

    def set_fs(self, fs):
        self.fs = fs
        self.ModulacionPAM_0.set_fs(self.fs)
        self.ModulacionPAM_0_0.set_fs(self.fs)
        self.ModulacionPAM_0_1.set_fs(self.fs)
        self.ModulacionPAM_0_1_0.set_fs(self.fs)

    def get_fm(self):
        return self.fm

    def set_fm(self, fm):
        self.fm = fm
        self.analog_sig_source_x_0.set_frequency(self.fm)
        self.analog_sig_source_x_1.set_frequency(self.fm)
        self.analog_sig_source_x_2.set_frequency(self.fm)
        self.analog_sig_source_x_3.set_frequency(self.fm)

    def get_d3(self):
        return self.d3

    def set_d3(self, d3):
        self.d3 = d3
        self.blocks_delay_2.set_dly(int(self.d3))

    def get_d2(self):
        return self.d2

    def set_d2(self, d2):
        self.d2 = d2
        self.blocks_delay_1.set_dly(int(self.d2))

    def get_d1(self):
        return self.d1

    def set_d1(self, d1):
        self.d1 = d1
        self.blocks_delay_0.set_dly(int(self.d1))

    def get_d(self):
        return self.d

    def set_d(self, d):
        self.d = d
        self.ModulacionPAM_0.set_D(self.d)
        self.ModulacionPAM_0_0.set_D(self.d)
        self.ModulacionPAM_0_1.set_D(self.d)
        self.ModulacionPAM_0_1_0.set_D(self.d)

    def get_am(self):
        return self.am

    def set_am(self, am):
        self.am = am
        self.analog_sig_source_x_0.set_amplitude(self.am)
        self.analog_sig_source_x_1.set_amplitude(self.am)
        self.analog_sig_source_x_2.set_amplitude(self.am)
        self.analog_sig_source_x_3.set_amplitude(self.am)




def main(top_block_cls=multiplexaPAM, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
