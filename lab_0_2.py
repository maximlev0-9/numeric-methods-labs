from math import ceil
import matplotlib.pylab as plt

C1 = 32 * 10 ** -3
C2 = 50 * 10 ** -3
L_min = 3
L_max = 30
i_min = 1
i_max = 2
R1 = 7
R2 = 61
R3 = 23
R4 = 53
half_period = 0.007
period = 2 * half_period


def draw_graph(x_arguments, y_values, title="", x_label="", y_label=""):
    graph = plt.figure().gca()
    graph.plot(x_arguments, y_values)
    graph.set_title(title)
    graph.set_xlabel(x_label)
    graph.set_ylabel(y_label)
    plt.show()


def input_voltage(time_point):
    number_of_half_periods = ceil(time_point / half_period)

    if number_of_half_periods % 2:
        return 10 / half_period * (time_point - (number_of_half_periods - 1) * half_period)

    return 0


def output_voltage(value):
    return value[2] * R4


def inductance(current_value):
    if abs(current_value) <= i_min:
        return L_max

    if abs(current_value) >= i_max:
        return L_min

    return ((2 * current_value + i_max - 3 * i_min) * ((i_max - current_value) ** 2) * L_max
            + (3 * i_max - i_min - 2 * current_value) * ((current_value - i_min) ** 2) * L_min) / (i_max - i_min) ** 3


differential_equations = \
    [lambda time_point, value: ((value[2] + input_voltage(time_point) / R3 - value[0] * (1 / R1 + 1 / R3)) / C1),
     lambda time_point, value: (value[2] / C2),
     lambda time_point, value:
     ((input_voltage(time_point) - value[0] - value[1] - value[2] * (R2 + R4)) / inductance(value[2]))]


def get_next_value(time_point, value, step):
    """Runge-Kutta method"""
    next_value = value

    for i in range(len(value)):
        this_value = value[i]
        coefficient1 = step * differential_equations[i](time_point, value)
        value[i] = this_value + 0.5 * coefficient1
        coefficient2 = step * differential_equations[i](time_point + 0.5 * step, value)
        value[i] = this_value + 0.5 * coefficient2
        coefficient3 = step * differential_equations[i](time_point + 0.5 * step, value)
        value[i] = this_value + coefficient3
        coefficient4 = step * differential_equations[i](time_point + step, value)
        value[i] = this_value

        next_value[i] = value[i] + (coefficient1 + 3 * (coefficient2 + coefficient3) + coefficient4) / 8

    return next_value


def get_results(time_point, time_interval, value, step):
    time_value_pairs = dict()
    time_value_pairs[time_point] = [value[0], value[1], value[2], input_voltage(time_point), output_voltage(value)]

    while time_point < time_interval:
        value = get_next_value(time_point, value, step)
        time_point += step

        time_value_pairs[time_point] = [value[0], value[1], value[2], input_voltage(time_point), output_voltage(value)]

    return time_value_pairs


def main():
    time_point = 0
    # value[0] = U_C1, value[1] = U_C2, value[2] = i_L2
    value = [0, 0, 0]
    time_interval = 5 * period

    step = period / 400

    time_value_pairs = get_results(time_point, time_interval, value, step)

    time_points = []
    values_u_c1 = []
    values_u_c2 = []
    values_i_l2 = []
    values_u1 = []
    values_u2 = []
    values_of_inductance = []

    i_interval = []
    i = 0
    while i <= i_max + 1:
        i_interval.append(i)
        values_of_inductance.append(inductance(i))
        i += step

    for t, v in time_value_pairs.items():
        time_points.append(t)
        values_u_c1.append(v[0])
        values_u_c2.append(v[1])
        values_i_l2.append(v[2])
        values_u1.append(v[3])
        values_u2.append(v[4])

    draw_graph(i_interval, values_of_inductance, "L2", "i, amp", "L, henry")
    draw_graph(time_points, values_u1, "U1", "t, sec", "u, volt")
    draw_graph(time_points, values_u_c1, "U_C1", "t, sec", "u, volt")
    draw_graph(time_points, values_u_c2, "U_C2", "t, sec", "u, volt")
    draw_graph(time_points, values_i_l2, "i_L2", "t, sec", "i, amp")
    draw_graph(time_points, values_u2, "U2", "t, sec", "u, volt")


if __name__ == '__main__':
    main()