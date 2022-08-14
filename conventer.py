#############################################################################################
#																			IMPORT   		#
from tkinter import *																		#
from tkinter import messagebox																#
#																							#
#############################################################################################
#                                                                          	MAIN WINDOW 	#
root = Tk()																					#
root.geometry('560x295')                                                                    #
root.resizable(width = False,																#
               height = False)																#
root.title('Конвентер')																		#
root.configure(background = '#D5DDE7')														#
root.iconbitmap('C:/Python/icon3.ico')  # Если отправлять это кому-нибудь, 					#
										# то эту строку надо удалять						#
#																							#
#############################################################################################
#																			DEF FOCUS		#
def focus_to_2(event):																		#
	Ent_two.focus_set()																		#
	transfer()																				#
#																							#
def focus_to_8(event):																		#
	Ent_eight.focus_set()																	#
	transfer()																				#
#																							#
def focus_to_16(event):																		#
	Ent_sixteen.focus_set()																	#
	transfer()																				#
def check_keys(text, action):																#
    # Не событие вставки или ни один символ в тексте не является буквой						#
    return action != '1' or not any (not char.isdigit() for char in text)					#
def check_keys_for_16(text, action):														#
	allowed = {"a","b","c", "d", "e", "f", 													#
	"A", "B", "C", "D", "E", "F", 															#
	"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}										############
	return action != '1' or not any (not char.isalnum() for char in text) and allowed.issuperset(text) #
def check_keys_for_2(text, action):																	   #
	allowed = {"1", "0"}																			   #
	return action != '1' or not any (not char.isdigit() for char in text) and allowed.issuperset(text) #
def check_keys_for_8(text, action):																	   #
	allowed = {"1", "2", "3", "4", "5", "6", "7", "0"}												   #
	return action != '1' or not any (not char.isdigit() for char in text) and allowed.issuperset(text) #
#																									   #
#####################################################################################################################
#																			2x DEF TRANSFER							#
def transfer_1(*args):																								#
	ten = Ent_ten.get()																								#
	two = Ent_two.get()																								#
	eight = Ent_eight.get()																							#
	sixteen = Ent_sixteen.get()																						#
	Label_OK_ten = Label(root, text = '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀', 				#
					   font =('Forefront', 12), 																	#
					   foreground = 'Black', 																		#
					   background = '#D5DDE7').place(x = 411, y = 70)												#
	Label_OK_two = Label(root, text = '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀', 				#
					   			font =('Forefront', 11), 															#
					   			foreground = 'Black', 																#
					   			background = '#D5DDE7').place(x = 411, y = 70)										#
	Label_OK_eight = Label(root, text = '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀', 				#
					   			   font =('Forefront', 11), 														#
					   			   foreground = 'Black', 															#
					   			   background = '#D5DDE7').place(x = 411, y = 120)									#
	Label_OK_sixteen = Label(root, text = '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀', 			#
					   				 font =('Forefront', 11), 														#
					   				 foreground = 'Black', 															#
					   				 background = '#D5DDE7').place(x = 411, y = 170)								#
#																													#
#																													#
	def all_for_ten(event=None):																					#
		try:																										#
			value_ten = abs(int(ten, 10))																			#
		except ValueError:																							#
			if ten != "":																							#
				Ent_two.delete(0, 'end')																			#
				Ent_eight.delete(0, 'end')																			#
				Ent_sixteen.delete(0, 'end')																		#
				Ent_two.insert(0, 'невозможно')																		#
				Ent_eight.insert(0, 'невозможно')																	#
				Ent_sixteen.insert(0, 'невозможно')																	#
		else:																										#
			value_ten = abs(int(ten, 10))																			#
			BVT = (str(bin(value_ten)))																				#
			OVT = (str(oct(value_ten)))																				#
			HVT = (str(hex(value_ten)))																				#
			ET = BVT[2:]																							#
			EE = OVT[2:]																							#
			ES = HVT[2:]																							#
			Ent_two.delete(0, 'end')																				#
			Ent_eight.delete(0, 'end')																				#
			Ent_sixteen.delete(0, 'end')																			#
			Ent_two.insert(0, ET)																					#
			Ent_eight.insert(0, EE)																					#
			Ent_sixteen.insert(0, ES)																				#
	all_for_ten()																									#
	def try_int_2_8_16(event=None):																					#
		try:																										#
			int(two, 2)																								#
		except ValueError:																							#
			pass 																									#
		else:																										#
			if str(int(two, 2))!=ten.lstrip('0') and int(two, 2)!=0:												#
				Label_result_two = Label(root, text = ' = ', 														#
						   				 font =('Forefront', 11), 													#
						  				 foreground = 'Black', 														#
						  				 background = '#D5DDE7')													#
				Label_result_two.place(x = 407, y = 70)																#
				Label_two_res = Label(root, text = int(two, 2), 													#
				              		  font = ('Forefront', 11),														#
			                 		  background = '#D5DDE7').place(x = 424, y = 70)								#
		try:																										#
			int(eight, 8)																							#
		except ValueError:																							#
			pass 																									#
#																													#
		else:																										#
			if str(int(eight, 8))!=ten.lstrip('0') and int(eight, 8)!=0:											#
				Label_result_eight = Label(root, text = ' = ', 														#
										   font =('Forefront', 11), 												#
										   foreground = 'Black', 													#
										   background = '#D5DDE7')													#
				Label_result_eight.place(x = 407, y = 120)															#
				Label_eight_res = Label(root, text = int(eight, 8), 												#
				              		  font = ('Forefront', 11),														#
			                 		  background = '#D5DDE7').place(x = 424, y = 120)								#
		try:																										#
			int(sixteen, 16)																						#
		except ValueError:																							#
			pass																									#
		else:																										#
			if str(int(sixteen, 16))!=ten.lstrip('0') and int(sixteen, 16)!=0:										#
				Label_result_sixteen = Label(root, text = ' = ', 													#
						  					 font =('Forefront', 11), 												#
											 foreground = 'Black', 													#
											 background = '#D5DDE7')												#
				Label_result_sixteen.place(x = 407, y = 170)														#
				Label_sixteen_res = Label(root, text = int(sixteen, 16), 											#
				              		  font = ('Forefront', 11),														#
			                 		  background = '#D5DDE7').place(x = 424, y = 170)								#
	try_int_2_8_16()																								#
#####################################################################################################################
#																													#
def transfer(event=None):																							#
	transfer_1()																									#
	transfer_1()																									#
#																													#
	ten = Ent_ten.get()																								#
	two = Ent_two.get()																								#
	eight = Ent_eight.get()																							#
	sixteen = Ent_sixteen.get()																						#
#																													#
	def pascal_devil_number_666(event=None):																		#
		messagebox.showinfo('Пасхалка!', 'Число Дьявола!')															#
	def pascal__golden_ratio_162(event=None):																		#
		messagebox.showinfo('Пасхалка!', 'Число золотого сечения!')													#
	def pascal_seven_0_everything(event=None):																		#
		messagebox.showinfo('Пасхалка!', "Семь нулей подряд, причем везде... Круто, но зачем?")						#
	def pascal_error_404(event=None):																				#
		messagebox.showwarning('Пасхалка!', "Ошибка 404!")															#
#																													#
	if ten == '666':																								#
		pascal_devil_number_666()																					#
	if two == '1' and eight == '6' and sixteen == '2':																#
		pascal__golden_ratio_162()																					#
	seven_0 = '0000000'																								#
	if two == seven_0 and eight == seven_0 and sixteen == seven_0:													#
		pascal_seven_0_everything()																					#
	if ten == '404':																								#
		pascal_error_404()																							#
#																													#
#####################################################################################################################
#																			LABELS 			#
#																							#
Label_name = Label(root, text = 'Преобразование чисел', 									#
				   font =('Bookman Old Style', 19),  										#
				   foreground = 'Crimson', 													#
				   background = '#D5DDE7', 													#
				   width = 35)																#
Label_name.place(x = -5, y = 10)															#
#																							#
#																							#
#																							#
Label_ten = Label(root, text = 'Десятичная система: ', 										#
					   font =('Forefront', 12), 											#
					   foreground = 'Black', 												#
					   background = '#D5DDE7')												#
Label_ten.place(x = 20, y = 220)															#
#																							#
#																							#
#																							#
Label_two = Label(root, text = 'Двоичная система: ', 										#
					   font =('Forefront', 12), 											#
					   foreground = 'Black', 												#
					   background = '#D5DDE7')												#
Label_two.place(x = 20, y = 70)																#
#																							#
#																							#
#																							#
Label_eight = Label(root, text = 'Восьмеричная система: ', 									#
					     font =('Forefront', 12), 											#
					     foreground = 'Black', 												#
					     background = '#D5DDE7')											#
Label_eight.place(x = 20, y = 120)															#
#																							#
#																							#
#																							#
Label_sixteen = Label(root, text = 'Шестнадцатеричная система: ', 							#
						   font =('Forefront', 12), 										#
						   foreground = 'Black', 											#
						   background = '#D5DDE7')											#
Label_sixteen.place(x = 20, y = 170)														#
#																							#
#############################################################################################
#																			 ENTRYS			#
Ent_ten = Entry(root, fg = 'black',															#
					font = ('Forefront', 11),												#
					state = 'disabled')														#
Ent_ten.place(x = 243, y = 220)																#
Ent_ten.bind('<Return>', transfer)															#
Ent_ten.config(validate = 'key',															#
			   validatecommand = (Ent_ten.register(check_keys), '%P', '%d'),				#
			   disabledbackground = 'Silver')												#
#																							#
#																							#
#																							#
Ent_two = Entry(root, fg = 'black',															#
				font = ('Forefront', 11))													#
Ent_two.focus()																				#
Ent_two.place(x = 243, y = 70)																#
Ent_two.bind('<Return>', focus_to_8)														#
Ent_two.config(validate = 'key',															#
			   validatecommand = (Ent_two.register(check_keys_for_2), '%P', '%d'))			#
#																							#
#																							#
#																							#
Ent_eight = Entry(root, fg = 'black', font = ('Forefront', 11))								#
Ent_eight.place(x = 243, y = 120)															#
Ent_eight.bind('<Return>', focus_to_16)														#
Ent_eight.config(validate = 'key',															#
			   validatecommand = (Ent_eight.register(check_keys_for_8), '%P', '%d'))		#
#																							#
#																							#
#																							#
Ent_sixteen = Entry(root, fg = 'black', font = ('Forefront', 11))							#
Ent_sixteen.place(x = 243, y = 170)															#
Ent_sixteen.bind('<Return>', focus_to_2)													#
Ent_sixteen.config(validate = 'key',														#
			   validatecommand = (Ent_sixteen.register(check_keys_for_16), '%P', '%d'))		#
#																							#
#############################################################################################
#																							#
#																			DELETE BUTTON	#
def delete(event=None):																		#
	Ent_ten.delete(0, 'end')																#
	Ent_two.delete(0, 'end')																#
	Ent_eight.delete(0, 'end')																#
	Ent_sixteen.delete(0, 'end')															#
	transfer_1()																			#
#																							#
#																							#
#																							#
#																							#
Button_delete = Button(root, text = '        🗑️',											#
					   font = (12), 														#
				  	   foreground = 'DarkViolet', 											#
				   	   activeforeground = 'OrangeRed', 										#
				   	   background = '#D5DDE7', 												#
				       width = 8,															#
				       relief = 'raised',													#
				       command = delete)													#
#																							#
Button_delete.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)								#
#																							#
#############################################################################################
#																			GO BUTTON		#
Button_go = Button(root, text = 'Преобразовать', 											#
				   font =('Arial', 12), 													#
				   foreground = 'Green', 													#
				   activeforeground = 'OrangeRed', 											#
				   background = '#D5DDE7', 													#
				   width = 52)																#
#																							#
Button_go.place(rely=1.0, relx=0, x=0, y=0, anchor=SW)										#
#																							#
Button_go.bind('<Button-1>', transfer)														#
#																							#
#############################################################################################
#																			CHECK BUTTON    #
check_state = BooleanVar(root)																#
check_state.set(0)																			#
#																							#
#																							#
def mytoggle(event = None):																	#
	val = check_state.get()																	#
	if not val:																				#
		Ent_two.focus_set()																	#
		Ent_ten.delete(0, 'end')															#
		Ent_ten.config(state = 'disabled',													#
					   disabledbackground = 'Silver')										#
		delete()																			#
	else:																					#
		Ent_ten.focus_set()																	#
		Ent_ten.config(state = 'normal')													#
		delete()																			#
#																							#
#																							#
check = Checkbutton(root,																	#
					text = 'on',															#
					font = ('Forefront', 11),												#
					variable = check_state,													#
					bg = '#D5DDE7',															#
                	fg = 'Black',															#
                	command = mytoggle)														#
check.place(x = 180, y = 220)																#
#																							#
#############################################################################################
#																			START PROG		#
root.mainloop()																				#
#																							#
#############################################################################################