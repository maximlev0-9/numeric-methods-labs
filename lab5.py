from math import sin, pi
import matplotlib.pylab as plt


U_max = 100
frequency = 50
R1 = 5
R2 = 4
R3 = 7
R4 = 2
L = 0.01
C1 = 300 * 10 ** -6
C2 = 150 * 10 ** -6
size_of_step = 0.00001

time_to_finish = 0.2
curr_time = 0

input_system = [
    lambda cur_time, dynamic_i3_ul: ((R2 * ((U_max * sin(2 * pi * frequency * cur_time)) - dynamic_i3_ul[0] * R2) / R3 + R1) - dynamic_i3_ul[0] * R4 / L),
    lambda cur_time, value: ((U_max * sin(2 * pi * frequency * cur_time) + value[0] * R2) / (R1 + R2))]


def calculate_dynamic_values(time_now, time_next_iteration, dynamic_value, h):
    next_value = dynamic_value

    for i in range(len(dynamic_value)):
        next_value[i] = dynamic_value[i] + h * input_system[i](time_now, dynamic_value)

    for i in range(len(dynamic_value)):
        next_value[i] = dynamic_value[i] + (h/2) * (input_system[i](time_now, dynamic_value) + input_system[i](time_next_iteration, next_value) )
    
    return next_value


def calculate_output(time_now, time_final, dynamic_i3_ul, step):
    iterational_result = dict()
    while time_now < time_final:
        next_cur_time = time_now + step
        next_value = calculate_dynamic_values(
            time_now, next_cur_time, dynamic_i3_ul, step)

        time_now = next_cur_time
        dynamic_i3_ul = next_value

        iterational_result[time_now] = dynamic_i3_ul[0] * L

    return iterational_result


def main():
    values = [0, 0]

    result_of_calculating = calculate_output(
        curr_time, time_to_finish, values, size_of_step)
    
    time_now_list = []
    dynamic_i3_ul = []
    for time, i3_ul in result_of_calculating.items():
        time_now_list.append(time)
        dynamic_i3_ul.append(i3_ul)
    
    print('U2: ' + str(values[1]))
    plt.plot(time_now_list, dynamic_i3_ul)
    plt.show()


if __name__ == '__main__':
    main()
