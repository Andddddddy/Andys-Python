"""
### 根據課程講述的內容, 請計算出下列剩餘所有情況的
若有一個人連續觀察到三天水草都是乾燥的(Dry), 則這三天的天氣機率為何？(可參考講義第13頁)
(Hint: 共有8種可能機率)

"""

observations = ('dry', 'dry', 'dry') #實際上觀察到的狀態為dry, dry, dry
states = ('sunny', 'rainy')
start_probability = {'sunny': 0.4, 'rainy': 0.6}
transition_probability = {'sunny':{'sunny':0.6, 'rainy':0.4},
                          'rainy': {'sunny':0.3, 'rainy':0.7}}
emission_probatility = {'sunny': {'dry':0.6, 'damp':0.3, 'soggy':0.1},
                        'rainy': {'dry':0.1, 'damp':0.4, 'soggy':0.5}}


def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    # Initialize base cases (t == 0)
    for y in states:
        ###<your codes>###
        path[y] = [y]
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        
    # Run Viterbi for t > 0
    for t in range(1,len(obs)):
        ###<your codes>###
        V.append({})
        newpath = {}
        for i, j in path.items():
            j.append('sunny')
            newpath[i] = j

            V[t][i] = V[t-1][i] * trans_p[newpath[i][-2]][newpath[i][-1]] * emit_p[newpath[i][-1]][obs[t]]
            

        # Don't need to remember the old paths
        path = newpath
    
    (prob, state) = max([(V[len(observations) - 1][final_state], final_state) for final_state in states])
    return (prob, path[state])



result = viterbi(observations,
                 states,
                 start_probability,
                 transition_probability,
                 emission_probatility)


result