# This file is part of QuTiP.
#
#    QuTiP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    QuTiP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with QuTiP.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2011 and later, Paul D. Nation & Robert J. Johansson
#
###########################################################################

import time
import datetime

class BaseProgressBar(object):
    """
    An abstract progress bar with some shared functionality.

    Example usage:

        n_vec = linspace(0, 10, 100)
        pbar = TextProgressBar(len(n_vec))
        for n in n_vec:
            pbar.update(n)
            compute_with_n(n)
        pbar.finished()

    """

    def __init__(self, iterations=0, chunk_size=10):
        pass

    def start(self, iterations, chunk_size=10):
        self.N = float(iterations)
        self.p_chunk_size = chunk_size
        self.p_chunk = 0
        self.t_start = time.time()

    def update(self, n):
        pass

    def time_elapsed(self):
        return "%6.2fs" % (time.time() - self.t_start)

    def time_remaining_est(self, p):
        if p > 0.0:
            t_r_est = (time.time() - self.t_start) * (100.0 - p) / p
        else:
            t_r_est = 0

        dd = datetime.datetime(1, 1, 1) + datetime.timedelta(seconds=t_r_est)
        time_string = "%02d:%02d:%02d:%02d" % \
            (dd.day - 1, dd.hour, dd.minute, dd.second)

        return time_string
        #return "%6.2fs" % (t_r_est)


    def finished(self):
       pass


class TextProgressBar(BaseProgressBar):
    """
    A simple text-based progress bar.
    """

    def __init__(self, iterations=0, chunk_size=10):
        super(TextProgressBar, self).start(iterations, chunk_size)

    def start(self, iterations, chunk_size=10):
        super(TextProgressBar, self).start(iterations, chunk_size)

    def update(self, n):
        p = (n / self.N) * 100.0
        if p >= self.p_chunk:
            print("Completed: %4.1f%%." % p +
                  " Elapsed time: %s." % self.time_elapsed() +
                  " Est. remaining time: %s." % self.time_remaining_est(p))
            self.p_chunk += self.p_chunk_size

    def finished(self):
       self.t_done = time.time()
       print("Elapsed time: %s" % self.time_elapsed())
