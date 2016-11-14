import game

def main():

    vlad = game.Game("evan")
    # print(vlad.loadGame())
    save = {"speed":1,"strength":1,"r_rate":2}
    vlad.saveGame(save)
    print("done")
    print(vlad.loadGame())

main()
