# Creator: Ruowei Li
# Email: lir3@tcd.ie
import numpy as np
from tqdm import tqdm


def my_median(input, detection):

    bar = tqdm(range(len(input)), 'my_median', ncols=100)  # show progress bar

    i = 0
    output = input * 1.0
    input1 = input * 1.0
    detection = np.append(detection, 0)
    while i < len(input) - 1:
        for i in bar:

            if detection[i] > 0:  # detected some clicks here
                j = i
                click_num = 0

                while detection[j] > 0:  # calculate the number of 1
                    click_num += 1
                    j += 1
                m = i
                k = 0
                md_wd = np.zeros(2*click_num + 1)
                while k < click_num:
                    # If the meidan window length exceeds the input list, fill each list with enough zeros
                    if m + click_num >= len(input):
                        p = 0
                        while p < m + click_num + 1 - len(input):

                            input1 = np.append(input1, 0)
                            detection = np.append(detection, 0)
                            p += 1

                    md_wd = input1[m - click_num: m +
                                   click_num + 1]  # median filter
                    md_wd.sort()
                    med = md_wd[click_num]
                    output[m] = med
                    md_wd = np.zeros(2*click_num + 1)
                    k += 1
                    m += 1

                i = m
            else:

                i += 1
    return output
