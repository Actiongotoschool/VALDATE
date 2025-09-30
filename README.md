# VALDATE - VALORANT: Heartlines

A fan-made text-based dating simulation game featuring VALORANT agents! Build relationships with your favorite agents through conversations and shared activities.

![Game Screenshot](https://img.shields.io/badge/Game-Text%20Based-blue) ![Platform](https://img.shields.io/badge/Platform-Cross%20Platform-green) ![Status](https://img.shields.io/badge/Status-Stable%20v3.0-brightgreen)

## 🎮 About The Game

VALORANT: Heartlines is a charming dating simulation where you can spend time with six different VALORANT agents, each with their own unique personalities, preferences, and dialogue. Get to know them through meaningful conversations, compliments, and fun activities!

**Available Agents:**
- **Jett** - Swift and cheeky duelist from South Korea
- **Phoenix** - Fiery and confident duelist from London  
- **Sage** - Calm and wise healer from China
- **Raze** - Explosive and energetic engineer from Brazil
- **Killjoy** - Genius inventor from Germany
- **Neon** - Electrifying speedster from the Philippines

## 📋 Requirements

- Python 3.6 or higher
- Works on Windows, macOS, and Linux
- Terminal/Command Prompt with basic keyboard support

## 🚀 How to Run

1. **Download the game:**
   ```bash
   git clone https://github.com/Actiongotoschool/VALDATE.git
   cd VALDATE
   ```

2. **Run the game:**
   ```bash
   python "Stable VALDATE 3.0 [RELEASE] .py"
   ```
   
   Or on some systems:
   ```bash
   python3 "Stable VALDATE 3.0 [RELEASE] .py"
   ```

3. **Start playing!** Use the arrow keys to navigate menus and Enter to select.

## 🎯 How to Play

### Main Menu Navigation
- Use **↑ ↓ Arrow Keys** to move between options
- Press **Enter** to select an option
- Press **Esc** to go back or cancel

### Game Flow
1. **Start the Game** - Choose "Start Game" from the main menu
2. **Choose an Agent** - Select which agent you'd like to spend time with
3. **Interact** - Choose from four interaction options:
   - **Compliment** - Give them a nice compliment (+1 affection)
   - **Ask something deep** - Have a meaningful conversation (+2 affection)
   - **Invite to activity** - Suggest doing something together (varies)
   - **Say goodbye** - End the interaction

### The Affection System 💕
Your choices affect your affection level with each agent:
- **Compliments:** +1 affection
- **Deep conversations:** +2 affection  
- **Successful activities:** +2 affection
- **Unsuccessful activities:** -1 affection (minimum 0)

### Activity System 🎲
Each agent has different personality types that determine their available activities:

- **Playful** (Jett): Go for a run, Try street food, Play a video game
- **Confident** (Phoenix): Watch a football match, Go shopping, Listen to music
- **Calm** (Sage): Have tea, Visit a garden, Meditate
- **Energetic** (Raze, Neon): Dance, Paint graffiti, Build something fun
- **Intelligent** (Killjoy): Tinker in the lab, Go to a museum, Try a puzzle challenge

**Pro Tip:** Activities that match an agent's interests will be more successful!

### Agent Preferences 📝
Each agent has specific likes that influence activity success:

| Agent | Personality | Likes |
|-------|-------------|-------|
| Jett | Playful | Adventure, Food, Competition |
| Phoenix | Confident | Music, Showing off, Banter |
| Sage | Calm | Peace, Helping, Tea |
| Raze | Energetic | Art, Fun, Music |
| Killjoy | Intelligent | Science, Gadgets, Coffee |
| Neon | Energetic | Running, Music, Competition |

### Endings 🎬
Your final affection level determines the ending:
- **5+ Affection:** Enthusiastic - "I had a great time. Let's do this again soon!"
- **2-4 Affection:** Friendly - "That was fun. See you around."
- **0-1 Affection:** Polite - "Take care."

## 🎯 Tips for Success

1. **Pay attention to personality types** - Match activities to their personality for better results
2. **Learn their interests** - Activities containing keywords from their "likes" will be more successful
3. **Mix your interactions** - Deep conversations give more affection than compliments
4. **Don't worry about mistakes** - Affection can't go below 0, so failed activities won't ruin your progress
5. **Try different approaches** - Each agent has multiple dialogue responses that are randomly selected

## 🎲 Advanced Gameplay

- **Multiple Playthroughs:** Try different interaction styles with the same agent
- **Collect All Endings:** Aim for different affection levels to see all possible endings
- **Character Exploration:** Each agent has unique dialogue that reveals their personality
- **Speed Running:** See how quickly you can achieve maximum affection!

## 🔧 Technical Features

- **Cross-platform compatibility** - Works on Windows, macOS, and Linux
- **Keyboard navigation** - Intuitive arrow key controls
- **Graceful fallbacks** - Works even without ANSI color support
- **Clean interruption handling** - Ctrl+C exits gracefully

## ⚖️ Legal Notice

This is a fan project and is not affiliated with Riot Games. All VALORANT characters and settings are the property of Riot Games. This project is for educational and entertainment purposes only.

## 🤝 Contributing

This is primarily a learning project, but feel free to:
- Report bugs or issues
- Suggest new features
- Add more agents (modify the `agents` dictionary)
- Add new activities (modify the `activities` dictionary)

## 📄 Credits

- **Developer:** Keaton Leung (Ketomine)
- **Inspiration:** VALORANT by Riot Games
- **Special Thanks:** Computer Science teachers and the Stack Overflow community

---

**Enjoy building relationships with your favorite VALORANT agents!** 💕

*THIS DESCRIPTION AND MOST OF THE DOCUMENTATIOJ IS AI GENERATED. NONE OF THE CODE IS*