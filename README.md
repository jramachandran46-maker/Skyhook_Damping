Skyhook_Damping

A physical model of the quarter car problem using CAD-designed parts. Uses ESP32 microcontroller and ToF sensor to control a servo motor that acts as an actuator in an active suspension system. The goal was to decrease the RMS of the body plate movement, as this would represent an increase in ride comfort.

How the control model works

Position data from the ToF sensor is differentiated to get relative velocity of the body. From there, the desired actuator force is computed by u = −cv, where c is the damping gain and v is relative body velocity. The servo applies this force through a spring (stiffness k) attached to its arm (length l): producing force u requires stretching the spring by u/k, so the servo rotates to θ = arcsin(u / (l·k)). This assumes the spring's stretch equals the arm tip's horizontal deflection, which would be true if the body plate was stationary. This is a rough approximation good enough for this elementary model.

Procedure

Data for the relative position of the body plate was collected in two 80 second trials, first with the active system engaged and then with it off. The road was simulated by gently raising and lowering the bottom plate by hand exactly 3 cm off the ground and back down again with a frequency of once per every two seconds. The hand movement was thus roughly controlled over the two trials.

Results

Python was used to analyze the resulting csvs, and the results are as follows:

RMS with active suspension: 3.75 mm

RMS without active suspension: 5.10 mm

Overall, the suspension system was able to successfully decrease the RMS value by 26.6 percent.
