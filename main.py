import streamlit as st

# header
st.title("🎯 Linux Riddle Challenge!")
st.markdown("Can you solve these simple Linux riddles? Join the **Linux User's Group** if you do!")

# questions
riddles = [
    {"riddle": "I list all the files in a directory, what command am I?", "answer": "ls", "hint": "It's a two-letter command."},
    {"riddle": "I change the current directory, what command am I?", "answer": "cd", "hint": "This command stands for 'Change Directory'."},
    {"riddle": "I display the current working directory, what command am I?", "answer": "pwd", "hint": "This command shows where you are."},
    {"riddle": "I clear the terminal screen, what command am I?", "answer": "clear", "hint": "Type what you want to do to your cluttered screen."},
    {"riddle": "I show the manual for a command, what command am I?", "answer": "man", "hint": "This command gives you a MANual!"}
]

# progress 
if "current_riddle" not in st.session_state:
    st.session_state.current_riddle = 0
    st.session_state.solved = False
    st.session_state.show_hint = False
    st.session_state.points = 0
    st.session_state.hint_taken = False
    st.session_state.wrong_attempts = 0
    st.session_state.user_input = ""  

# checking answer 
def check_answer(user_answer, correct_answer):
    if user_answer.lower().strip() == correct_answer:
        st.session_state.solved = True
        st.session_state.show_hint = False
        st.session_state.hint_taken = False
        st.success("✅ Correct! You earned 10 points.")
        st.session_state.points += 10
    else:
        st.session_state.wrong_attempts += 1
        st.session_state.points -= 1
        st.error(f"❌ Oops! That's not the right answer. You lost 1 point. Attempts: {st.session_state.wrong_attempts}")

# showing the riddle
current_riddle = riddles[st.session_state.current_riddle]
st.write(f"### Riddle {st.session_state.current_riddle + 1}: {current_riddle['riddle']}")

# I/P box
user_input = st.text_input("Your answer:", key=f"input_{st.session_state.current_riddle}", value=st.session_state.user_input)

# hint: with point dedcution 
if st.session_state.hint_taken:
    st.warning(f"💡 Hint: {current_riddle['hint']} (Hint taken: -2 points)")

if not st.session_state.hint_taken and st.button("Get Hint"):
    st.session_state.show_hint = True
    st.session_state.hint_taken = True
    st.session_state.points -= 2
    st.warning(f"💡 Hint: {current_riddle['hint']} (You lost 2 points for taking the hint!)")

# checking answer here
if st.button("Submit"):
    check_answer(user_input, current_riddle["answer"])
    st.session_state.user_input = ""  

# moving to next riddle
if st.session_state.solved:
    if st.session_state.current_riddle < len(riddles) - 1:
        if st.button("Next Riddle"):
            st.session_state.current_riddle += 1
            st.session_state.solved = False
            st.session_state.show_hint = False
            st.session_state.wrong_attempts = 0
            st.session_state.user_input = ""  #empty text box for new riddle
    else:
        st.balloons()
        st.success("🎉 Congratulations! You've solved all the riddles.**Congrats**!")
        st.markdown(f"Your final score: {st.session_state.points} points")
        st.markdown("🔗 [Join the Club](https://www.instagram.com/bitslugofficial?igsh=MWkyMjdobGo4anI0aA==)")

# Display the point system and progress
st.sidebar.title("✨ Game Progress")
st.sidebar.markdown(f"Riddle {st.session_state.current_riddle + 1} of {len(riddles)}")
st.sidebar.markdown(f"💰 **Points**: {st.session_state.points}")
st.sidebar.progress((st.session_state.current_riddle + 1) / len(riddles))
