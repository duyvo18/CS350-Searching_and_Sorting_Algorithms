def main():
    polandball_word_num, enemyball_word_num = map(int, input().split(maxsplit=1))
    
    if enemyball_word_num > polandball_word_num:
        print('NO')
        return
    elif polandball_word_num > enemyball_word_num:
        print('YES')
        return
    else:
        polandball_words = [input() for _ in range(polandball_word_num)]
        enemyball_words = [input() for _ in range(enemyball_word_num)]
        
        # poland_num_of_repeated_words >= enemy_num_of_repeated_words -> poland wins
        
        print('YES')
        return

if __name__ == '__main__':
    main()