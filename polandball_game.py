def main():
    polandball_word_num, enemyball_word_num = map(int, input().split(maxsplit=1))

    polandball_words = [input() for _ in range(polandball_word_num)]
    enemyball_words = [input() for _ in range(enemyball_word_num)]

    if enemyball_word_num > polandball_word_num:
        print("NO")
        return
    elif polandball_word_num > enemyball_word_num:
        print("YES")
        return
    else:
        '''
            Find the freqency of words that both balls know
            
            Time: O(n)
            Space: O(n)
        '''
        repeated_words = {}

        for word in polandball_words:
            repeated_words[word] = repeated_words.get(word, 0) + 1

        for word in enemyball_words:
            repeated_words[word] = repeated_words.get(word, 0) + 1


        '''
            Find the number of words that both balls know
            
            Time: O(n)
            Space: O(1)
        '''
        num_of_repeated_words = 0
        for _, freq in repeated_words.items():
            if freq > 1:
                num_of_repeated_words += 1

        '''
            Given both balls know the same number of words,
            if the number of words that both balls know is
            even then PolandBall loses its advantage,
            otherwise, PolandBall wins
        '''
        if num_of_repeated_words % 2 == 0:
            print("NO")
        else:
            print("YES")

        return


if __name__ == "__main__":
    main()