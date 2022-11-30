# Creator: Ruowei Li
# Email: lir3@tcd.ie
import numpy as np
from tqdm import tqdm
from scipy.io import wavfile
from scipy.interpolate import CubicSpline


def my_cubic(input, detection):

    bar = tqdm(range(len(input)), 'my_cubic', ncols=100)  # show progress bar
    x = list(range(0, len(input)))
    y_before = []
    y_after = []
    y_combine = []
    x_combine = []
    x_before = []
    x_after = []

    i = 0
    output = input * 1.0
    input1 = input * 1.0
    detection = np.append(detection, 0)
    while i < len(input) - 1:
        for i in bar:

            if detection[i] > 0:  # detected some clicks here
                j = i
                t = i
                click_num = 0
                y_before = []
                y_after = []
                y_combine = []
                x_combine = []
                x_before = []
                x_after = []

                while detection[j] > 0:  # calculate the number of 1
                    click_num += 1
                    j += 1

                x_before = x[t - 1 - click_num: t]
                x_after = x[t + click_num: t + 2*click_num + 1]
                x_combine = np.concatenate((x_before, x_after), axis=None)
                # combine the x list
                y_before = input1[t - 1 - click_num: t]
                y_after = input1[t + click_num: t + 2*click_num + 1]
                y_combine = np.concatenate((y_before, y_after), axis=None)
                # combine the y list
                f = CubicSpline(x_combine, y_combine, bc_type='natural')
                x_new = np.linspace(
                    x[t + click_num], x[t + 2*click_num + 1], 2*click_num + 1)
                y_new = f(x_new)
                # get the interpolation list
                r = 0
                while r < 3:  # change the value of the clicks
                    output[t + r - 1] = y_new[r]
                    r = r + 1

                i = j + 1

            else:  # if there is no click

                i += 1
    return output
