def convert_to_d_h_m_s(seconds):
    hours, minutes = divmod(minutes, 60)
    return days, hours, minutes, seconds
if __name__ == '__main__':
    for seconds in [ 11, 61, 3601, 3668, 86400, 86401, 90061, 1043573894573948573 ]:
        print("{0} seconds: {1[0]} days, {1[1]} hours, {1[2]} minutes, {1[3]} seconds".format(
              seconds, convert_to_d_h_m_s(seconds)))
