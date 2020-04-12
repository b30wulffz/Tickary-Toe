from random import choice
from ursina import *
import time
from multiprocessing import Process


### Backend ###

# global advance_screen, game_screen, home_screen


class Problem():

    def __init__(self, dim, cutoff):
        self.state = [['' for x in range(0, dim)] for y in range(0, dim)]
        self.dim = dim
        self.cutoff = cutoff

    def Player(self, state):
        # assuming a player had already used his turn
        dim = len(state)
        c = 0
        for i in range(0, dim):
            for j in range(0, dim):
                if state[i][j] == "X":
                    c += 1
                elif state[i][j] == "O":
                    c -= 1
        if c > 0:
            return "O"
        elif c < 0:
            return "X"
        else:
            return "-"

    def Actions(self, state):
        dim = len(state)

        empty = []

        for i in range(0, dim):
            for j in range(0, dim):
                if state[i][j] == "":
                    empty.append((i, j))

        return empty

    def Result(self, state, act, isHuman):
        # here action is going to be of form (x,y)
        if isHuman:
            state[act[0]][act[1]] = "X"
        else:
            state[act[0]][act[1]] = "O"

        return state

    def TerminalTest(self, state, cutoff):
        # here cutoff represents the count of elements to be taken consecutively
        dim = len(state)

        # Check for row
        for i in range(0, dim):
            initVal = ""
            count = 0
            won_index = []
            for j in range(0, dim):

                if initVal == "":
                    if state[i][j] != "":
                        initVal = state[i][j]
                        won_index.append((i, j))
                        count = 1
                else:
                    if state[i][j] == initVal:
                        won_index.append((i, j))
                        count += 1
                    else:
                        if state[i][j] == "":
                            initVal = ""
                            won_index = []
                            count = 0
                        else:
                            initVal = state[i][j]
                            won_index.append((i, j))
                            count = 1

                if count == cutoff:
                    return [initVal, won_index]

        # Check for column
        for i in range(0, dim):
            initVal = ""
            count = 0
            won_index = []
            for j in range(0, dim):

                if initVal == "":
                    if state[j][i] != "":
                        initVal = state[j][i]
                        won_index.append((j, i))
                        count = 1
                else:
                    if state[j][i] == initVal:
                        won_index.append((j, i))
                        count += 1
                    else:
                        if state[j][i] == "":
                            initVal = ""
                            won_index = []
                            count = 0
                        else:
                            initVal = state[j][i]
                            won_index.append((j, i))
                            count = 1

                if count == cutoff:
                    return [initVal, won_index]

        # Check for diagonal L to R
        for i in range(0, dim):
            x = 0
            y = i
            initVal = ""
            count = 0
            won_index = []

            while x < dim and y < dim:
                if initVal == "":
                    if state[x][y] != "":
                        initVal = state[x][y]
                        won_index.append((x, y))
                        count = 1
                else:
                    if state[x][y] == initVal:
                        won_index.append((x, y))
                        count += 1
                    else:
                        if state[x][y] == "":
                            initVal = ""
                            won_index = []
                            count = 0
                        else:
                            initVal = state[x][y]
                            won_index.append((x, y))
                            count = 1
                if count == cutoff:
                    return [initVal, won_index]

                x += 1
                y += 1

            x = i
            y = 0
            initVal = ""
            count = 0
            won_index = []

            while x < dim and y < dim:
                if initVal == "":
                    if state[x][y] != "":
                        initVal = state[x][y]
                        won_index.append((x, y))
                        count = 1
                else:
                    if state[x][y] == initVal:
                        won_index.append((x, y))
                        count += 1
                    else:
                        if state[x][y] == "":
                            initVal = ""
                            won_index = []
                            count = 0
                        else:
                            initVal = state[x][y]
                            won_index.append((x, y))
                            count = 1
                if count == cutoff:
                    return [initVal, won_index]

                x += 1
                y += 1

        # Check for diagonal R to L
        for i in range(0, dim):
            x = 0
            y = dim-i-1
            initVal = ""
            count = 0
            won_index = []

            while x < dim and y >= 0:
                if initVal == "":
                    if state[x][y] != "":
                        initVal = state[x][y]
                        won_index.append((x, y))
                        count = 1
                else:
                    if state[x][y] == initVal:
                        won_index.append((x, y))
                        count += 1
                    else:
                        if state[x][y] == "":
                            initVal = ""
                            won_index = []
                            count = 0
                        else:
                            initVal = state[x][y]
                            won_index.append((x, y))
                            count = 1
                if count == cutoff:
                    return [initVal, won_index]

                x += 1
                y -= 1

            x = i
            y = dim-1
            initVal = ""
            count = 0
            won_index = []

            while x < dim and y >= 0:
                if initVal == "":
                    if state[x][y] != "":
                        initVal = state[x][y]
                        won_index.append((x, y))
                        count = 1
                else:
                    if state[x][y] == initVal:
                        won_index.append((x, y))
                        count += 1
                    else:
                        if state[x][y] == "":
                            initVal = ""
                            won_index = []
                            count = 0
                        else:
                            initVal = state[x][y]
                            won_index.append((x, y))
                            count = 1
                if count == cutoff:
                    return [initVal, won_index]

                x += 1
                y -= 1

        empty = self.Actions(state)
        if len(empty) == 0:
            return ['T', []]

        return ['N', []]

    def Utility(self, player):
        if player == "X":
            return 1
        elif player == "O":
            return -1
        else:
            return 0

    def PrintBoard(self, state):
        dim = len(state)
        for i in range(0, dim):
            for j in range(0, dim):
                if state[i][j] == '':
                    print("-", end=" ")
                else:
                    print(state[i][j], end=" ")
            print()

    def CheckWinner(self, problem):
        result = self.TerminalTest(problem.state, problem.cutoff)
        winner = result[0]
        if winner != 'N':
            game_audio.stop()
            if winner == 'X':
                winner_audio.play()
                for ind in result[1]:
                    new_ind = (ind[0]*game_screen.dim) + ind[1]
                    game_screen.but_list[new_ind].color = color.turquoise
                game_screen.text.text = "You Won!"
                print("X won")
            elif winner == 'O':
                winner_audio.play()
                for ind in result[1]:
                    new_ind = (ind[0]*game_screen.dim) + ind[1]
                    game_screen.but_list[new_ind].color = color.rgb(
                        234, 82, 111)
                    # color.tint(
                    # color.lime, amount=.2)
                game_screen.text.text = "Computer Won!"
                print("O won")
            else:
                game_draw_audio.play()
                game_screen.text.text = "Its a Tie!"
                print("Match Tied")
            return True
        else:
            return False

### Heuristic ###


def calcScore(player, count):
    if count == 0:
        return 0
    if player == 'X':
        return (10**(count-1))
    elif player == 'O':
        return -(10**(count-1))
    return 0


def Heuristic(problem, state):
    # max elements in a row, column, diagonal
    dim = len(state)
    score = 0
    tempScore = 0

#     print("Row")

    # Check for row
    for i in range(0, dim):
        initVal = ""
        count = 0
        for j in range(0, dim):

            if initVal == "":
                if state[i][j] != "":
                    initVal = state[i][j]
                    count = 1
            else:
                if state[i][j] == initVal:
                    count += 1
                else:
                    #                     print(initVal, str(count))
                    score += calcScore(initVal, count)
                    if state[i][j] == "":
                        initVal = ""
                        count = 0
                    else:
                        initVal = state[i][j]
                        count = 1
#         print(initVal, str(count))
        score += calcScore(initVal, count)

#     print("Col")
    # Check for column
    for i in range(0, dim):
        initVal = ""
        count = 0
        for j in range(0, dim):

            if initVal == "":
                if state[j][i] != "":
                    initVal = state[j][i]
                    count = 1
            else:
                if state[j][i] == initVal:
                    count += 1
                else:
                    if count > 1:
                        #                         print(initVal, str(count))
                        score += calcScore(initVal, count)
                    if state[j][i] == "":
                        initVal = ""
                        count = 0
                    else:
                        initVal = state[j][i]
                        count = 1
        if count > 1:
            #             print(initVal, str(count))
            score += calcScore(initVal, count)

#     print("L2R")
    # Check for diagonal L to R
    for i in range(0, dim):
        x = 0
        y = i
        initVal = ""
        count = 0

        while x < dim and y < dim:
            if initVal == "":
                if state[x][y] != "":
                    initVal = state[x][y]
                    count = 1
            else:
                if count > 1:
                    #                     print(initVal, str(count))
                    score += calcScore(initVal, count)
                if state[x][y] == initVal:
                    count += 1
                else:
                    if state[x][y] == "":
                        initVal = ""
                        count = 0
                    else:
                        initVal = state[x][y]
                        count = 1
            x += 1
            y += 1
        if count > 1:
            #             print(initVal, str(count))
            score += calcScore(initVal, count)

        if i != 0:

            x = i
            y = 0
            initVal = ""
            count = 0

            while x < dim and y < dim:
                if initVal == "":
                    if state[x][y] != "":
                        initVal = state[x][y]
                        count = 1
                else:
                    if state[x][y] == initVal:
                        count += 1
                    else:
                        if count > 1:
                            #                             print(initVal, str(count))
                            score += calcScore(initVal, count)
                        if state[x][y] == "":
                            initVal = ""
                            count = 0
                        else:
                            initVal = state[x][y]
                            count = 1
                x += 1
                y += 1
            if count > 1:
                #                 print(initVal, str(count))
                score += calcScore(initVal, count)

#     print("R2L")
    # Check for diagonal R to L
    for i in range(0, dim):
        x = 0
        y = dim-i-1
        initVal = ""
        count = 0

        while x < dim and y >= 0:
            if initVal == "":
                if state[x][y] != "":
                    initVal = state[x][y]
                    count = 1
            else:
                if state[x][y] == initVal:
                    count += 1
                else:
                    if count > 1:
                        #                         print(initVal, str(count))
                        score += calcScore(initVal, count)
                    if state[x][y] == "":
                        initVal = ""
                        count = 0
                    else:
                        initVal = state[x][y]
                        count = 1
            x += 1
            y -= 1
        if count > 1:
            #             print(initVal, str(count))
            score += calcScore(initVal, count)

        if i > 0:
            x = i
            y = dim-1
            initVal = ""
            count = 0

            while x < dim and y >= 0:
                if initVal == "":
                    if state[x][y] != "":
                        initVal = state[x][y]
                        count = 1
                else:
                    if state[x][y] == initVal:
                        count += 1
                    else:
                        if count > 1:
                            #                             print(initVal, str(count))
                            score += calcScore(initVal, count)
                        if state[x][y] == "":
                            initVal = ""
                            count = 0
                        else:
                            initVal = state[x][y]
                            count = 1
                x += 1
                y -= 1
            if count > 1:
                #                 print(initVal, str(count))
                score += calcScore(initVal, count)
    return score

### Algorithms ###


def MaxValue(problem, state):
    #     print(state)
    check = problem.TerminalTest(state, problem.cutoff)[0]
    if check != 'N':
        return [(-1, -1), problem.Utility(check)]

    v = [(-1, -1), float("-inf")]
    for a in problem.Actions(state):
        result = MinValue(problem, problem.Result(state, a, True))
        state[a[0]][a[1]] = ""
        newMax = max(v[1], result[1])
        if newMax != v[1]:
            v = [a, newMax]
    return v


def MinValue(problem, state):
    #     print(state)
    check = problem.TerminalTest(state, problem.cutoff)[0]
    if check != 'N':
        return [(-1, -1), problem.Utility(check)]

    v = [(-1, -1), float("inf")]
    for a in problem.Actions(state):
        result = MaxValue(problem, problem.Result(state, a, False))
        state[a[0]][a[1]] = ""
        newMin = min(v[1], result[1])
        if newMin != v[1]:
            v = [a, newMin]
    return v

# alpha beta pruning


def MaxValueAB(problem, state, alpha, beta):
    #     print(state)
    check = problem.TerminalTest(state, problem.cutoff)[0]
    if check != 'N':
        return [(-1, -1), problem.Utility(check)]

    v = [(-1, -1), float("-inf")]
    for a in problem.Actions(state):
        result = MinValueAB(problem, problem.Result(
            state, a, True), alpha, beta)
        state[a[0]][a[1]] = ""

        # it compares just the two branched, if the condition a>=b satisfies, it doesn't check further

        newMax = max(v[1], result[1])
        if newMax != v[1]:
            v = [a, newMax]

        if v[1] >= beta:
            return v

        alpha = max(alpha, v[1])

    return v


def MinValueAB(problem, state, alpha, beta):
    #     print(state)
    check = problem.TerminalTest(state, problem.cutoff)[0]
    if check != 'N':
        return [(-1, -1), problem.Utility(check)]

    v = [(-1, -1), float("inf")]
    for a in problem.Actions(state):
        result = MaxValueAB(problem, problem.Result(
            state, a, False), alpha, beta)
        state[a[0]][a[1]] = ""

        newMin = min(v[1], result[1])
        if newMin != v[1]:
            v = [a, newMin]

        if v[1] <= alpha:
            return v

        beta = min(beta, v[1])

    return v


def MaxValueDepthLim(problem, state, depth, limit):
    #     print(state)
    check = problem.TerminalTest(state, problem.cutoff)[0]
    if check != 'N':
        return [(-1, -1), problem.Utility(check)]

    if depth == limit:
        return [(-1, -1), Heuristic(problem, state)]

    v = [(-1, -1), float("-inf")]
    for a in problem.Actions(state):
        result = MinValueDepthLim(
            problem, problem.Result(state, a, True), depth+1, limit)
        state[a[0]][a[1]] = ""
        newMax = max(v[1], result[1])
        if newMax != v[1]:
            v = [a, newMax]
    return v


def MinValueDepthLim(problem, state, depth, limit):
    #     print(state)
    check = problem.TerminalTest(state, problem.cutoff)[0]
    if check != 'N':
        return [(-1, -1), problem.Utility(check)]

    if depth == limit:
        return [(-1, -1), Heuristic(problem, state)]

    v = [(-1, -1), float("inf")]
    for a in problem.Actions(state):
        result = MaxValueDepthLim(problem, problem.Result(
            state, a, False), depth+1, limit)
        state[a[0]][a[1]] = ""
        newMin = min(v[1], result[1])
        if newMin != v[1]:
            v = [a, newMin]
    return v

# alpha beta pruning with depth limit


def MaxValueDepthLimAB(problem, state, alpha, beta, depth, limit):
    #     print(state)
    check = problem.TerminalTest(state, problem.cutoff)[0]
    if check != 'N':
        return [(-1, -1), problem.Utility(check)]

    if depth == limit:
        return [(-1, -1), Heuristic(problem, state)]

    v = [(-1, -1), float("-inf")]
    for a in problem.Actions(state):
        result = MinValueDepthLimAB(problem, problem.Result(
            state, a, True), alpha, beta, depth+1, limit)
        state[a[0]][a[1]] = ""

        # it compares just the two branched, if the condition a>=b satisfies, it doesn't check further

        newMax = max(v[1], result[1])
        if newMax != v[1]:
            v = [a, newMax]

        if v[1] >= beta:
            return v

        alpha = max(alpha, v[1])

    return v


def MinValueDepthLimAB(problem, state, alpha, beta, depth, limit):
    #     print(state)
    check = problem.TerminalTest(state, problem.cutoff)[0]
    if check != 'N':
        return [(-1, -1), problem.Utility(check)]

    if depth == limit:
        return [(-1, -1), Heuristic(problem, state)]

    v = [(-1, -1), float("inf")]
    for a in problem.Actions(state):
        result = MaxValueDepthLimAB(problem, problem.Result(
            state, a, False), alpha, beta, depth+1, limit)
        state[a[0]][a[1]] = ""

        newMin = min(v[1], result[1])
        if newMin != v[1]:
            v = [a, newMin]

        if v[1] <= alpha:
            return v

        beta = min(beta, v[1])

    return v


def AIalgo(problem, algo, lim=0):
    print("Wkwkwk")
    algo = algo[0]
    result = [(-1, -1), float("inf")]
    if algo == 'Basic Minimax':
        result = MinValue(problem, problem.state)
    elif algo == 'Alpha Beta Pruning':
        result = MinValueAB(problem, problem.state,
                            float("-inf"), float("inf"))
    elif algo == 'Depth Limited':
        result = MinValueDepthLim(problem, problem.state, 0, lim)
    elif algo == 'Pruning with Depth Limit':
        result = MinValueDepthLimAB(
            problem, problem.state, float("-inf"), float("inf"), 0, lim)

    if result[0] != (-1, -1):
        print("\nO turn:")
        x = result[0][0]
        y = result[0][1]
        problem.state[x][y] = 'O'
        problem.PrintBoard(problem.state)
        index = (x*game_screen.dim) + y
        but = game_screen.but_list[index]

        but.text = "O"
        but.color = color.rgb(255, 138, 91)
        but.disabled = True
        but.collision = False
        computer_play_audio.play()
        if not game_screen.board.CheckWinner(game_screen.board):
            game_screen.text.text = 'Your Turn!'
            # user_play = True
            # mouse.enabled = True
############################################################


app = Ursina()


class SplashScreen(Entity):
    def __init__(self, txtr='ursina_logo'):
        super().__init__()
        self.parent = camera.ui
        camera.overlay.fade_in(duration=0)
        self.logo = Sprite(name='ursina_splash', parent=self, texture=txtr,
                           world_z=camera.overlay.z-1, scale=.1, color=color.clear)
        self.logo.animate_color(color.white, duration=1, delay=.0)
        self.logo.fade_out(.5, delay=5, curve=curve.linear)
        camera.overlay.animate_color(color.clear, duration=1, delay=5)
        destroy(self.logo, delay=5)


class HomeScreen(Entity):
    def __init__(self):
        super().__init__()
        self.bg = Entity(parent=scene, model='quad', texture='bg',
                         scale=(24, 16), z=10, color=color.light_gray)

        self.parent = camera.ui
        self.scale = .8
        # self.menu_parent = Entity(parent=camera.ui)
        self.bg = Panel(parent=self)
        self.text = Text(world_parent=self,
                         text="Select a mode", scale=3, origin=(0, 0), y=0.3)

        self.but1 = Button(text='Classic 3v3', parent=self,
                           position=(0, 0.10), scale=(0.60, 0.12), color=color.orange, highlight_color=color.azure, pressed_color=color.azure)
        self.but2 = Button(text='Advanced', parent=self,
                           position=(0, -0.10), scale=(0.60, 0.12), color=color.orange, highlight_color=color.azure, pressed_color=color.azure)
        Text(world_parent=self, text="Would you like to play first?",
             x=-.07, y=-.27, origin=(0, 0))
        self.playFirst = ButtonGroup(
            ('Yes', 'No'), default='Yes', parent=self,  origin=(0, 0), x=.15, y=-.245, max_selection=1, min_selection=1)

        self.text = Text(world_parent=self,
                         text="© b30wulffz", scale=.8, origin=(0, 0), y=-0.38)
        self.enabled = False

    def trigger(self):
        self.enabled = not self.enabled

    # def launchMainGame(self):
    #     self.trigger()
    #     MainGame(3)


class MainGame(Entity):
    def __init__(self, board, algo, lim):
        super().__init__()

        print("hello")
        ### For Backend ###
        self.board = board
        self.dim = board.dim
        self.algo = algo
        self.lim = lim

        ### For Frontend ###
        self.parent = camera.ui
        # center = Entity(model='quad', scale=.1, color=color.red)
        # p = Entity()
        # for i in range(4*5):
        #     b = Button(parent=p, model='quad', scale=.5, scale_x=1, text=str(i), color=color.tint(color.random_color(),-.6))
        #     b.text_entity.world_scale = 1
        # t = time.time()
        # grid_layout(p.children, max_x=7, max_y=10, origin=(0, .5))
        # center = Entity(parent=camera.ui, model=Circle(), scale=.005, color=color.lime)
        # EditorCamera()
        # print(time.time() - t)
        # self.scale = 0.4/(dim-1)
        # self.position
        # self.position = (-0.22, -0.25)
        # Button(parent=self, position=(1, 1))
        # self.bg = Panel(parent=self)
        Panel(parent=self,
              #  world_parent=camera.ui,
              y=0.4, model='quad', scale=(0.8, 0.13), color=color.azure)
        self.text = Text('Your Turn!', parent=self,
                         # world_parent=camera.ui,
                         origin=(0, 0), world_scale=1, scale=3, y=0.4)
        # center = Entity(model='quad', scale=.1, color=color.red)
        self.p = Entity(parent=self, scale=0.5/(self.dim))
        self.but_list = []
        for x in range(0, self.dim):
            for y in range(0, self.dim):
                self.but_list.append(
                    Button(parent=self.p,  scale=1))
        shift = self.dim/2
        print(shift)
        grid_layout(self.p.children, max_x=self.dim,
                    max_y=self.dim, offset=(-shift, shift))

        def go_back():
            button_click_audio.play()
            game_audio.stop()
            winner_audio.stop()
            game_draw_audio.stop()
            intro_audio.play()
            print("hiii")
            game_screen.trigger()
            home_screen.trigger()
            destroy(game_screen)

        def reset():
            button_click_audio.play()
            winner_audio.stop()
            game_draw_audio.stop()
            game_audio.play()

            for but in self.but_list:
                but.text = ""
                but.color = Button.color
                but.disabled = False
                but.collision = True

            self.board.state = [
                ['' for x in range(0, self.dim)] for y in range(0, self.dim)]
            if home_screen.playFirst.value[0] == 'No':
                game_screen.text.text = "Computer's Turn"
                invoke(rand_start, delay=1)
            else:
                game_screen.text.text = 'Your Turn!'

        self.but1 = Button(text='Restart', parent=self, position=(
            -0.2, -0.39), scale=(0.30, 0.1), color=color.orange, on_click=reset)
        self.but2 = Button(text='End Game', parent=self, position=(
            0.2,  -0.39), scale=(0.30, 0.1), color=color.orange, on_click=go_back)
        # center = Entity(parent=camera.ui, model=Circle(),
        #                 scale=.005, color=color.lime)
        print("Hi")

    def trigger(self):
        self.enabled = not self.enabled


class Option(Entity):
    def __init__(self):
        super().__init__()

        self.parent = camera.ui
        # self.scale = .8

        self.board = Slider(2, 9, default=3, x=-.16, y=.3,
                            text='Board Size', dynamic=True, step=1, parent=self)
        self.cutoff = Slider(2, 9, default=3,  x=-.16, y=.2,
                             text='Cutoff', dynamic=True, step=1, parent=self)
        Text("Choose Algorithm", parent=self, y=.1, origin=(0, 0))
        self.algo = ButtonGroup(
            ('Basic Minimax', 'Alpha Beta Pruning', 'Depth Limited', 'Pruning with Depth Limit', 'Experimental'), default='Alpha Beta Pruning', parent=self,  origin=(0, 0), x=-.78, y=.05, max_selection=1, min_selection=1)

        # Text("Depth", x=-.22, y=-.1, origin=(0, 0))
        # input_field = InputField(default_value='4', x=.08, y=-.1)

        self.depth = Slider(1, 20, default=5,  x=-.16, y=-.1,
                            text='Depth(optional)', dynamic=True, step=1, parent=self)

        def go_back():
            button_click_audio.play()
            game_audio.stop()
            intro_audio.play()
            advance_screen.trigger()
            home_screen.trigger()
            destroy(advance_screen)

        self.but1 = Button(text='Go back', parent=self, position=(
            -0.2, -0.3), scale=(0.30, 0.1), color=color.orange, on_click=go_back)
        self.but2 = Button(text='Start', parent=self, position=(
            0.2,  -0.3), scale=(0.30, 0.1), color=color.orange, on_click=launch_advance_game)

    def trigger(self):
        self.enabled = not self.enabled


# play_first = ['Yes']


def rand_start():
    x = choice(range(0, game_screen.dim))
    y = choice(range(0, game_screen.dim))
    game_screen.board.state[x][y] = 'O'
    game_screen.board.PrintBoard(game_screen.board.state)
    index = (x*game_screen.dim) + y
    but = game_screen.but_list[index]

    but.text = "O"
    but.color = color.rgb(255, 138, 91)
    but.disabled = True
    but.collision = False
    computer_play_audio.play()
    if not game_screen.board.CheckWinner(game_screen.board):
        game_screen.text.text = 'Your Turn!'


def launch_advance_options():
    # play_first = home_screen.playFirst.value

    button_click_audio.play()
    global advance_screen
    home_screen.trigger()
    advance_screen = Option()


def launch_classic_game():
    # play_first = home_screen.playFirst.value

    button_click_audio.play()
    intro_audio.stop()
    game_audio.play()

    global game_screen, user_play
    home_screen.trigger()

    board = Problem(3, 3)

    user_play = True
    game_screen = MainGame(board, ['Basic Minimax'], 0)
    # print(play_first[0])
    if home_screen.playFirst.value[0] == 'No':
        game_screen.text.text = "Computer's Turn"
        invoke(rand_start, delay=1)


def launch_advance_game():
    button_click_audio.play()
    intro_audio.stop()
    game_audio.play()

    global game_screen, user_play
    advance_screen.trigger()

    # print(advance_screen.board.value)
    # print(advance_screen.cutoff.value)
    # print(advance_screen.algo.value)
    # print(advance_screen.depth.value)

    dim = int(advance_screen.board.value)
    cutoff = int(advance_screen.cutoff.value)

    if cutoff > dim:
        dim = cutoff

    board = Problem(dim, cutoff)
    user_play = True
    game_screen = MainGame(
        board, advance_screen.algo.value, int(advance_screen.depth.value))
    destroy(advance_screen)
    # print(play_first[0])
    if home_screen.playFirst.value[0] == 'No':
        game_screen.text.text = "Computer's Turn"
        invoke(rand_start, delay=1)
    # global game_screen
    # home_screen.trigger()
    # game_screen = MainGame(3)


# splash_0 = SplashScreen()
# splash_1 = SplashScreen()
# splash_1.enabled = False
# entity_0 = Text('text0', enabled=False)
# entity_1 = Text('text1', color=color.red, position=(0, .25), enabled=False)
home_screen = HomeScreen()
home_screen.but1.on_click = launch_classic_game
home_screen.but2.on_click = launch_advance_options
# music
intro_audio = Audio('intro_audio', autoplay=False, loop=True)
game_audio = Audio('game_audio', autoplay=False, loop=True)
button_click_audio = Audio('button_click_audio', autoplay=False)
# error_audio = Audio('error_audio', autoplay=False)
user_play_audio = Audio('user_play_audio', autoplay=False)
computer_play_audio = Audio('computer_play_audio', autoplay=False)
winner_audio = Audio('winner_audio', autoplay=False)
game_draw_audio = Audio('game_draw_audio', autoplay=False)

Sequence(
    # Func(SplashScreen),
    # Wait(5),
    # Func(intro_audio.play),
    # Func(SplashScreen, txtr='logo2'),
    # # Func(Audio, 'intro_audio', loop=True),
    # Wait(5),
    Func(home_screen.trigger),
    # Wait(10),
    # Func(home_screen.trigger),
    # Func(setattr, entity_0, 'enabled', True),
    # Wait(5),
    # Func(setattr, entity_0, 'enabled', False),
    # Func(setattr, entity_1, 'enabled', True),
    # Wait(5),
    # Func(setattr, entity_1, 'enabled', False),
    # Func(print, 'finished')


).start()


player_name = "X"
player_color = color.azure


# def update_player():
#     if player_name == "O":
#         player_name = "X"
#         player_color = color.orange
#         print("yes")
#     else:
#         player_name = "O"
#         player_color = color.azure
#         print("no")

mode = "AI"


def input(key):
    if key == 'left mouse down' and mouse.hovered_entity:
        print(user_play)
        but = mouse.hovered_entity

        if str(but) == "ui_render/ui_camera/ui/game_screen/p/button" or str(but) == "ui_render/ui_camera/ui/main_game/p/button":
            # if mouse.enabled == True:
            but.text = "X"
            but.color = color.rgb(95, 168, 211)
            but.disabled = True
            but.collision = False

            # print(game_screen.but_list)
            l = game_screen.but_list.index(but)
            x = int(l / game_screen.dim)
            y = l % game_screen.dim
            game_screen.board.state[x][y] = 'X'
            user_play_audio.play()

            if not game_screen.board.CheckWinner(game_screen.board):
                    # mouse.enabled = False
                game_screen.text.text = 'Computer\'s Turn!'

                invoke(AIalgo, game_screen.board,
                       game_screen.algo, game_screen.lim, delay=1)
            # for but1 in game_screen.but_list:
            #     but1.disabled = True
            # user_play = not user_play
            # time.sleep(1)
            # print(game_screen.board.state)

            # if game == True:
            # AIalgo(game_screen.board, game_screen.algo, game_screen.lim)


Cursor(texture='cursor', scale=.1)
mouse.visible = False
app.run()


# ### game ###


# def gameBackend(dim, cutoff, lim=0, algo='Alpha Beta Pruning'):

#     # dim =
#     # cutoff = int(input("Enter Cutoff: "))

#     # lim = 0
#     # algo = int(input("Choose Algorithm: [1] Basic, [2] Alpha-Beta Pruning, [3] Depth Limit, [4] Alpha-Beta Pruning with Depth Limit: "))
#     # 'Basic Minimax', 'Alpha Beta Pruning', 'Depth Limited', 'Pruning with Depth Limit', 'Experimental'
#     if algo == 'Basic Minimax':
#         algo = "basic"
#     elif algo == 'Alpha Beta Pruning':
#         algo = "alphaBeta"
#     elif algo == 'Depth Limited':
#         algo = "depthLim"
#         # lim = lim
#     elif algo == 'Pruning with Depth Limit':
#         algo = "alphaBetaDepthLim"
#         # lim = lim
#     else:
#         algo = "alphaBeta"

#     board = Problem(dim, cutoff)

#     check = 1

#     # check = int(input("Do you want to play first: "))

#     if check == 0:
#         print("\nO turn:")
#         board.state[choice(range(0, dim))][choice(range(0, dim))] = 'O'
#         board.PrintBoard(board.state)

#     while True:
#         print("\nX turn:")
#         try:
#             [x, y] = list(map(int, input().split()))
#         except ValueError:
#             print("Wrong Input")
#             continue

#         try:
#             if board.state[x][y] == '':
#                 board.state[x][y] = 'X'
#                 board.PrintBoard(board.state)

#                 # AI turn
#                 AIalgo(board, algo, lim)
#             else:
#                 print("Already Occupied")
#             if board.CheckWinner(board):
#                 break
#         except IndexError:
#             print("Out of bounds")
