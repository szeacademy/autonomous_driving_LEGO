# AutoDrive

A "learn by demonstration" example for LEGO lovers that want to try a machine-learning approach with their LEGO robot. Built with [Pybricks](https://pybricks.com).

## Video Tutorial

Watch the step-by-step tutorial on YouTube: [INSERT YOUTUBE LINK HERE]

## Overview

Instead of programming a path turn-by-turn, you **show the robot** the path once:

1. **Record** — Manually drive the robot along the desired path while `streaming_datalog.py` logs distance and gyro heading.
2. **Fit a curve** — Plot the logged data in a spreadsheet (Excel, Google Sheets, etc.) and fit a polynomial to `distance → heading angle`. Note the equation and its R² value.
3. **Drive** — Paste the equation, distance, and R² into `autonomous_driving.py`. The robot reproduces the path on its own using a proportional gyro controller.

This is a hands-on introduction to regression, fitting a mathematical model to real sensor data, that works with a Mindstorm or Spike LEGO kit.

## Files

| File | Purpose |
|------|---------|
| `streaming_datalog.py` | Records `(distance, gyro_angle)` samples while you manually guide the robot. Streams `plot:distance,gyro_angle` lines to the Pybricks IDE datalog. |
| `autonomous_driving.py` | Drives a learned path from a fitted polynomial equation, R², and total distance. Edit the `equation`, `distance`, and `R2` placeholders. |
| `test1.csv` | Sample captured run (`timestamp, distance, gyro_angle`) to use as a reference. |

## Requirements

- A Pybricks-enabled LEGO hub with two motors (e.g., SPIKE Prime).  Note: Can also be done with regular HUB software with adjustments.
- Motor ports, wheel size, and other robot-specific settings are configurable at the top of each script.

## Notes

- The `R²` value scales the target angle to improve accuracy; a lower R² means a less reliable fit.
- The `direction` argument in `ad_navigation()` lets the robot travel forward (1) or backward (-1).
- Robot speed is reduced at the start and end of the path for a smooth stop.

## License

MIT
