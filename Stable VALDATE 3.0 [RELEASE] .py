import sys
import os
import time
import random

# ============== ANSI checker / helper ==============
def enable_ansi_on_windows():
    #Try to enable ANSI processing on Windows. Returns True if ANSI probably will work, False otherwise.
    # SOME OF THIS IS FROM https://stackoverflow.com/a/36760881 because windows is annoying and im not THAT good
    if os.name != "nt":
        return True
    try:
        import ctypes
        from ctypes import wintypes
        kernel32 = ctypes.windll.kernel32
        STD_OUTPUT_HANDLE = -11
        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004

        hOut = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        if hOut == 0 or hOut == -1:
            return False
        mode = wintypes.DWORD()
        if kernel32.GetConsoleMode(hOut, ctypes.byref(mode)) == 0:
            return False
        new_mode = mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING
        if kernel32.SetConsoleMode(hOut, new_mode) == 0:
            return False
        return True
    except Exception:
        # best effort fallback
        try:
            os.system("")  # in case of older system
            return True
        except Exception:
            return False

ANSI_OK = enable_ansi_on_windows()

# ANSI keys (backup empty if ANSI not supported)
BOLD = "\033[1m" if ANSI_OK else ""
RESET = "\033[0m" if ANSI_OK else ""
YELLOW = "\033[33m" if ANSI_OK else ""
CYAN = "\033[36m" if ANSI_OK else ""

# ============== Cross-platform key reader ==============
if os.name == "nt":
    #normal windows environment
    import msvcrt

    def get_key():
        #Return 'UP','DOWN','LEFT','RIGHT','ENTER','ESC' or None (Windows).
        while True:
            ch = msvcrt.getch()
            if ch in (b'\x00', b'\xe0'):  # special (arrows, f-keys)
                ch2 = msvcrt.getch()
                return {b'H': 'UP', b'P': 'DOWN', b'K': 'LEFT', b'M': 'RIGHT'}.get(ch2)
            if ch == b'\r':
                return 'ENTER'
            if ch == b'\x1b':
                return 'ESC'
            # ignore other keys and continue loop
            return None
else:
    # Unix-like system (POSIX terminal) just in case anyone doesnt run on windows
    # adapted from https://stackoverflow.com/a/22085679 as well as https://stackoverflow.com/a/510364 because im not THAT good
    import tty
    import termios

    def get_key():
        #Return 'UP','DOWN','LEFT','RIGHT','ENTER','ESC' or None (Unix).
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch1 = sys.stdin.read(1)
            if ch1 == '\x1b':  # escape sequence
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    return {'A': 'UP', 'B': 'DOWN', 'C': 'RIGHT', 'D': 'LEFT'}.get(ch3)
                else:
                    return 'ESC'
            if ch1 in ('\r', '\n'):
                return 'ENTER'
            return None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

# ============== UI helpers ==============
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.02):
    # Print text with per-character delay . +newline error fix.
    
    if not text:
        print()
        return
    for c in text:
        print(c, end='', flush=True)
        if delay and c != '\n':
            time.sleep(delay)
    # backup single newline at end unless the text already ended with newline
    if not text.endswith('\n'):
        print()

def pause():
#Cross-platform pause that waits for ENTER (clean ikk)
    try:
        input("\n[Press ENTER to continue]")
    except (EOFError, KeyboardInterrupt):
        # If input isn't available, just go to returning
        print()
        return

def run_menu(options, title="Menu"):
    #Display an arrow-key navigable menu and return the selected option string. Returns None if the user cancels (ESC).
    
    if not options:
        return None
    selected = 0
    while True:
        clear_screen()
        print(f"=== {title} ===\n")
        for i, option in enumerate(options):
            prefix = f"{BOLD}{YELLOW}> {RESET}" if i == selected else "  "
            text = f"{BOLD}{option}{RESET}" if i == selected else option
            print(f"{prefix}{text}")
        print("\nUse ↑ ↓ to move, Enter to select, Esc to cancel.")
        key = get_key()
        if key == 'UP':
            selected = (selected - 1) % len(options)
        elif key == 'DOWN':
            selected = (selected + 1) % len(options)
        elif key == 'ENTER':
            return options[selected]
        elif key == 'ESC':
            return None

# ============== Game data ==============
agents = {
    "Jett": {
        "desc": "A swift and cheeky duelist from South Korea, always ready with a witty comeback.",
        "personality": "playful",
        "likes": ["adventure", "food", "competition"],
        "responses": {
            "greet": ["Yo! You look like you could use some excitement.", "Hey! Ready to do something fun?"],
            "compliment": ["Haha, thanks! I know I look good.", "You trying to flatter me? Not bad!"],
            "deep": ["Sometimes I wonder if I'm moving too fast for my own good.", "I miss home, but I love the thrill of the chase."]
        }
    },
    "Phoenix": {
        "desc": "A fiery duelist from London, confident and always up for a challenge.",
        "personality": "confident",
        "likes": ["music", "showing off", "banter"],
        "responses": {
            "greet": ["Oi, what's up? Ready to see some real moves?", "Hey, you look like you could use some fire in your life."],
            "compliment": ["Of course I look good. But thanks, yeah?", "You got good taste, I'll give you that."],
            "deep": ["Sometimes I wonder if I'm more than just the show-off.", "I act tough, but I care about my mates, you know?"]
        }
    },
    "Sage": {
        "desc": "A calm and wise healer from China, always composed and caring.",
        "personality": "calm",
        "likes": ["peace", "helping", "tea"],
        "responses": {
            "greet": ["Greetings. How are you feeling today?", "Hello. It's good to see you."],
            "compliment": ["Thank you. Your kindness is appreciated.", "You are very thoughtful."],
            "deep": ["I carry many burdens, but I find strength in helping others.", "Balance is important, even in chaos."]
        }
    },
    "Raze": {
        "desc": "An explosive engineer from Brazil, energetic and always ready to make things go boom.",
        "personality": "energetic",
        "likes": ["art", "fun", "music"],
        "responses": {
            "greet": ["Yo! Ready to blow stuff up? Figuratively, of course!", "Hey hey! Let's make some noise!"],
            "compliment": ["Haha, you got good taste! I like you already.", "Aww, thanks! You're not so bad yourself."],
            "deep": ["Sometimes I wonder if people only see the explosions, not the art.", "I just want to make people smile, you know?"]
        }
    },
    "Killjoy": {
        "desc": "A genius inventor from Germany, analytical but secretly caring.",
        "personality": "intelligent",
        "likes": ["science", "gadgets", "coffee"],
        "responses": {
            "greet": ["Hey! Did you want to see what I’m working on?", "You’re just in time for an experiment!"],
            "compliment": ["Oh? Well... thank you. That’s sweet.", "You have a good eye for engineering talent."],
            "deep": ["Sometimes I wish I could switch off my brain for a bit.", "I create because I want to make life better for others."]
        }
    },
    "Neon": {
        "desc": "An electrifying agent from the Philippines, fast, blunt, and full of energy.",
        "personality": "energetic",
        "likes": ["running", "music", "competition"],
        "responses": {
            "greet": ["Hey! Try to keep up, yeah?", "Yo! You’re quick on your feet? Let’s race!"],
            "compliment": ["Heh, thanks! You’re not so bad yourself!", "Aww, stop it! You’re making me blush."],
            "deep": ["Sometimes, I wish I could slow down... just a little.", "I miss my family, but I know I’m doing something good here."]
        }
    }
}

activities = {
    "playful": ["Go for a run", "Try street food", "Play a video game"],
    "confident": ["Watch a football match", "Go shopping", "Listen to music"],
    "calm": ["Have tea", "Visit a garden", "Meditate"],
    "energetic": ["Dance", "Paint graffiti", "Build something fun"],
    "intelligent": ["Tinker in the lab", "Go to a museum", "Try a puzzle challenge"]
}

# ============== Game logic ==============
def choose_agent():
    #Return selected agent name or None if user cancels/back.
    options = [f"{name} - {data['desc']}" for name, data in agents.items()]
    options.append("[Back]")
    selection = run_menu(options, "Choose an agent to spend time with")
    if selection is None or selection == "[Back]":
        return None
    # selection like "Jett - desc"
    return selection.split(" - ", 1)[0]

def invite_activity(agent):
    # Return True if liked, False if disliked, dont punish for cancels
    personality = agent.get("personality", "")
    options = activities.get(personality, [])
    if not options:
        slow_print("They don't have activities listed.")
        pause()
        return None
    options = options.copy()
    options.append("[Back]")
    selection = run_menu(options, "Invite them to:")
    if selection is None or selection == "[Back]":
        return None
    act = selection.lower()
    # check for keywords in likes
    liked = False
    for like in agent.get("likes", []):
        if like.lower() in act:
            liked = True
            break
    if liked:
        slow_print(f"{selection}? They light up with excitement!")
        pause()
        return True
    else:
        slow_print(f"{selection}? They seem unsure, but they'll join you anyway.")
        pause()
        return False

def use_menu():
    options = ["Compliment", "Ask something deep", "Invite to activity", "Say goodbye"]
    return run_menu(options, "What do you want to do?")

def interact(agent_name):
    # Main interaction loop for AFFECTION BUILDING
    agent = agents[agent_name]
    affection = 0
    clear_screen()
    slow_print(random.choice(agent["responses"]["greet"]))
    pause()
    while True:
        action = use_menu()
        if action is None or action == "Say goodbye":
            break
        if action == "Compliment":
            slow_print(random.choice(agent["responses"]["compliment"]))
            affection += 1
        elif action == "Ask something deep":
            slow_print(random.choice(agent["responses"]["deep"]))
            affection += 2
        elif action == "Invite to activity":
            result = invite_activity(agent)
            if result is True:
                affection += 2
            elif result is False:
                affection = max(0, affection - 1)
            # if result is None ignore for now
        # Alr cap minimum affection to 0 (to help noobbsss)
        affection = max(0, affection)
        pause()
    return affection

def ending(agent_name, affection):
    affection = max(0, affection)
    agent = agents[agent_name]
    clear_screen()
    slow_print("\nYour time together comes to an end...")
    if affection >= 5:
        slow_print(f"{agent_name} smiles warmly at you.")
        slow_print(f"\"I had a great time. Let's do this again soon!\"")
    elif affection >= 2:
        slow_print(f"{agent_name} nods. \"That was fun. See you around.\"")
    else:
        slow_print(f"{agent_name} gives a polite nod. \"Take care.\"")
    pause()

# ============== Title  ==============
def title_screen():
    #Return True if user chooses wants to play, False to leave :(
    while True:
        selection = run_menu(["Start Game", "Credits", "Exit"], "VALORANT: Heartlines")
        if selection == "Start Game":
            return True
        elif selection == "Credits":
            clear_screen()
            slow_print("VALORANT: Heartlines\n", 0.02)
            slow_print("Literally all coded by: ")
            print(f"{CYAN}Keaton Leung - Ketomine{RESET}\n")
            slow_print("A fan project. Not affiliated with Riot Games.")
            print("seriously don't sue me riot please")
            pause()
        elif selection == "Exit" or selection is None:
            clear_screen()
            slow_print("Goodbye, Agent.")
            return False

def main():
    # recursion fix
    while True:
        start = title_screen()
        if not start:
            break
        slow_print("Welcome to VALORANT: Heartlines\n", 0.02)
        # game session loop
        while True:
            agent_name = choose_agent()
            if agent_name is None:
                # back to title screen
                break
            affection = interact(agent_name)
            ending(agent_name, affection)
            again = run_menu(["Choose another agent", "Return to title", "Exit"], "What next?")
            if again == "Choose another agent":
                continue
            elif again == "Return to title" or again is None:
                # break to title screen
                break
            else:  # Exit
                slow_print("\nThanks for playing!")
                return
        # returns to title screen
    slow_print("\nThanks for playing!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("\nInterrupted. Goodbye!")

'''Alr so as most can tell im a VALORANT addict. So I started making a dating sim with the agents, mostly to practice python.

This is a stable version of VALDATE 3.0, which has a title screen, a main menu, and a few agents to choose from. The game is still in development but this is a stable build.
To add more agents, just add to the 'agents' dictionary. To add more activities, just add to the 'activities' dictionary.

The menu system is cross-platform and should work on Windows, Linux, and MacOS. It uses ANSI escape codes for styling, but falls back gracefully if not supported.

semi-legal related DISCLAIMER: This is a fan project and is not affiliated with Riot Games. All characters and settings are the property of Riot Games. (blah blah blah JKJK please dont sue me riot I love your game)

other DISCLAIMER: Some of the code for the menu system is adapted from various sources on StackOverflow, as noted in the comments, I had a few bugs i asked others for help solving.
    No code was directly copied, all code is written by me, but some logic and ideas are adapted from others.
    and NO AI WAS USED TO WRITE THIS CODE. I REPEAT NO AI WAS USED TO WRITE THIS CODE. lets gooooo

Shoutout to: Mr Carr and the rest of my past compsci teachers for not just teaching me the skills but developing my passion for coding.

Alr I've probably missed something but its like 3am so im going to bed. Enjoy the code! - Ketomine'''