import streamlit as st

def main():
    st.title('리뷰 긍정 부정 예측 맵')

    menu = ['Home','EDA',"ML"]

    choice = st.sidebar.selectbox('메뉴 선택',menu)

    if choice == menu[0]:
        pass
    elif choice == menu[1]:
        pass
    elif choice == menu[2]:
        pass


if __name__ == '__main__':
    main()