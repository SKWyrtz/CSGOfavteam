import itertools
import tkinter as tk

text_file = open("teams(short).txt",  "r")
lines = text_file.read()
lines = lines.splitlines()
teams_dict = dict.fromkeys(lines, 0)
combinations = list(itertools.combinations(teams_dict, 2))
comparisons_done = 0

combinations_lenght = 0
for i in combinations:
    combinations_lenght += 1
print(f"length of combinations: {combinations_lenght}")

def generate_GUI(root):

    canvas = tk.Canvas(root, width=600, height=300)
    canvas.grid(columnspan=2, rowspan=3)
    

    instructions = tk.Label(root, text="Select your favorite team of the two")
    instructions.grid(columnspan=3, column=0, row=0)

    team1_label =tk.Label(root, text=combinations[0][0])
    team1_label.grid(column=0, row=1)

    team2_label =tk.Label(root, text=combinations[0][1])
    team2_label.grid(column=1, row=1)

    #Team1 Button
    team1_btn_text = tk.StringVar()
    team1_btn_text.set("Team1")
    team1_btn = tk.Button(root, textvariable=team1_btn_text, command=lambda:favorite_selected(1, team1_label, team2_label))
    team1_btn.grid(column=0, row=2)

    #Team2 Button
    team2_btn_text = tk.StringVar()
    team2_btn_text.set("Team2")
    team2_btn = tk.Button(root, textvariable=team2_btn_text, command=lambda:favorite_selected(2, team1_label, team2_label))
    team2_btn.grid(column=1, row=2)

def favorite_selected(team_selected, team_label1, team_label2): 
    global comparisons_done
    if not combinations_lenght == comparisons_done:
        comparisons_done += 1
        print(f"Comparisons done are now: {comparisons_done}")
        team = combinations[comparisons_done][team_selected-1]
        print(f"The team selected is: {team}")
        teams_dict[team] += 1
        print("This team has been selected {teams_dict[team]} times")
        if comparisons_done == combinations_lenght-1:
            next_team1 = combinations[comparisons_done + 1][0]
            next_team2 = combinations[comparisons_done + 1][1]
            team_label1.config(text=next_team1)
            team_label2.config(text=next_team2)
    else:
        print("done")

    
if __name__ == '__main__':
    root = tk.Tk()
    generate_GUI(root)
    root.mainloop()


def main():

    comparisons_done = 0
    for index, element in enumerate(combinations):
        comparisons_done += 1
        print(f"{combinations_lenght - comparisons_done} comparisons left. Next comparison is:")
        print(f"{element[0]} vs {element[1]}")
        while True:
            fav_team = input("Select your favorite team either by '1' or '2'")
            if fav_team == "1":
                teams_dict[element[0]] += 1
                break
            elif fav_team == "2":
                teams_dict[element[1]] += 1
                break
            else:
                print("Please provide a valid input") 
                print(f"{element[0]} vs {element[1]}")
                continue

    sorted_teams = sorted(teams_dict.items(), key=lambda x:x[1], reverse=True)
    for element in sorted_teams:
        print(element)