import rerun as rr


rr.init("rerun_example_my_data", spawn=True)
x_values = [x * 2 - 10 for x in range(10)]  # Creates values from -10 to 10
positions = [[x, 0, 0] for x in x_values]
color_values = [int(i * 255 / 9) for i in range(10)]  # Creates values from 0 to 255
colors = [[c, 0, 0] for c in color_values]

rr.log(
    "my_points",
    rr.Points3D(positions, colors=colors, radii=0.5)
)
