import random
def player(prev_play,opponent_history=[]):
    if prev_play!="":
        opponent_history.append(prev_play)
    if len(opponent_history)==0:
        return "R"
    #Quincy - Cycle Detection
    cycle_len=5
    if len(opponent_history)>=cycle_len:
        last_seq=opponent_history[-cycle_len:]
        if last_seq==["R","P","S","R","P"]:
            cycle=["R","P","S","R","P"]
            next_index=len(opponent_history)%len(cycle)
            predicted=cycle[next_index]
            return beats(predicted)
    
    #Kris - Mirrors Last Play
    if len(opponent_history)>=2:
        if opponent_history[-1]==player.last_play:
            predicted=player.last_play
            move=beats(predicted)
            player.last_play=move
            return move
    
    #Abbey
    if len(opponent_history)>=2:
        last_two="".join(opponent_history[-2:])
        transition={}
        for i in range(len(opponent_history)-2):
            seq="".join(opponent_history[i:i+2])
            next_move=opponent_history[i+2]
            if seq not in transition:
                transition[seq]={"R":0,"P":0,"S":0}
            transition[seq][next_move]+=1
        if last_two in transition:
            predicted=max(transition[last_two],key=transition[last_two].get)
            move=beats(predicted)
            player.last_play=move
            return move
        
        #Mrugesh - Frequency Analysis
        counts = {
            "R": opponent_history.count("R"),
            "P": opponent_history.count("P"),
            "S": opponent_history.count("S")
        }
        predicted=max(counts,key=counts.get)
        move=beats(predicted)
        player.last_play=move
        return move
def beats(move):
    if move=="R":
        return "P"
    if move=="P":
        return "S"
    if move=="S":
        return "R"
player.last_play="R"