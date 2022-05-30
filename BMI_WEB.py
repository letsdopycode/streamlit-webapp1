#body mass index calculation app
import streamlit as sm

#set title
primaryColor = "#F63366"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
sm.title("welcome to BMI calculator")

#take i/p for weight and heigth in kgs,meters respectively
weigth = sm.number_input("Enter your weight(in kgs)")
#add radio button to select height format()
status = sm.radio("select your height format:", ("cms", "meters", "feet"))
if status == "cms":
    heigth = sm.number_input("centimeters")
    try:
        bmi = weigth/((heigth/100)**2)
    except:
        sm.text("enter height ..")
if status == "meters":
    heigth = sm.number_input("meters")
    try:
        bmi = weigth/(heigth**2)
    except:
        sm.text("enter height ..")
if status == "feet":
    heigth = sm.number_input("feet")
    try:
        bmi = weigth/((heigth/3.28)**2)
    except:
        sm.text("enter height ..")

#create bmi cslculste button
if sm.button("calculate bmi"):
    #print bmi Index
    sm.text("your bmi is: {}".format(bmi))

    if bmi < 16:
        sm.error("you are extremely underweigth")

    if bmi >= 16 and bmi < 18.5:
        sm.warning("you are  underweigth")

    if bmi >= 18.5 and bmi < 25:
        sm.success("healthy")

    if bmi >= 25 and bmi < 30:
        sm.warning("overweigthed")

    if bmi >= 30:
        sm.error("extremely overweigthed")
