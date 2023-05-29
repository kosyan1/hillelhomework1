def group_by_surname(list_of_enrollees):
    count_a_i = 0
    count_j_p = 0
    count_q_t = 0
    count_u_z = 0

    for enrollee in list_of_enrollees:
        surname = enrollee.split()
        surname = surname[1]

        if surname[0] >= 'A' and surname[0] <= 'I':
            count_a_i += 1
        elif surname[0] >= 'J' and surname[0] <= 'P':
            count_j_p += 1
        elif surname[0] >= 'Q' and surname[0] <= 'T':
            count_q_t += 1
        elif surname[0] >= 'U' and surname[0] <= 'Z':
            count_u_z += 1

    return count_a_i, count_j_p, count_q_t, count_u_z

enrollees = ['James Hetfield', 'Lars Ulrich', 'Kirk Hammett', 'Robert Trujillo', 'Cliff Burton', 'Jason Newsted']

result = group_by_surname(enrollees)

print(result)
