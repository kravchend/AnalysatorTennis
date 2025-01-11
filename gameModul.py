import random


def format_message(*args):
    return ' '.join(str(arg) for arg in args)


def play_full_game(name_1, name_2, p1_1, p2_1, p3_1, p4_1, p1_2, p2_2, p3_2, p4_2, callback):
    callback(format_message(f'Начало игры: {name_1} vs {name_2}'))
    result = {name_1: 00, name_2: 00, 'game_1': 0, 'game_2': 0, 'sett_1': 0, 'sett_2': 0, 'break_1': 0, 'break_2': 0, }
    bal_1 = 15
    bal_2 = 10
    server = name_1
    reserver = name_2
    a, b = 0, 0
    res = []

    def winnerGamer_1(name_1, p1_1, p2_1, p3_1, p4_1):
        win_chance_1 = float((p1_1 * p2_1) / 1000)
        win_chance_2 = float((p1_2 * p2_2) / 1000)
        win_chance_1_2 = float((p1_1 * p2_1) / 1000) + (1 - (p1_1 / 100)) * ((p3_1 * p4_1) / 1000)
        win_chance_2_2 = float((p1_2 * p2_2) / 1000) + (1 - (p1_2 / 100)) * ((p3_2 * p4_2) / 1000)
        win_P1_1 = random.randint(0, 100)
        if win_P1_1 <= p1_1:
            callback(format_message('1st service'))
            winner = random.choices([name_1, name_2], [win_chance_1, win_chance_2])[0]
            return winner
        else:
            win_P3_1 = random.randint(0, 100)
            if win_P3_1 <= p3_1:
                callback(format_message('2nd service'))
                winner = random.choices([name_1, name_2], [win_chance_1_2, win_chance_2_2])[0]
                return winner
            else:
                callback(format_message('Double faute!'))
                return name_2

    def winnerGamer_2(name_2, p1_2, p2_2, p3_2, p4_2):
        win_chance_1 = float((p1_1 * p2_1) / 1000)
        win_chance_2 = float((p1_2 * p2_2) / 1000)
        win_chance_1_2 = float((p1_1 * p2_1) / 1000) + (1 - (p1_1 / 100)) * ((p3_1 * p4_1) / 1000)
        win_chance_2_2 = float((p1_2 * p2_2) / 1000) + (1 - (p1_2 / 100)) * ((p3_2 * p4_2) / 1000)
        win_P2_2 = random.randint(0, 100)
        if win_P2_2 <= p1_2:
            callback(format_message('1st service'))
            winner = random.choices([name_1, name_2], [win_chance_1, win_chance_2])[0]
            return winner
        else:
            win_P3_2 = random.randint(1, 100)
            if win_P3_2 <= p3_2:
                callback(format_message('2nd service'))
                winner = random.choices([name_1, name_2], [win_chance_1_2, win_chance_2_2])[0]
                return winner
            else:
                callback(format_message('Double faute!'))
                return name_1

    while result['sett_1'] < 3 or result['sett_2'] < 3:
        if server == name_1:
            winner = winnerGamer_1(name_1, p1_1, p2_1, p3_1, p4_1)
        else:
            winner = winnerGamer_2(name_2, p1_2, p2_2, p3_2, p4_2)
        if result['game_1'] == 6 and result['game_2'] == 6:
            if result['break_1'] >= 0 and result['break_2'] >= 0:
                if result['break_1'] == 0 and result['break_2'] == 0:
                    if winner == server == name_1:
                        result[name_1] += 1
                        result['break_1'] += 1
                        callback(
                            format_message(name_1, ' - ', name_2, '   ', result['break_1'], '-', result['break_2']))
                        server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                    elif winner == reserver == name_1:
                        result[name_1] += 1
                        result['break_1'] += 1
                        callback(
                            format_message(name_2, ' - ', name_1, '   ', result['break_2'], '-', result['break_1']))
                        server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                    elif winner == server == name_2:
                        result[name_2] += 1
                        result['break_2'] += 1
                        callback(
                            format_message(name_2, ' - ', name_1, '   ', result['break_2'], '-', result['break_1']))
                        server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                    elif winner == reserver == name_2:
                        result[name_2] += 1
                        result['break_2'] += 1
                        callback(
                            format_message(name_1, ' - ', name_2, '   ', result['break_1'], '-', result['break_2']))
                        server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                elif result[name_1] >= 0 and result[name_2] >= 1 or result[name_1] >= 1 and result[name_2] >= 0:
                    if winner == server == name_1:
                        result[name_1] += 1
                        result['break_1'] += 1
                        if result['break_1'] >= 7 and (result['break_1'] - result['break_2']) >= 2:
                            result['game_1'] = 7
                            result['sett_1'] += 1
                            callback(
                                format_message('Game', name_1, ' - ', name_2, result['game_1'], '-', result['game_2'],
                                               '  ', '(',
                                               result['break_1'], '-', result['break_2'], ')', '  ', result['sett_1'],
                                               '-',
                                               result['sett_2']))
                            res.append(result['game_1'])
                            res.append(result['game_2'])
                            result['game_1'], result['game_2'], result['break_1'], result['break_2'] = 0, 0, 0, 0
                            result[name_1], result[name_2] = 0, 0
                        else:
                            callback(
                                format_message(name_1, ' - ', name_2, '   ', result['break_1'], '-', result['break_2']))
                            if (result[name_1] + result[name_2]) % 2 == 1:
                                server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                    elif winner == reserver == name_1:
                        result[name_1] += 1
                        result['break_1'] += 1
                        if result['break_1'] >= 7 and (result['break_1'] - result['break_2']) >= 2:
                            result['game_1'] = 7
                            result['sett_1'] += 1
                            callback(
                                format_message('Game', name_2, ' - ', name_1, result['game_2'], '-', result['game_1'],
                                               '  ', '(',
                                               result['break_2'], '-', result['break_1'], ')', '  ', result['sett_2'],
                                               '-',
                                               result['sett_1']))
                            res.append(result['game_1'])
                            res.append(result['game_2'])
                            result['game_1'], result['game_2'], result['break_1'], result['break_2'] = 0, 0, 0, 0
                            result[name_1], result[name_2] = 0, 0
                        else:
                            callback(
                                format_message(name_2, ' - ', name_1, '   ', result['break_2'], '-', result['break_1']))
                            if (result[name_1] + result[name_2]) % 2 == 1:
                                server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                    elif winner == server == name_2:
                        result[name_2] += 1
                        result['break_2'] += 1
                        if result['break_2'] >= 7 and (result['break_2'] - result['break_1']) >= 2:
                            result['game_2'] = 7
                            result['sett_2'] += 1
                            callback(
                                format_message('Game', name_2, ' - ', name_1, result['game_2'], '-', result['game_1'],
                                               '  ', '(',
                                               result['break_2'], '-', result['break_1'], ')', '  ', result['sett_2'],
                                               '-',
                                               result['sett_1']))
                            res.append(result['game_1'])
                            res.append(result['game_2'])
                            result['game_1'], result['game_2'], result['break_1'], result['break_2'] = 0, 0, 0, 0
                            result[name_1], result[name_2] = 0, 0
                        else:
                            callback(
                                format_message(name_2, ' - ', name_1, '   ', result['break_2'], '-', result['break_1']))
                            if (result[name_1] + result[name_2]) % 2 == 1:
                                server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                    elif winner == reserver == name_2:
                        result[name_2] += 1
                        result['break_2'] += 1
                        if result['break_2'] >= 7 and (result['break_2'] - result['break_1']) >= 2:
                            result['game_2'] = 7
                            result['sett_2'] += 1
                            callback(
                                format_message('Game', name_1, ' - ', name_2, result['game_1'], '-', result['game_2'],
                                               '  ', '(',
                                               result['break_1'], '-', result['break_2'], ')', '  ', result['sett_1'],
                                               '-',
                                               result['sett_2']))
                            res.append(result['game_1'])
                            res.append(result['game_2'])
                            result['game_1'], result['game_2'], result['break_1'], result['break_2'] = 0, 0, 0, 0
                            result[name_1], result[name_2] = 0, 0
                        else:
                            callback(
                                format_message(name_1, ' - ', name_2, '   ', result['break_1'], '-', result['break_2']))
                            if (result[name_1] + result[name_2]) % 2 == 1:
                                server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)

                if result['sett_1'] == 3 or result['sett_2'] == 3:
                    if len(res) == 6 and result['sett_1'] == 3:
                        callback(format_message('Final score: ', res[0], '-', res[1], '   ', res[2], '-', res[3], '   ',
                                                res[4], '-',
                                                res[5]))
                    elif len(res) == 8 and result['sett_1'] == 3:
                        callback(format_message('Final score: ', res[0], '-', res[1], '   ', res[2], '-', res[3], '   ',
                                                res[4], '-',
                                                res[5],
                                                '   ', res[6], '-', res[7]))
                    elif len(res) == 10 and result['sett_1'] == 3:
                        callback(format_message('Final score: ', res[0], '-', res[1], '   ', res[2], '-', res[3], '   ',
                                                res[4], '-',
                                                res[5],
                                                '   ', res[6], '-', res[7], '   ', res[8], '-', res[9]))
                    if len(res) == 6 and result['sett_2'] == 3:
                        callback(
                            format_message('Final score: ', res[1], '-', res[0], '   ', res[3], '-', res[2], res[5],
                                           '-', res[4]))
                    elif len(res) == 8 and result['sett_2'] == 3:
                        callback(format_message('Final score: ', res[1], '-', res[0], '   ', res[3], '-', res[2], '   ',
                                                res[5], '-',
                                                res[4],
                                                '   ', res[7], '-', res[6]))
                    elif len(res) == 10 and result['sett_2'] == 3:
                        callback(format_message('Final score: ', res[1], '-', res[0], '   ', res[3], '-', res[2], '   ',
                                                res[5], '-',
                                                res[4],
                                                '   ', res[7], '-', res[6], '   ', res[9], '-', res[8]))
                    break

        else:
            if result[winner] < 30:
                result[winner] += bal_1
                if server == name_1:
                    callback(format_message(name_1, ' - ', name_2, '   ', result[name_1], '-', result[name_2], '   ',
                                            result['game_1'],
                                            '-',
                                            result['game_2'], '   ', result['sett_1'], '-', result['sett_2']))
                elif server == name_2:
                    callback(format_message(name_2, ' - ', name_1, '   ', result[name_2], '-', result[name_1], '   ',
                                            result['game_2'],
                                            '-',
                                            result['game_1'], '   ', result['sett_2'], '-', result['sett_1']))
            elif result[winner] == 30:
                result[winner] += bal_2
                if server == name_1:
                    callback(format_message(name_1, ' - ', name_2, '   ', result[name_1], '-', result[name_2], '   ',
                                            result['game_1'],
                                            '-',
                                            result['game_2'], '   ', result['sett_1'], '-', result['sett_2']))
                elif server == name_2:
                    callback(format_message(name_2, ' - ', name_1, '   ', result[name_2], '-', result[name_1], '   ',
                                            result['game_2'],
                                            '-',
                                            result['game_1'], '   ', result['sett_2'], '-', result['sett_1']))
            elif result[winner] == 40 and winner == name_1 and result[name_2] < 40:
                result['game_1'] += 1
                if server == name_1 and result['game_1'] >= 6 and (result['game_1'] - result['game_2']) >= 2:
                    result['sett_1'] += 1
                    callback(format_message('Game', winner, ' ', result['game_1'], '-', result['game_2'], ' ',
                                            result['sett_1'], '-',
                                            result['sett_2']))
                    res.append(result['game_1'])
                    res.append(result['game_2'])
                    result['game_1'], result['game_2'], result[name_1], result[name_2] = 0, 0, 0, 0
                    server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                elif server == name_1 and result['game_1'] < 6 or server == name_1 and result['game_1'] >= 6 and (
                        result['game_1'] - result['game_2']) < 2:
                    callback(format_message('Game', winner, ' ', result['game_1'], '-', result['game_2'], ' ',
                                            result['sett_1'], '-',
                                            result['sett_2']))
                    result[name_1] = 0
                    result[name_2] = 0
                    server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                elif server == name_2 and result['game_1'] >= 6 and (result['game_1'] - result['game_2']) >= 2:
                    result['sett_1'] += 1
                    callback(format_message('Game', winner, ' ', result['game_2'], '-', result['game_1'], ' ',
                                            result['sett_2'], '-',
                                            result['sett_1']))
                    res.append(result['game_1'])
                    res.append(result['game_2'])
                    result['game_1'], result['game_2'], result[name_1], result[name_2] = 0, 0, 0, 0
                    server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                elif server == name_2 and result['game_2'] < 6 or server == name_2 and result['game_2'] >= 6 and (
                        result['game_2'] - result['game_1']) < 2:
                    callback(format_message('Game', winner, ' ', result['game_2'], '-', result['game_1'], ' ',
                                            result['sett_2'], '-',
                                            result['sett_1']))
                    result[name_1] = 0
                    result[name_2] = 0
                    server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
            elif result[winner] == 40 and winner == name_2 and result[name_1] < 40:
                result['game_2'] += 1
                if server == name_1 and result['game_2'] >= 6 and (result['game_2'] - result['game_1']) >= 2:
                    result['sett_2'] += 1
                    callback(format_message('Game', winner, ' ', result['game_1'], '-', result['game_2'], ' ',
                                            result['sett_1'], '-',
                                            result['sett_2']))
                    res.append(result['game_1'])
                    res.append(result['game_2'])
                    result['game_1'], result['game_2'], result[name_1], result[name_2] = 0, 0, 0, 0
                    server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                elif server == name_1 and result['game_1'] < 6 or server == name_1 and result['game_1'] >= 6 and (
                        result['game_1'] - result['game_2']) < 2:
                    callback(format_message('Game', winner, ' ', result['game_1'], '-', result['game_2'], ' ',
                                            result['sett_1'], '-',
                                            result['sett_2']))
                    result[name_1] = 0
                    result[name_2] = 0
                    server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                elif server == name_2 and result['game_2'] >= 6 and (result['game_2'] - result['game_1']) >= 2:
                    result['sett_2'] += 1
                    callback(format_message('Game', winner, ' ', result['game_2'], '-', result['game_1'], ' ',
                                            result['sett_2'], '-',
                                            result['sett_1']))
                    res.append(result['game_1'])
                    res.append(result['game_2'])
                    result['game_1'], result['game_2'], result[name_1], result[name_2] = 0, 0, 0, 0
                    server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                elif server == name_2 and result['game_2'] < 6 or server == name_2 and result['game_2'] >= 6 and (
                        result['game_2'] - result['game_1']) < 2:
                    callback(format_message('Game', winner, ' ', result['game_2'], '-', result['game_1'], ' ',
                                            result['sett_2'], '-',
                                            result['sett_1']))
                    result[name_1] = 0
                    result[name_2] = 0
                    server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
            elif winner == server and result[server] == (40 + a) and result[reserver] == (40 + a):
                result[winner] += 1
                callback(format_message('Avantage service'))
                a += 1
            elif winner == reserver and result[server] == (40 + a) and result[reserver] == (40 + a):
                result[winner] += 1
                callback(format_message('Avantage retour'))
                a += 1
            elif winner == server == name_1 and result[server] == (41 + b) and result[reserver] == (40 + b):
                result['game_1'] += 1
                if winner == name_1 and result['game_1'] >= 6 and (result['game_1'] - result['game_2']) >= 2:
                    result['sett_1'] += 1
                    callback(format_message('Game', winner, ' ', result['game_1'], '-', result['game_2'], ' ',
                                            result['sett_1'], '-',
                                            result['sett_2']))
                    res.append(result['game_1'])
                    res.append(result['game_2'])
                    a, b, result['game_1'], result['game_2'], result[name_1], result[name_2] = 0, 0, 0, 0, 0, 0
                    server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                elif server == name_1 and result['game_1'] < 6 or server == name_1 and result['game_1'] >= 6 and (
                        result['game_1'] - result['game_2']) < 2:
                    callback(format_message('Game', winner, ' ', result['game_1'], '-', result['game_2'], ' ',
                                            result['sett_1'], '-',
                                            result['sett_2']))
                    result[name_1], result[name_2], a, b = 0, 0, 0, 0
                    server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
            elif winner == server == name_2 and result[server] == (41 + b) and result[reserver] == (40 + b):
                result['game_2'] += 1
                if server == name_2 and result['game_2'] >= 6 and (result['game_2'] - result['game_1']) >= 2:
                    result['sett_2'] += 1
                    callback(format_message('Game', winner, ' ', result['game_2'], '-', result['game_1'], ' ',
                                            result['sett_2'], '-',
                                            result['sett_1']))
                    res.append(result['game_1'])
                    res.append(result['game_2'])
                    a, b, result['game_1'], result['game_2'], result[name_1], result[name_2] = 0, 0, 0, 0, 0, 0
                    server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                elif server == name_2 and result['game_2'] < 6 or server == name_2 and result['game_2'] >= 6 and (
                        result['game_2'] - result['game_1']) < 2:
                    callback(format_message('Game', winner, ' ', result['game_2'], '-', result['game_1'], ' ',
                                            result['sett_2'], '-',
                                            result['sett_1']))
                    result[name_1], result[name_2], a, b = 0, 0, 0, 0
                    server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
            elif winner == reserver and result[server] == (41 + b) and result[reserver] == (40 + b):
                result[winner] += 1
                callback(format_message('Deuce'))
                b += 1
            elif winner == server and result[server] == (40 + b) and result[reserver] == (41 + b):
                result[winner] += 1
                callback(format_message('Deuce'))
                b += 1
            elif winner == reserver and result[server] == (40 + b) and result[reserver] == (41 + b):
                if reserver == name_2:
                    result['game_2'] += 1
                    if reserver == name_2 and result['game_2'] >= 6 and (result['game_2'] - result['game_1']) >= 2:
                        result['sett_2'] += 1
                        callback(format_message('Game', winner, ' ', result['game_1'], '-', result['game_2'], ' ',
                                                result['sett_1'],
                                                '-',
                                                result['sett_2']))
                        res.append(result['game_1'])
                        res.append(result['game_2'])
                        a, b, result['game_1'], result['game_2'], result[name_1], result[name_2] = 0, 0, 0, 0, 0, 0
                        server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                    elif reserver == name_2 and result['game_2'] < 6 or reserver == name_2 and result[
                        'game_2'] >= 6 and (result['game_2'] - result['game_1']) < 2:
                        callback(format_message('Game', winner, ' ', result['game_1'], '-', result['game_2'], ' ',
                                                result['sett_1'],
                                                '-',
                                                result['sett_2']))
                        result[name_1], result[name_2], a, b = 0, 0, 0, 0
                        server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                elif reserver == name_1:
                    result['game_1'] += 1
                    if reserver == name_1 and result['game_1'] >= 6 and (result['game_1'] - result['game_2']) >= 2:
                        result['sett_1'] += 1
                        callback(format_message('Game', winner, ' ', result['game_2'], '-', result['game_1'], ' ',
                                                result['sett_2'],
                                                '-',
                                                result['sett_1']))
                        res.append(result['game_1'])
                        res.append(result['game_2'])
                        a, b, result['game_1'], result['game_2'], result[name_1], result[name_2] = 0, 0, 0, 0, 0, 0
                        server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)
                    elif reserver == name_1 and result['game_1'] < 6 or reserver == name_1 and result[
                        'game_1'] >= 6 and (result['game_1'] - result['game_2']) < 2:
                        callback(format_message('Game', winner, ' ', result['game_2'], '-', result['game_1'], ' ',
                                                result['sett_2'],
                                                '-',
                                                result['sett_1']))
                        result[name_1], result[name_2], a, b = 0, 0, 0, 0
                        server, reserver = (name_2, name_1) if server == name_1 else (name_1, name_2)

        if result['sett_1'] == 3 or result['sett_2'] == 3:
            if len(res) == 6 and result['sett_1'] == 3:
                callback(
                    format_message('Final score: ', res[0], '-', res[1], '   ', res[2], '-', res[3], '   ', res[4], '-',
                                   res[5]))
            elif len(res) == 8 and result['sett_1'] == 3:
                callback(
                    format_message('Final score: ', res[0], '-', res[1], '   ', res[2], '-', res[3], '   ', res[4], '-',
                                   res[5],
                                   '   ', res[6], '-', res[7]))
            elif len(res) == 10 and result['sett_1'] == 3:
                callback(
                    format_message('Final score: ', res[0], '-', res[1], '   ', res[2], '-', res[3], '   ', res[4], '-',
                                   res[5],
                                   '   ', res[6], '-', res[7], '   ', res[8], '-', res[9]))
            if len(res) == 6 and result['sett_2'] == 3:
                callback(
                    format_message('Final score: ', res[1], '-', res[0], '   ', res[3], '-', res[2], '   ', res[5], '-',
                                   res[4]))
            elif len(res) == 8 and result['sett_2'] == 3:
                callback(
                    format_message('Final score: ', res[1], '-', res[0], '   ', res[3], '-', res[2], '   ', res[5], '-',
                                   res[4],
                                   '   ', res[7], '-', res[6]))
            elif len(res) == 10 and result['sett_2'] == 3:
                callback(
                    format_message('Final score: ', res[1], '-', res[0], '   ', res[3], '-', res[2], '   ', res[5], '-',
                                   res[4],
                                   '   ', res[7], '-', res[6], '   ', res[9], '-', res[8]))
            break

    return result, res
