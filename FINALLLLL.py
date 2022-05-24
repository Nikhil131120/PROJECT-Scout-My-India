import tkinter
from tkinter import *
from PIL import Image,ImageTk
def time():
    from time import strftime
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
def date():
    from datetime import datetime
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    date_time = datetime.fromtimestamp(timestamp)
    d = date_time.strftime("%d %B, %Y")
    lbl2.config(text=d.upper())
def func():
    global root
    root.destroy()
    def func():
        global root
        root.destroy()
        def func():
            pass
        root = Tk()
        root.title("SCOUT MY INDIA")
        root.geometry("1350x800")
        root.minsize(1350, 800)
        # root.iconbitmap("q.ico.ico")
        root.wm_attributes("-transparentcolor", 'grey')
        img = Image.open("govern.jpg")
        img = img.resize((1370, 700))
        photo = ImageTk.PhotoImage(img)
        canvas = Canvas(root, width=1400, height=700)
        canvas.create_image(0, 0, image=photo, anchor="nw")
        canvas.pack()
        lbl2 = Label(root, text="SEARCH  SCHOOLS  BY", font=('calibri', 25, 'bold'), foreground='red')
        lbl2.place(x=550, y=40)
        lbl2 = Label(root, text="STATE", font=('calibri', 25, 'bold'), foreground='black')
        lbl2.place(x=350, y=140)
        lbl2 = Label(root, text="DISTRICT", font=('calibri', 25, 'bold'), foreground='black')
        lbl2.place(x=340, y=240)
        lbl2 = Label(root, text="BLOCK", font=('calibri', 25, 'bold'), foreground='black')
        lbl2.place(x=350, y=340)
        Button(root, text="SEARCH", command=func, font="comicsansms 20 bold", bg="red").place(x=590, y=460)
        svar = StringVar()
        pvar = StringVar()
        scidvar = StringVar()
        a = Entry(root, textvariable=svar, font="courier 20 bold", selectborderwidth=4)
        a.place(x=700, y=145)
        a.focus_force()
        b = Entry(root, textvariable=pvar, font="courier 20 bold")
        b.place(x=700, y=250)
        c = Entry(root, textvariable=scidvar, font="courier 20 bold")
        c.place(x=700, y=345)
        root.mainloop()
    def func2():
        global root
        root.destroy()
        def func3():
            global root
            root.destroy()
            def func4():
                global root
                root.destroy()
                # def func77():
                #     global root
                #     root.destroy()
                #     def func09():
                #         global root
                #         import tkinter.messagebox as tksmg
                #         tksmg.showinfo("CONFIRMATION","DETAILS HAVE BEEN SAVED")
                #         root.destroy()
                #     root = Tk()
                #     root.title("Scout my india")
                #     root.geometry("1350x800")
                #     root.minsize(1350, 800)
                #     root.iconbitmap("q.ico.ico")
                #     img = Image.open("j.jpg")
                #     img = img.resize((1570, 800))
                #     photo = ImageTk.PhotoImage(img)
                #     canvas = Canvas(root, width=1400, height=800)
                #     canvas.create_image(0, 0, image=photo, anchor="nw")
                #     canvas.pack()
                #     Button(root, text="<<BACK", command=func, font="comicsansms 10 bold").place(x=5, y=650)
                #     Button(root, text="SAVE", command=func09, font="default 15 bold").place(x=600, y=650)
                #     Label(root, text="SCHOOL DETAIL FORM", font="default 25 bold", fg="red").place(x=510, y=33)


                root = Tk()
                root.title("SCOUT MY INDIA")
                root.geometry("1350x800")
                root.minsize(400, 220)
                # root.iconbitmap("q.ico.ico")
                root.wm_attributes("-transparentcolor", 'blue')
                im = Image.open("bg22.jpg")
                im = im.resize((1370, 800))
                phot = ImageTk.PhotoImage(im)
                canvas = Canvas(root, width=1400, height=700)
                canvas.create_image(0, 0, image=phot, anchor="nw")
                canvas.pack()
                img = Image.open("CT1.jpg")
                img = img.resize((350, 200))
                photo = ImageTk.PhotoImage(img)
                label1 = tkinter.Label(image=photo)
                label1.image = photo
                label1.place(x=30, y=140)

                img1 = Image.open("ud11.jpg")
                img1 = img1.resize((350, 200))
                photo1 = ImageTk.PhotoImage(img1)
                label2 = tkinter.Label(image=photo1)
                label2.image = photo1
                label2.place(x=30, y=440)

                img2 = Image.open("JGT1.jpg")
                img2 = img2.resize((350, 200))
                photo2 = ImageTk.PhotoImage(img2)
                label3 = tkinter.Label(image=photo2)
                label3.image = photo2
                label3.place(x=670, y=150)

                img3 = Image.open("FT1.jpg")
                img3 = img3.resize((350, 200))
                photo3 = ImageTk.PhotoImage(img3)
                label4 = tkinter.Label(image=photo3)
                label4.image = photo2
                label4.place(x=670, y=450)

                lbl1 = Label(root, text="  PLACES TO VISIT  ", font=('calibri', 40, 'bold'), foreground='white',background="black")
                lbl1.place(x=500, y=20)
                lbl2 = Label(root, text="  CITY PALACE  ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl2.place(x=30, y=130)
                lbl21 = Label(root,text="City Palace is Rajasthan's largest palace \n built  along  the banks of Lake Pichola. \n The main part of the palace is open as\n City Palace Museum with extravagant  \narchitecture comprising of ornate halls, \nroyal courtyard, central garden and \nZenana  Mahal among others.",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl21.place(x=390, y=160)
                lbl3 = Label(root, text="  LAKE PICHOLA  ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl3.place(x=30, y=430)
                lbl31 = Label(root,text="The oldest and one of the largest lakes of\n Udaipur, Lake Pichola is enveloped by lofty\n palaces, temples, and bathing ghats.\n Boating in Lake Pichola is the most popular\n  thing to do in Udaipur. Boats are \neasily available from Rameshwar Ghat\n if visiting from the City Palace.\n Otherwise, take a boat trip from Lal\n Ghat.",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl31.place(x=390, y=480)
                lbl4 = Label(root, text="  JAGDISH TEMPLE  ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl4.place(x=670, y=130)
                lbl41 = Label(root,text="Jagdish Temple is one of the most famous\n temples in and around Udaipur. It is dedicated \nto Lord Vishnu in the form of Jagannath.\nThe temple is also popular for its striking\n architecture. Jagdish Temple is located\n 150m from City Palace's Badi Pol \nentrance and has a steep flight of steps \nto the top.",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl41.place(x=1030, y=170)
                lbl5 = Label(root, text="  FATEH SAGAR LAKE  ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl5.place(x=670, y=430)
                lbl5 = Label(root,text="Fateh Sagar Lake is an artificial lake named\n after Maharana Fateh Singh of Udaipur and Mewar.\n It is one of the four lakes in Udaipur\n and houses Nehru Island and the Udaipur \nSolar Observatory on its three islands. \nBoating here in the backdrop of Aravali \nis a must-do activity.",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl5.place(x=1030, y=470)
                Button(root, text=" <<BACK ", command=func3, font="comicsansms 10 bold", bg="red", fg="white").place(x=40, y=645)

                root.mainloop()
            def func5():
                global root
                root.destroy()
                root = Tk()
                root.title("SCOUT MY INDIA")
                root.geometry("1350x800")
                root.minsize(400, 220)
                # root.iconbitmap("q.ico.ico")
                root.wm_attributes("-transparentcolor", 'blue')
                im = Image.open("bg21.jpg")
                im = im.resize((1370, 800))
                phot = ImageTk.PhotoImage(im)
                canvas = Canvas(root, width=1400, height=700)
                canvas.create_image(0, 0, image=phot, anchor="nw")
                canvas.pack()
                img = Image.open("DLBA.jpg")
                img = img.resize((350, 200))
                photo = ImageTk.PhotoImage(img)
                label1 = tkinter.Label(image=photo)
                label1.image = photo
                label1.place(x=30, y=140)

                img1 = Image.open("FD1.jpg")
                img1 = img1.resize((350, 200))
                photo1 = ImageTk.PhotoImage(img1)
                label2 = tkinter.Label(image=photo1)
                label2.image = photo1
                label2.place(x=30, y=440)

                img2 = Image.open("AM1.jpeg")
                img2 = img2.resize((350, 200))
                photo2 = ImageTk.PhotoImage(img2)
                label3 = tkinter.Label(image=photo2)
                label3.image = photo2
                label3.place(x=670, y=150)

                img3 = Image.open("JN1.jpg")
                img3 = img3.resize((350, 200))
                photo3 = ImageTk.PhotoImage(img3)
                label4 = tkinter.Label(image=photo3)
                label4.image = photo2
                label4.place(x=670, y=450)

                lbl1 = Label(root, text="   FOOD   ", font=('calibri', 40, 'bold'), foreground='white',background="black")
                lbl1.place(x=500, y=20)
                lbl2 = Label(root, text="  The Oberoi Udaivilas ", font=('calibri', 20, 'bold'), foreground='white', background="black")
                lbl2.place(x=30, y=130)
                lbl21 = Label(root,text=" * Hardasji Ki Magri, Udaipur 313001 India \n * Rajasthani, Indian, Chinese, Thai \n * 12:00 AM - 12:00 PM, 9:00 PM - 12:00 AM \n  * INR 800-1950 For Two",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl21.place(x=390, y=160)
                lbl3 = Label(root, text="  1559 AD ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl3.place(x=30, y=430)
                lbl31 = Label(root,text=" *Lake Pichola Hotel, Outside Chandpole,\n Pichola, Udaipur \n * Rajasthani, North Indian, Continental \n *12:30pm to 3:30pm, 6:30pm to 10:30pm \n (Mon-Sun) \n * ",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl31.place(x=390, y=480)
                lbl4 = Label(root, text="  Ambrai  ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl4.place(x=670, y=130)
                lbl41 = Label(root,text="* Amet Haveli, Outside Chandpole, Naga Nagri, \n Pichola, Udaipur  \n * North Indian, Mughlai, Continental \n *11:30pm to 3:30pm, 6:30pm to 10:30pm \n (Mon-Sun)",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl41.place(x=1030, y=170)
                lbl5 = Label(root, text=" Jagat Niwas Palace Hotel  ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl5.place(x=670, y=430)
                lbl5 = Label(root,text="* 23-25, Lal Ghat, Chandpole, Udaipur \n North Indian, Thai, Italian, Chinese, \n Continental, Mughlai, Desserts, Beverages\n * 7am to 10:30pm (Mon-Sun) .",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl5.place(x=1030, y=480)
                Button(root, text=" <<BACK ", command=func3, font="comicsansms 10 bold", bg="red", fg="white").place(x=40, y=645)

                root.mainloop()
            def func6():
                global root
                root.destroy()
                root = Tk()
                root.title("SCOUT MY INDIA")
                root.geometry("1350x800")
                root.minsize(1350, 780)
                # root.iconbitmap("q.ico.ico")
                root.wm_attributes("-transparentcolor", 'blue')
                im = Image.open("htr1.jpg")
                im = im.resize((1370, 800))
                phot = ImageTk.PhotoImage(im)
                canvas = Canvas(root, width=1400, height=700)
                canvas.create_image(0, 0, image=phot, anchor="nw")
                canvas.pack()
                lbl1 = Label(root, text="  HOW TO REACH !  ", font=('calibri', 40, 'bold'), foreground='white',background="black")
                lbl1.place(x=400, y=30)
                # Button(root,text=" SEARCH ",command=func,bg="white",fg="blue",font="courier 15 bold",activebackground="green",activeforeground="black",relief=RAISED,borderwidth=15).place(x=580,y= 480)
                Button(root, text=" <<BACK ", command=func3, font="comicsansms 15 bold", bg="red", fg="white").place(x=1200, y=645)
                # Button(root,text="STUDENT SERVICES",command=func,font="comicsansms 10 bold",fg="white",bg="red").place(x=1190,y=660)
                lbl2 = Label(root,text="The Maharana Pratap Airport is nearly 24km from the main city. The city is connected by air \n with all major cities of India (3 - 4 daily flights from Delhi & Mumbai). \n There are many trains that stop at the Udaipur Railway Station as well. You can reach Udaipur\n  by road (by bus, cab or car) too.",font=('calibri', 18, 'bold'), foreground='black', background="white")
                lbl2.place(x=30, y=120)
                lbl4 = Label(root, text=" HOW TO REACH UDAIPUR BY ROAD ", font=('calibri', 20, 'bold'),foreground='white', background="black")
                lbl4.place(x=30, y=280)
                lbl41 = Label(root,text="The city lies midway between Delhi and Mumbai, at the intersection of NH 8, Golden \n quadrilateral,  East west Corridor and NH 76. Road travellers can drive  down to the \n city  either from Ahmedabad through NH8 which takes approximately 5  hours or from\n  Jaipur which   is a 6-hour journey via the Golden quadrilateral. \n It's also a 4-hour drive  from Kota through the EW corridor.",font=('calibri', 18, 'bold'), foreground='black', background="white")
                lbl41.place(x=30, y=330)
                lbl3 = Label(root, text="  HOW TO REACH UDAIPUR BY TRAIN  ", font=('calibri', 20, 'bold'),foreground='white', background="black")
                lbl3.place(x=30, y=500)
                lbl31 = Label(root,text="There are two railway stations in Udaipur- Udaipur City railway station and Rana Pratap Nagar\n railway station, both well networked to most of the cities in India like Kolkata,\n  Bangalore, New Delhi, Mumbai, Jaipur, Ajmer, Kota, Agra, etc. Both the stations are\n located within a distance of 3km from the city centre.",font=('calibri', 18, 'bold'), foreground='black', background="white")
                lbl31.place(x=30, y=550)

                root.mainloop()
            def func7():
                global root
                root.destroy()
                root = Tk()
                root.title("SCOUT MY INDIA")
                root.geometry("1350x800")
                root.minsize(400, 220)
                # root.iconbitmap("q.ico.ico")
                root.wm_attributes("-transparentcolor", 'blue')
                im = Image.open("bbbg1.jpg")
                im = im.resize((1370, 800))
                phot = ImageTk.PhotoImage(im)
                canvas = Canvas(root, width=1400, height=700)
                canvas.create_image(0, 0, image=phot, anchor="nw")
                canvas.pack()
                img = Image.open("HT1.jpg")
                img = img.resize((350, 200))
                photo = ImageTk.PhotoImage(img)
                label1 = tkinter.Label(image=photo)
                label1.image = photo
                label1.place(x=30, y=140)

                img1 = Image.open("HT2.jpg")
                img1 = img1.resize((350, 200))
                photo1 = ImageTk.PhotoImage(img1)
                label2 = tkinter.Label(image=photo1)
                label2.image = photo1
                label2.place(x=30, y=440)

                img2 = Image.open("HT3.jpg")
                img2 = img2.resize((350, 200))
                photo2 = ImageTk.PhotoImage(img2)
                label3 = tkinter.Label(image=photo2)
                label3.image = photo2
                label3.place(x=670, y=150)

                img3 = Image.open("HT4.jpg")
                img3 = img3.resize((350, 200))
                photo3 = ImageTk.PhotoImage(img3)
                label4 = tkinter.Label(image=photo3)
                label4.image = photo2
                label4.place(x=670, y=450)

                lbl1 = Label(root, text="   HOTELS   ", font=('calibri', 40, 'bold'), foreground='white',background="black")
                lbl1.place(x=500, y=20)
                lbl2 = Label(root, text="  Taj Fateh Prakash Palace Udaipur", font=('calibri', 20, 'bold'),foreground='white', background="black")
                lbl2.place(x=30, y=130)
                lbl21 = Label(root,text=" * Facilities: Parking , Bar , Wifi ,\n Pool , Food \n * If you are in Udaipur and want a \n luxurious  stay in the royal style, then\n  you should  definitely consider Taj Fateh\n  Prakash Palace. This property, equipped \n with an outdoor  swimming pool, a \n beautiful lake",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl21.place(x=390, y=160)
                lbl3 = Label(root, text="  Taj Aravali Resort & Spa Udaipur ", font=('calibri', 20, 'bold'),foreground='white', background="black")
                lbl3.place(x=30, y=430)
                lbl31 = Label(root, text=" * Facilities: Parking , Bar , Wifi ,\n  Pool , Food  \n * Sprawled over 27 acres at the picturesque\n foothills of Aravalli range, this modern \nresort is conveniently located in the tranquil\n Bhujra Village close to the city centre.\n Guests can enjoy breathtaking  ",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl31.place(x=390, y=480)
                lbl4 = Label(root, text="  Pride Hotel Udaipur ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl4.place(x=670, y=130)
                lbl41 = Label(root, text="* Facilities: Parking , Bar , Wifi , Pool , Food ", font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl41.place(x=1030, y=170)
                lbl5 = Label(root, text=" Chunda Palace   ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl5.place(x=670, y=430)
                lbl5 = Label(root,text="* Facilities: Parking , Bar , Wifi , Pool , Food \n * Offering spectacular views of City Palace and\n  Lake Pichola, this stately hotel showcases\n Rajasthani heritage with hand-painted décor.\n They have well-equipped suites with marble\n flooring and awe) .",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl5.place(x=1030, y=480)
                Button(root, text=" <<BACK ", command=func3, font="comicsansms 15 bold", bg="red", fg="white").place(x=10, y=645)

                root.mainloop()




            def func8():
                global root
                root.destroy()
                root = Tk()
                root.title("SCOUT MY INDIA")
                root.geometry("1350x800")
                root.minsize(400, 220)
                # root.iconbitmap("q.ico.ico")
                root.wm_attributes("-transparentcolor", 'blue')
                im = Image.open("bg11.jpg")
                im = im.resize((1370, 800))
                phot = ImageTk.PhotoImage(im)
                canvas = Canvas(root, width=1400, height=700)
                canvas.create_image(0, 0, image=phot, anchor="nw")
                canvas.pack()
                img = Image.open("ud11.jpg")
                img = img.resize((350, 200))
                photo = ImageTk.PhotoImage(img)
                label1 = tkinter.Label(image=photo)
                label1.image = photo
                label1.place(x=150, y=180)

                img1 = Image.open("ud2.jpg")
                img1 = img1.resize((350, 200))
                photo1 = ImageTk.PhotoImage(img1)
                label2 = tkinter.Label(image=photo1)
                label2.image = photo1
                label2.place(x=480, y=180)

                img2 = Image.open("ud3.jpg")
                img2 = img2.resize((350, 200))
                photo2 = ImageTk.PhotoImage(img2)
                label3 = tkinter.Label(image=photo2)
                label3.image = photo2
                label3.place(x=830, y=180)

                img3 = Image.open("ud4.jpg")
                img3 = img3.resize((350, 200))
                photo3 = ImageTk.PhotoImage(img3)
                label4 = tkinter.Label(image=photo3)
                label4.image = photo2
                label4.place(x=150, y=450)

                img4 = Image.open("ud5.jpg")
                img4 = img4.resize((350, 200))
                photo4 = ImageTk.PhotoImage(img4)
                label5 = tkinter.Label(image=photo4)
                label5.image = photo4
                label5.place(x=480, y=450)

                img5 = Image.open("ud6.jpg")
                img5 = img5.resize((350, 200))
                photo5 = ImageTk.PhotoImage(img5)
                label6 = tkinter.Label(image=photo5)
                label6.image = photo5
                label6.place(x=830, y=450)

                lbl1 = Label(root, text="  PHOTOS  ", font=('calibri', 40, 'bold'), foreground='white',background="black")
                lbl1.place(x=500, y=30)
                Button(root, text=" <<BACK ", command=func3, font="comicsansms 15 bold", bg="red", fg="white").place(x=20, y=650)

                root.mainloop()



            root = Tk()
            root.title("SCOUT MY INDIA")
            root.geometry("1350x800")
            root.minsize(1350, 780)
            # root.iconbitmap("q.ico.ico")
            root.wm_attributes("-transparentcolor", 'blue')
            img = Image.open("udd1.jpg")
            img = img.resize((1370, 800))
            photo = ImageTk.PhotoImage(img)
            canvas = Canvas(root, width=1400, height=700)
            canvas.create_image(0, 0, image=photo, anchor="nw")
            canvas.pack()
            lbl1 = Label(root, text="  UDAIPUR  ", font=('calibri', 40, 'bold'), foreground='white', background="black")
            lbl1.place(x=500, y=30)
            Button(root, text="PLACES TO VISIT ", command=func4, bg="white", fg="blue", font="courier 20 bold",activebackground="orange", activeforeground="black", relief=RAISED, borderwidth=15).place(x=1000, y=120)

            Button(root, text=" SPECIAL FOOD ", command=func5, bg="white", fg="blue", font="courier 20 bold",activebackground="orange", activeforeground="black", relief=RAISED, borderwidth=15).place(x=1000,y=220)

            Button(root, text="HOW TO REACH ", command=func6, bg="white", fg="blue", font="courier 20 bold",activebackground="orange", activeforeground="black", relief=RAISED, borderwidth=15).place(x=1000,y=320)

            Button(root, text="  HOTELS  ", command=func7, bg="white", fg="blue", font="courier 20 bold",activebackground="orange", activeforeground="black", relief=RAISED, borderwidth=15).place(x=1000,y=420)
            Button(root, text=" PHOTOS ", command=func8, bg="white", fg="blue", font="courier 20 bold",activebackground="orange", activeforeground="black", relief=RAISED, borderwidth=15).place(x=1000,y=520)


            # Button(root,text=" SEARCH ",command=func,bg="white",fg="blue",font="courier 15 bold",activebackground="green",activeforeground="black",relief=RAISED,borderwidth=15).place(x=580,y= 480)
            Button(root, text=" <<BACK ", command=func2, font="comicsansms 15 bold", bg="red", fg="white").place(x=15,y=640)

            # Button(root,text="STUDENT SERVICES",command=func,font="comicsansms 10 bold",fg="white",bg="red").place(x=1190,y=660)
            lbl2 = Label(root,text="Udaipur, also known as the City of Lakes, is one of the most visited \ntourist places in Rajasthan. Located around stunning water lakes and enveloped by the Aravalli Hills in all \n directions, Udaipur is known for its azure lakes, magnificent palaces, vibrant culture and delectable food. \n Along with being a must-visit destination, it is also one of the best places to experience luxury in India. ",font=('calibri', 15, 'bold'), foreground='black', background="white")
            lbl2.place(x=20, y=120)
            lbl3 = Label(root,text=" Boating through the shimmering Lake Pichola is one of the most beautiful \n sights and highlights of every Udaipur trip. Also known as the Venice of the East , Udaipur is inarguably \n one of the most romantic cities in India. Visit its larger than life havelis and monuments, stroll through \n the bustling street markets, ride through one of the seven lakes of the city or relax in one of the extraordinary \n hotels, and you will discover the charm of Udaipur.",font=('calibri', 15, 'bold'), foreground='black', background="white")
            lbl3.place(x=20, y=300)
            lbl4 = Label(root,text="  The city was founded in 1559 by Maharana Udai Singh II as the new capital of \n the Mewar kingdom. The grandeur of the Rajput era is still prevalent in the city's architecture. A trip \n to Udaipur is often combined with a visit to nearby Kumbhalgarh (80km) and Mount Abu. \n The revered Nathdwara temple is about 60 km from Udaipur.",font=('calibri', 15, 'bold'), foreground='black', background="white")
            lbl4.place(x=20, y=500)
            root.mainloop()
        def func9():
            global root
            root.destroy()
            def func10():
                global root
                root.destroy()
                root = Tk()
                root.title("SCOUT MY INDIA")
                root.geometry("1350x800")
                root.minsize(400, 220)
                # root.iconbitmap("q.ico.ico")
                root.wm_attributes("-transparentcolor", 'blue')
                im = Image.open("bg22.jpg")
                im = im.resize((1370, 800))
                phot = ImageTk.PhotoImage(im)
                canvas = Canvas(root, width=1400, height=700)
                canvas.create_image(0, 0, image=phot, anchor="nw")
                canvas.pack()
                img = Image.open("PV1.jpg")
                img = img.resize((350, 200))
                photo = ImageTk.PhotoImage(img)
                label1 = tkinter.Label(image=photo)
                label1.image = photo
                label1.place(x=30, y=140)

                img1 = Image.open("PV5.jpg")
                img1 = img1.resize((350, 200))
                photo1 = ImageTk.PhotoImage(img1)
                label2 = tkinter.Label(image=photo1)
                label2.image = photo1
                label2.place(x=30, y=440)

                img2 = Image.open("PV3.jpg")
                img2 = img2.resize((350, 200))
                photo2 = ImageTk.PhotoImage(img2)
                label3 = tkinter.Label(image=photo2)
                label3.image = photo2
                label3.place(x=670, y=150)

                img3 = Image.open("PV4.jpg")
                img3 = img3.resize((350, 200))
                photo3 = ImageTk.PhotoImage(img3)
                label4 = tkinter.Label(image=photo3)
                label4.image = photo2
                label4.place(x=670, y=450)

                lbl1 = Label(root, text="  PLACES TO VISIT  ", font=('calibri', 40, 'bold'), foreground='white',background="black")
                lbl1.place(x=500, y=20)
                lbl2 = Label(root, text="  CITY PALACE JAIPUR  ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl2.place(x=30, y=130)
                lbl21 = Label(root,text="The City Palace is the main palace from \nwhere the Maharaja Sawai Jai Singh reigned. \nThe palace includes the Chandra Mahan and \nMubarak Mahal along with various other\n buildings within the complex \nIt is located towards the north-eastern\n side of Jaipur. The palace is divided into\n a series of courtyards, buildings and gardens.",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl21.place(x=390, y=160)
                lbl3 = Label(root, text="  HAWA MAHAL  ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl3.place(x=30, y=430)
                lbl31 = Label(root,text="The Hawa Mahal stands at the intersection of \n the main road in Jaipur, Badi Chaupad. It is\n  regarded as the signature building of Jaipur. \nFrom within, the Hawa Mahal palace is based\n  on five floors each of which has a uniquely\n decorated chamber.The top of the palace\n offers a brilliant view of the City\n Palace,Jantar Mantar and the \n ever-busy  Siredeori Bazar.",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl31.place(x=390, y=480)
                lbl4 = Label(root, text=" ALBERT HALL MUSEUM  ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl4.place(x=670, y=130)
                lbl41 = Label(root,text="Situated in the Ram Niwas Garden, Albert\n Hall Museum is one of the oldest museums\n of Rajasthan. It has a rich collection of\n various kinds of items such as paintings, carpets,\n ivory, stone, metal sculptures, colourful crystal\n works etc. The museum looks stunning \nwith yellow lights at night.",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl41.place(x=1030, y=170)
                lbl5 = Label(root, text="  BIRLA TEMPLE  ", font=('calibri', 20, 'bold'), foreground='white', background="black")
                lbl5.place(x=670, y=430)
                lbl5 = Label(root,text="Located on an elevated ground at the base \nof Moti Dungri hill, the Birla Temple of Jaipur\n is dedicated to Lord Vishnu (Narayan), the\npreserver and his consort Lakshmi, the Goddess\n of wealth. It is also known as the Lakshmi \nNarayanan Temple and forms a part of one of the\n several Birla temples located all around \n  the country.",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl5.place(x=1030, y=470)
                Button(root, text=" <<BACK ", command=func9, font="comicsansms 15 bold", bg="red", fg="white").place(x=20, y=650)

                root.mainloop()
            def func11():
                global root
                root.destroy()

                root = Tk()
                root.title("SCOUT MY INDIA")
                root.geometry("1350x800")
                root.minsize(400, 220)
                # root.iconbitmap("q.ico.ico")
                root.wm_attributes("-transparentcolor", 'blue')
                im = Image.open("bg21.jpg")
                im = im.resize((1370, 800))
                phot = ImageTk.PhotoImage(im)
                canvas = Canvas(root, width=1400, height=700)
                canvas.create_image(0, 0, image=phot, anchor="nw")
                canvas.pack()
                img = Image.open("FP1.jpg")
                img = img.resize((350, 200))
                photo = ImageTk.PhotoImage(img)
                label1 = tkinter.Label(image=photo)
                label1.image = photo
                label1.place(x=30, y=140)

                img1 = Image.open("FP2.jpg")
                img1 = img1.resize((350, 200))
                photo1 = ImageTk.PhotoImage(img1)
                label2 = tkinter.Label(image=photo1)
                label2.image = photo1
                label2.place(x=30, y=440)

                img2 = Image.open("FP3.jpg")
                img2 = img2.resize((350, 200))
                photo2 = ImageTk.PhotoImage(img2)
                label3 = tkinter.Label(image=photo2)
                label3.image = photo2
                label3.place(x=670, y=150)

                img3 = Image.open("FP4.jpg")
                img3 = img3.resize((350, 200))
                photo3 = ImageTk.PhotoImage(img3)
                label4 = tkinter.Label(image=photo3)
                label4.image = photo2
                label4.place(x=670, y=450)

                lbl1 = Label(root, text="   FOOD   ", font=('calibri', 40, 'bold'), foreground='white',background="black")
                lbl1.place(x=500, y=20)
                lbl2 = Label(root, text="  Hotel Sweet Dream ", font=('calibri', 20, 'bold'), foreground='white', background="black")
                lbl2.place(x=30, y=130)
                lbl21 = Label(root,text=" * Tucked away in Jaipur, Hotel Sweet\n Dream is a quaint hotel/restaurant with\n a pleasant rooftop terrace, live music\n and friendly atmosphere.\n * 12:00 AM - 12:00 PM, 9:00 PM - 12:00 AM \n  * INR 800-1950 For Two",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl21.place(x=390, y=160)
                lbl3 = Label(root, text="  Rawat Kachori ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl3.place(x=30, y=430)
                lbl31 = Label(root,text=" * Rawat Kachori/Rawat Misthan Bhandar in \nJaipur is a fantastic place to dine. One\n can find lip-smacking kachoris delicious\n sweet and salt lassies, along with some\n authentic Rajasthani Cuisines. The approximate \nprice for two people to eat here\n is INR 600. ", font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl31.place(x=390, y=480)
                lbl4 = Label(root, text="  Jaipur Modern Kitchen  ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl4.place(x=670, y=130)
                lbl41 = Label(root,text="* With the all-day dining facilities, Jaipur\n modern cafe offers a global menu with an\n exciting blend of flavours. Directly teamed up \nwith the local farming communities, to ensure\n the quality and freshness of the produce.", font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl41.place(x=1030, y=170)
                lbl5 = Label(root, text=" Pandit Kulfi  ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl5.place(x=670, y=430)
                lbl5 = Label(root,text="* Nestled in Jaipur, Sri Pandit Kulfi is a \n go-to dessert place opened until midnight.\n In spite of being a small shop, Pandit Kulfi \noffers a variety of delicious desserts.", font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl5.place(x=1030, y=480)
                Button(root, text=" <<BACK ", command=func9, font="comicsansms 15 bold", bg="red", fg="white").place(x=20, y=650)

                root.mainloop()

            def func12():
                global root
                root.destroy()
                root = Tk()
                root.title("SCOUT MY INDIA")
                root.geometry("1350x800")
                root.minsize(1350, 780)
                # root.iconbitmap("q.ico.ico")
                root.wm_attributes("-transparentcolor", 'blue')
                im = Image.open("htr1.jpg")
                im = im.resize((1370, 800))
                phot = ImageTk.PhotoImage(im)
                canvas = Canvas(root, width=1400, height=700)
                canvas.create_image(0, 0, image=phot, anchor="nw")
                canvas.pack()
                lbl1 = Label(root, text="  HOW TO REACH !  ", font=('calibri', 40, 'bold'), foreground='white',
                             background="black")
                lbl1.place(x=400, y=30)
                # Button(root,text=" SEARCH ",command=func,bg="white",fg="blue",font="courier 15 bold",activebackground="green",activeforeground="black",relief=RAISED,borderwidth=15).place(x=580,y= 480)
                Button(root, text=" <<BACK ", command=func9, font="comicsansms 15 bold", bg="red", fg="white").place(
                    x=1200, y=645)
                # Button(root,text="STUDENT SERVICES",command=func,font="comicsansms 10 bold",fg="white",bg="red").place(x=1190,y=660)
                lbl2 = Label(root,
                             text="JAIPUR INTERNATIONAL AIRPORT is nearly 24km from the main city. The city is connected by air \n with all major cities of India (3 - 4 daily flights from Delhi & Mumbai). \n There are many trains that stop at the Udaipur Railway Station as well. You can reach Udaipur\n  by road (by bus, cab or car) too.",
                             font=('calibri', 18, 'bold'), foreground='black', background="white")
                lbl2.place(x=30, y=120)
                lbl4 = Label(root, text=" HOW TO REACH JAIPUR BY ROAD ", font=('calibri', 20, 'bold'),
                             foreground='white', background="black")
                lbl4.place(x=30, y=280)
                lbl41 = Label(root,
                              text="The city lies midway between Delhi and Mumbai, at the intersection of NH 8, Golden \n quadrilateral,  East west Corridor and NH 76. Road travellers can drive  down to the \n city  either from Ahmedabad through NH8 which takes approximately 5  hours or from\n  Jaipur which   is a 6-hour journey via the Golden quadrilateral. \n It's also a 4-hour drive  from Kota through the EW corridor.",
                              font=('calibri', 18, 'bold'), foreground='black', background="white")
                lbl41.place(x=30, y=330)
                lbl3 = Label(root, text="  HOW TO REACH JAIPUR BY TRAIN  ", font=('calibri', 20, 'bold'),
                             foreground='white', background="black")
                lbl3.place(x=30, y=500)
                lbl31 = Label(root,
                              text="There are two railway stations in Jaipur- Jaipur City railway station and Rana Pratap Nagar\n railway station, both well networked to most of the cities in India like Kolkata,\n  Bangalore, New Delhi, Mumbai, Jaipur, Ajmer, Kota, Agra, etc. Both the stations are\n located within a distance of 3km from the city centre.",
                              font=('calibri', 18, 'bold'), foreground='black', background="white")
                lbl31.place(x=30, y=550)

                root.mainloop()



            def func13():
                global root
                root.destroy()
                root = Tk()

                root.title("SCOUT MY INDIA")
                root.geometry("1350x800")
                root.minsize(400, 220)
                # root.iconbitmap("q.ico.ico")
                root.wm_attributes("-transparentcolor", 'blue')
                im = Image.open("bbbg1.jpg")
                im = im.resize((1370, 800))
                phot = ImageTk.PhotoImage(im)
                canvas = Canvas(root, width=1400, height=700)
                canvas.create_image(0, 0, image=phot, anchor="nw")
                canvas.pack()
                img = Image.open("HJ1.jpg")
                img = img.resize((350, 200))
                photo = ImageTk.PhotoImage(img)
                label1 = tkinter.Label(image=photo)
                label1.image = photo
                label1.place(x=30, y=140)

                img1 = Image.open("HJ2.jpg")
                img1 = img1.resize((350, 200))
                photo1 = ImageTk.PhotoImage(img1)
                label2 = tkinter.Label(image=photo1)
                label2.image = photo1
                label2.place(x=30, y=440)

                img2 = Image.open("HJ3.jpg")
                img2 = img2.resize((350, 200))
                photo2 = ImageTk.PhotoImage(img2)
                label3 = tkinter.Label(image=photo2)
                label3.image = photo2
                label3.place(x=670, y=150)

                img3 = Image.open("HJ4.jpg")
                img3 = img3.resize((350, 200))
                photo3 = ImageTk.PhotoImage(img3)
                label4 = tkinter.Label(image=photo3)
                label4.image = photo2
                label4.place(x=670, y=450)

                lbl1 = Label(root, text="   HOTELS   ", font=('calibri', 40, 'bold'), foreground='white',background="black")
                lbl1.place(x=500, y=20)
                lbl2 = Label(root, text="  Rambagh Palace ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl2.place(x=30, y=130)
                lbl21 = Label(root,text=" * Facilities: Parking , Bar , Wifi ,\n Pool , Food \n * Presented by Jaipur’s royal family, this \nhotel operates with an inventory of 78 \nsuites that originally were the \nformer prince’s chambers.",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl21.place(x=390, y=160)
                lbl3 = Label(root, text="  Hathi Mauja ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl3.place(x=30, y=430)
                lbl31 = Label(root,text=" * Facilities: Parking , Bar , Wifi \n * Surrounded by mountains and overlooking\n   the Elephant Village, this Resort Near Jaipur \nhas a beautiful and serene view of sunrises\n and sunsets. The elegantly designed rooms\n are cleaned twice a day .", font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl31.place(x=390, y=480)
                lbl4 = Label(root, text="  Jai Mahal Palace ", font=('calibri', 20, 'bold'), foreground='white',background="black")
                lbl4.place(x=670, y=130)
                lbl41 = Label(root, text="* Facilities: Parking , Bar , Wifi , Pool , Food ",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl41.place(x=1030, y=170)
                lbl5 = Label(root, text=" Hotel Grand Lotus Inn  ", font=('calibri', 20, 'bold'), foreground='white', background="black")
                lbl5.place(x=670, y=430)
                lbl5 = Label(root, text="* Facilities: Parking , Bar , Wifi , Pool , Food .",font=('calibri', 11, 'bold'), foreground='black', background="white")
                lbl5.place(x=1030, y=480)
                Button(root, text=" <<BACK ", command=func9, font="comicsansms 15 bold", bg="red", fg="white").place(x=1200, y=640)

                root.mainloop()


            def func14():
                global root
                root.destroy()

                root = Tk()

                root.title("SCOUT MY INDIA")
                root.geometry("1350x800")
                root.minsize(400, 220)
                # root.iconbitmap("q.ico.ico")
                root.wm_attributes("-transparentcolor", 'blue')
                im = Image.open("bg11.jpg")
                im = im.resize((1370, 800))
                phot = ImageTk.PhotoImage(im)
                canvas = Canvas(root, width=1400, height=700)
                canvas.create_image(0, 0, image=phot, anchor="nw")
                canvas.pack()
                img = Image.open("P1.jpg")
                img = img.resize((350, 200))
                photo = ImageTk.PhotoImage(img)
                label1 = tkinter.Label(image=photo)
                label1.image = photo
                label1.place(x=150, y=180)

                img1 = Image.open("P2.jpg")
                img1 = img1.resize((350, 200))
                photo1 = ImageTk.PhotoImage(img1)
                label2 = tkinter.Label(image=photo1)
                label2.image = photo1
                label2.place(x=480, y=180)

                img2 = Image.open("P3.jpg")
                img2 = img2.resize((350, 200))
                photo2 = ImageTk.PhotoImage(img2)
                label3 = tkinter.Label(image=photo2)
                label3.image = photo2
                label3.place(x=830, y=180)

                img3 = Image.open("P4.jpg")
                img3 = img3.resize((350, 200))
                photo3 = ImageTk.PhotoImage(img3)
                label4 = tkinter.Label(image=photo3)
                label4.image = photo2
                label4.place(x=150, y=450)

                img4 = Image.open("P5.jpg")
                img4 = img4.resize((350, 200))
                photo4 = ImageTk.PhotoImage(img4)
                label5 = tkinter.Label(image=photo4)
                label5.image = photo4
                label5.place(x=480, y=450)

                img5 = Image.open("P6.jpg")
                img5 = img5.resize((350, 200))
                photo5 = ImageTk.PhotoImage(img5)
                label6 = tkinter.Label(image=photo5)
                label6.image = photo5
                label6.place(x=830, y=450)

                lbl1 = Label(root, text="  PHOTOS  ", font=('calibri', 40, 'bold'), foreground='white', background="black")
                lbl1.place(x=540, y=30)
                Button(root, text=" <<BACK ", command=func9, font="comicsansms 15 bold", bg="red", fg="white").place(x=1200, y=645)

                root.mainloop()






            root = Tk()
            root.title("SCOUT MY INDIA")
            root.geometry("1350x800")
            root.minsize(1350, 780)
            # root.iconbitmap("q.ico.ico")
            root.wm_attributes("-transparentcolor", 'blue')
            img = Image.open("udd1.jpg")
            img = img.resize((1370, 800))
            photo = ImageTk.PhotoImage(img)
            canvas = Canvas(root, width=1400, height=700)
            canvas.create_image(0, 0, image=photo, anchor="nw")
            canvas.pack()
            lbl1 = Label(root, text="  JAIPUR  ", font=('calibri', 40, 'bold'), foreground='white', background="black")
            lbl1.place(x=500, y=30)
            Button(root, text="PLACES TO VISIT ", command=func10, bg="white", fg="blue", font="courier 20 bold",activebackground="orange", activeforeground="black", relief=RAISED, borderwidth=15).place(x=1000,
                                                                                                             y=120)
            Button(root, text=" SPECIAL FOOD ", command=func11, bg="white", fg="blue", font="courier 20 bold",activebackground="orange", activeforeground="black", relief=RAISED, borderwidth=15).place(x=1000,
                                                                                                             y=220)
            Button(root, text="HOW TO REACH ", command=func12, bg="white", fg="blue", font="courier 20 bold",activebackground="orange", activeforeground="black", relief=RAISED, borderwidth=15).place(x=1000,
                                                                                                             y=320)
            Button(root, text=" HOTELS ", command=func13, bg="white", fg="blue", font="courier 20 bold",activebackground="orange", activeforeground="black", relief=RAISED, borderwidth=15).place(x=1000,
                                                                                                             y=420)
            Button(root, text=" PHOTOS ", command=func14, bg="white", fg="blue", font="courier 20 bold",activebackground="orange", activeforeground="black", relief=RAISED, borderwidth=15).place(x=1000,
                                                                                                             y=520)

            # Button(root,text=" SEARCH ",command=func,bg="white",fg="blue",font="courier 15 bold",activebackground="green",activeforeground="black",relief=RAISED,borderwidth=15).place(x=580,y= 480)
            Button(root, text=" <<BACK ", command=func2, font="comicsansms 15 bold", bg="red", fg="white").place(x=10,y=640)

            # Button(root,text="STUDENT SERVICES",command=func,font="comicsansms 10 bold",fg="white",bg="red").place(x=1190,y=660)
            lbl2 = Label(root,text=" No trip to India is complete without spending time in Jaipur. \n Affectionately nicknamed The Pink City for the blushing color of its historic buildings, Jaipur is a princely \n wonderland of culture and heritage, brimming with architectural gems. It's also a preeminent stop in India's \n famous Golden Triangle, a popular tourist circuit.", font=('calibri', 15, 'bold'), foreground='black', background="white")
            lbl2.place(x=20, y=120)
            lbl3 = Label(root,text=" Prepare to be captivated by the grandeur of Jaipur, the capital \n of Rajasthan. City Palace gives you a taste of the lavish lifestyle afforded to the royal family of Jaipur. \n Just next door, the astronomical instruments at the Jantar Mantar observatory bring the mysteries of space down \n to Earth. And depending on the time of your visit, you may be able to experience one of \n the many festivals that fill Jaipur's annual calendar, like the International Kite\n  Festival in January or Elephant Festival in early spring.", font=('calibri', 15, 'bold'), foreground='black', background="white")
            lbl3.place(x=20, y=300)
            lbl4 = Label(root,text=" Ready to make your trip to The Paris of India a memorable \nexperience? Map out your itinerary with our guide to the top attractions and places to visit in Jaipur.",font=('calibri', 15, 'bold'), foreground='black', background="white")
            lbl4.place(x=20, y=520)

            root.mainloop()

        root = Tk()
        root.title("SCOUT MY INDIA")
        root.geometry("1350x800")
        root.minsize(1350, 780)
        # root.iconbitmap("q.ico.ico")
        root.wm_attributes("-transparentcolor", 'grey')
        img = Image.open("thr33.jpg")
        img = img.resize((1370, 800))
        photo = ImageTk.PhotoImage(img)
        canvas = Canvas(root, width=1400, height=700)
        canvas.create_image(0, 0, image=photo, anchor="nw")
        canvas.pack()
        lbl1 = Label(root, text=" ENTER YOUR DESTINATION !  ", font=('calibri', 40, 'bold'), foreground='white',
                     background="black")
        lbl1.place(x=350, y=170)
        # Button(root,text="GOVERNMENT OFFICIALS",command=func,bg="white",fg="blue",font="courier 25 bold",activebackground="orange",activeforeground="black",relief=RAISED,borderwidth=15).place(x=205,y=510)
        global strr
        strr = StringVar()
        strr.set("DESTINATION !")
        e1 = Entry(root, textvariable=strr, font="courier 25 bold", fg="green")
        def bt_cmd():
            if strr.get() == "udaipur":
                func3()
            elif strr.get() =="jaipur":
                func9()
            else :
                pass
        e1.place(x=460, y=380)
        e1.focus_force()

        Button(root, text=" SEARCH ", command=bt_cmd, bg="white", fg="blue", font="courier 15 bold",activebackground="green", activeforeground="black", relief=RAISED, borderwidth=15).place(x=580, y=480)
        Button(root, text=" <<BACK ", command=func, font="comicsansms 10 bold", bg="red", fg="white").place(x=10, y=660)
        # Button(root,text="STUDENT SERVICES",command=func,font="comicsansms 10 bold",fg="white",bg="red").place(x=1190,y=660)
        lbl2 = Label(root, font=('calibri', 25, 'bold'), foreground='black', background="white")
        lbl2.place(x=1100, y=550)
        root.mainloop()

    root = Tk()
    root.title("SCOUT MY INDIA")
    root.geometry("1350x800")
    root.minsize(900, 800)
    # root.iconbitmap("q.ico.ico")
    img = Image.open("sd222.jpg")
    img = img.resize((1370, 700))
    photo = ImageTk.PhotoImage(img)
    canvas = Canvas(root, width=1400, height=700)
    canvas.create_image(0, 0, image=photo, anchor="nw")
    canvas.pack()
    Label(root, text=" LOGIN PAGE ", bg="blue", fg="white", font="courier 30 bold", relief=RAISED).place(x=560, y=170)

    Label(root, text=" USERNAME ", bg="white", fg="black", font="courier 25 bold", relief=RAISED).place(x=320, y=270)
    Label(root, text=" PASSWORD ", bg="white", fg="black", font="courier 25 bold", relief=RAISED).place(x=320, y=360)
    Button(root, text="<<BACK", command=func,bg ="green", font="comicsansms 10 bold").place(x=5, y=650)
    strr = StringVar()
    strr2 = StringVar()

    def bt_cm():
        if strr.get() == "nikhil" and strr2.get() == "nik@123":
            func2()
        elif strr.get() == "nitesh" and strr2.get() =="nk@123":
            func2()
        else:
            func009()

    def func009():
        global root
        import tkinter.messagebox as tksmg
        tksmg.showinfo("CONFIRMATION","DETAILS ARE NOT FOUND")
        root.destroy()
    e1 = Entry(root, textvariable=strr, font="courier 25 bold", fg="green")
    e1.place(x=560, y=273)
    e1.focus_force()
    e2 = Entry(root, textvariable=strr2, font="courier 25 bold")
    e2.place(x=560, y=360)
    e2.focus_force()
    Button(root, text=" ENTER ", command=bt_cm, font="default 20 bold").place(x=610, y=473)
    # Button(root,text="SIGN UP",command=func,font="default 15 bold").place(x=720,y=473)
    root.mainloop()
def func123():
    global root
    root.destroy()


    def func09():
        global root
        import tkinter.messagebox as tksmg
        tksmg.showinfo("CONFIRMATION","DETAILS HAVE BEEN SAVED")
        root.destroy()
    root = Tk()
    root.title("SCOUT MY INDIA")
    root.geometry("1350x800")
    root.minsize(900, 800)
    # root.iconbitmap("q.ico.ico")
    img = Image.open("sd222.jpg")
    img = img.resize((1370, 700))
    photo = ImageTk.PhotoImage(img)
    canvas = Canvas(root, width=1400, height=700)
    canvas.create_image(0, 0, image=photo, anchor="nw")
    canvas.pack()
    Label(root, text=" SIGNUP PAGE ", bg="blue", fg="white", font="courier 30 bold", relief=RAISED).place(x=560, y=170)

    Label(root, text=" USERNAME ", bg="white", fg="black", font="courier 25 bold", relief=RAISED).place(x=320, y=270)
    Label(root, text=" PASSWORD ", bg="white", fg="black", font="courier 25 bold", relief=RAISED).place(x=320, y=360)
    Button(root, text="<<BACK", command=func, font="comicsansms 10 bold").place(x=5, y=650)
    strr = StringVar()
    strr2 = StringVar()
    e1 = Entry(root, textvariable=strr, font="courier 25 bold", fg="green")
    e1.place(x=560, y=273)
    e1.focus_force()
    e2 = Entry(root, textvariable=strr2, font="courier 25 bold")
    e2.place(x=560, y=360)
    e2.focus_force()
    Button(root, text=" DETAILS SAVED  ", command=func09, font="default 20 bold").place(x=610, y=473)
    # Button(root,text="SIGN UP",command=func,font="default 15 bold").place(x=720,y=473)
    root.mainloop()


root = Tk()
root.title("SCOUT MY INDIA")
root.geometry("1350x800")
root.minsize(1200, 800)
# root.iconbitmap("q.ico.ico")
img = Image.open("frnt2.jpg")
img = img.resize((1000, 700))
photo = ImageTk.PhotoImage(img)
canvas = Canvas(root, width=1400, height=700)
canvas.create_image(0, 0, image=photo, anchor="nw")
canvas.pack()

img1 = Image.open("frnt1.jpg")
img1 = img1.resize((850, 600))
photo1 = ImageTk.PhotoImage(img1)
label2 = tkinter.Label(image=photo1)
label2.image = photo1
label2.place(x=45, y=40)

Button(root, text="LOG IN ", command=func, fg="blue", font="default 20 bold", activebackground="orange",
       activeforeground="black", relief=GROOVE, borderwidth=10, bg="white").place(x=1020, y=450)
Button(root, text="SIGN UP ", command=func123, fg="blue", font="default 20 bold", activebackground="orange",
       activeforeground="black", relief=GROOVE, borderwidth=10, bg="white").place(x=1180, y=450)
lbl1 = Label(root, text="  SCOUT  ", font=('calibri', 50, 'bold'), foreground='white', background="black")
lbl1.place(x=1050, y=100)
lbl12 = Label(root, text="  MY  ", font=('calibri', 50, 'bold'), foreground='white', background="black")
lbl12.place(x=1090, y=200)
lbl13 = Label(root, text="  INDIA   ", font=('calibri', 50, 'bold'), foreground='white', background="black")
lbl13.place(x=1050, y=300)
lbl2 = Label(root, font=('calibri', 25, 'bold'), foreground='black', background="white")
lbl2.place(x=1100, y=550)
date()
lbl = Label(root, font=('calibri', 10, 'bold'), background='white', foreground='black')
lbl.place(x=1190, y=590)
time()
root.mainloop()
