
##########################################################################
# Viterbi Algorithm for HMM
# dp, time complexity O(mn^2), m is the length of sequence of observation, n is the number of hidden states
##########################################################################


# five elements for HMM
states = ('Healthy', 'Fever')

observations = ('normal', 'cold', 'dizzy')

start_probability = {'Healthy': 0.6, 'Fever': 0.4}

transition_probability = {
    'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
    'Fever':   {'Healthy': 0.4, 'Fever': 0.6},
}

emission_probability = {
    'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
    'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
}


def Viterbit(obs, states, s_pro, t_pro, e_pro):
    # init path: path[s] represents the path ends with s
    path = {s: [] for s in states}
    path_pro = {s: s_pro[s] * e_pro[s][obs[0]] for s in states}

    for i in range(1, len(obs)):
        last_pro = path_pro
        for curr_state in states:
            max_pro, last_sta = max(((last_pro[last_state] * t_pro[last_state][curr_state] * e_pro[curr_state][obs[i]], last_state)
                                     for last_state in states))
            # update path
            path[curr_state].append(last_sta)
            
            # update path probability
            path_pro[curr_state] = max_pro
            

    # path add end
    for s in states:
        path[s].append(s)

    # find the final largest probability
    max_path = path[max(path_pro)]

    return max_path


if __name__ == '__main__':
    obs = ['normal', 'cold', 'dizzy']
    print(Viterbit(obs, states, start_probability,
                   transition_probability, emission_probability))
