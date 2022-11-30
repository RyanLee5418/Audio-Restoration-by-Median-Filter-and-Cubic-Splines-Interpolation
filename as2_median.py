# Creator: Ruowei Li
# Email: lir3@tcd.ie
import numpy as np
import unittest
from my_median import my_median
from my_cubic import my_cubic
from scipy.io import wavfile
from scipy.interpolate import CubicSpline
from matplotlib import pyplot as plt
from playsound import playsound


t, degraded = wavfile.read("degraded.wav")
t, detection = wavfile.read("detectionfile.wav")
t, clean = wavfile.read("clean.wav")

degraded = degraded/32767
clean = clean/32767

plt.figure(1)
plt.ylim(-0.06, 0.06)
plt.title('Degraded_Audio')
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.plot(degraded[0:])
plt.ylabel("Amplitude")
plt.xlabel("Time")


outputfile_median = my_median(degraded, detection)
outputfile_cubic = my_cubic(degraded, detection)

wavfile.write('outputfile_median.wav', t, outputfile_median)
wavfile.write('outputfile_cubic.wav', t, outputfile_cubic)

print("Done")
print("The MSE of median is :", np.square(clean - outputfile_median).mean())
print("The MSE of cubic is :", np.square(clean - outputfile_cubic).mean())

plt.figure(2)
plt.ylim(-0.06, 0.06)
plt.title('Median_Result')
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.plot(outputfile_median[0:])
plt.ylabel("Amplitude")
plt.xlabel("Time")

plt.figure(3)
plt.ylim(-0.06, 0.06)
plt.title('Clean_Audio')
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.plot(clean[0:])
plt.ylabel("Amplitude")
plt.xlabel("Time")

plt.figure(4)
plt.ylim(-0.06, 0.06)
plt.title('Cubic_Result')
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.plot(outputfile_cubic[0:])
plt.ylabel("Amplitude")
plt.xlabel("Time")

plt.show()

playsound('outputfile_median.wav')
playsound('outputfile_cubic.wav')


class TestMyWork(unittest.TestCase):
    def test_length(self):
        L_median = len(outputfile_median)
        L_clean = len(clean)
        self.assertEqual(L_median, L_clean)


if __name__ == '_main_':
    unittest.main()
