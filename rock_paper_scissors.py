import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n") # выбор пользователя
    computer = random.choice(['r', 'p', 's']) # случайный выбор компьютеру

    if user == computer:
        return 'It\'s a tie'
    # если одинаковые, то ничья
    # логика по силе r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'
    # если побеждаем, то высвечивается победа
    return 'You lost!'
    # при проигрыше высвечивается поражение
def is_win(player, opponent):
    # возвращаем тру если игрок выиграл
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
