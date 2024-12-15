import numpy as np

def day13(part_two = False):
    machine = {}
    total_prize = 0

    def iwn(num, accuracy = 0.001):
        minv = round(num) - accuracy
        maxv = round(num) + accuracy
        return minv < num < maxv

    with open('../data/d13.txt', 'r') as file:

        for line in file:

            vec = [vec.strip() for vec in line.split(':')]
            
            if vec[0] == 'Button A' or vec[0] == 'Button B':
                machine[vec[0][-1]] = (int(vec[1].split(',')[0].split('+')[1]), int(vec[1].split(',')[1].split('+')[1]))
            elif vec[0] == 'Prize':
                machine['P'] = (int(vec[1].split(',')[0].split('=')[1]), int(vec[1].split(',')[1].split('=')[1]))

                if part_two:
                    machine['P'] = (machine['P'][0] + 10000000000000, machine['P'][1] + 10000000000000)

                A = np.transpose([list(machine['A']), list(machine['B'])])
                b = list(machine['P'])
                
                if abs(np.linalg.det(A)) > 0.01:
                    
                    invA = np.linalg.inv(A)
                    x = np.matmul(invA, b)

                    if iwn(x[0]) and iwn(x[1]) and -0.01 <= x[0] and -0.01 <= x[1]:
                        if part_two or (not part_two and x[0] < 100.01 and x[1] < 100.01):
                            total_prize += int(round(x[0]) * 3 + round(x[1]))

                else:
                    prize = []

                    div1 = b[0]/A[0][0]
                    div2 = b[1]/A[1][0]
                    if round(div1, 2) == round(div2, 2) and iwn(div1) and iwn(div2):
                        prize.append(int(3 * round(div1)))
                    
                    div1 = b[0]/A[0][1]
                    div2 = b[1]/A[1][1]
                    if round(div1, 2) == round(div2, 2) and iwn(div1) and iwn(div2):
                        prize.append(int(round(div1)))

                    if len(prize) != 0:
                        total_prize += min(prize)

    if part_two:
        print("Part 2: " + str(total_prize))
    else:
        print("Part 1: " + str(total_prize))

# Part 1
day13()

# Part 2
day13(part_two = True)

