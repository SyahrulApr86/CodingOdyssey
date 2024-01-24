# https://www.codewars.com/kata/54e6533c92449cc251001667/

def unique_in_order(sequence):
    return [sequence[i] for i in range(len(sequence)) if sequence[i] != sequence[i-1] or i == 0]