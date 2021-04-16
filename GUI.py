from calculations import *
import time
import pygame, os, pyautogui
pygame.font.init()


#Adjust the width and height to the monitor size of user
WIDTH, HEIGHT = pyautogui.size()[0]//5, pyautogui.size()[1]//2

'''
#1080p monitor test
WIDTH = 384
HEIGHT = 540
'''

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Calculator')

#Fonts
BASE_FONT = pygame.font.SysFont('timesnewroman', HEIGHT//10)

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

FPS = 60

#Images




Dante2 = pygame.transform.scale(pygame.image.load(
	os.path.join('Assets', 'Dante2.jpg')), (WIDTH//3, HEIGHT//4))


#List of numbers, operators, and other that will be displayed
numbers = range(10)
operators = ['+', '-', '*', '/', '**', 'sr']
other = ['clr', 'del', '=']

#Borders
HW = WIDTH//2 #Gets half of width
HH = HEIGHT//2 #Gets half of height

INPUT_BORDER = pygame.Rect(HW - (WIDTH - HW//5)//2, 0 + HEIGHT//20, WIDTH - HW//5, HEIGHT//8)

box_list = []

def create_inputs():
	box_list.clear() #Clearing the box's list

	#positions (numbers here are the starter number)
	box_x = 0 + HW//14
	box_y = 0 + HEIGHT//5

	orignal_x = box_x #Setting a orignal number to reset X

	delta = WIDTH//5 #Make the delta change based on screen size (delta is space between each square)

	#Loop that creates the numbers
	for number in numbers:
		#Draw the Box
		box_border = pygame.Rect(box_x, box_y, WIDTH//7, WIDTH//7)
		pygame.draw.rect(WIN, BLACK, box_border, 2)

		#Add text
		number_text = BASE_FONT.render(str(number), True, BLACK)
		WIN.blit(number_text, (box_x + number_text.get_width()//2, box_y))

		#Add delta and check if the box will go past the width
		box_x += delta
		if box_x >= WIDTH:
			box_x = orignal_x
			box_y += delta

		box_list.append(box_border)

	for operator in operators:
		#Draw the Box
		box_border = pygame.Rect(box_x, box_y, WIDTH//7, WIDTH//7)
		pygame.draw.rect(WIN, BLACK, box_border, 2)

		#Add text
		number_text = BASE_FONT.render(str(operator), True, BLACK)

		index = operators.index(operator)
		if index == 0:
			WIN.blit(number_text, (box_border.x + number_text.get_width()//2.5, box_border.y - number_text.get_height()//9))
		elif index == 1:
			WIN.blit(number_text, (box_border.x + number_text.get_width(), box_border.y - number_text.get_height()//9))
		elif index == 2:
			WIN.blit(number_text, (box_border.x + number_text.get_width()//2, box_border.y + number_text.get_height()//9))
		elif index == 3:
			WIN.blit(number_text, (box_border.x + number_text.get_width() * 1.2, box_border.y - number_text.get_height()//20))
		elif index == 4:
			WIN.blit(number_text, (box_border.x + number_text.get_width()//20, box_border.y))
		else:
			WIN.blit(number_text, (box_border.x + number_text.get_width()//5, box_border.y - number_text.get_height()//10))

		#Add delta and check if the box will go past the width
		box_x += delta
		if box_x >= HW:
			box_x = orignal_x
			box_y += delta

		box_list.append(box_border)


	delta = WIDTH//3
	for item in other:
		index = other.index(item)
		#Draw the Box
		box_border = pygame.Rect(box_x, box_y, WIDTH//4, WIDTH//7)
		pygame.draw.rect(WIN, BLACK, box_border, 2)

		#Add text
		number_text = BASE_FONT.render(item, True, BLACK)

		if index == 0:
			WIN.blit(number_text, (box_border.x + number_text.get_width()//2.5, box_border.y - number_text.get_height()//9))
		elif index == 1:
			WIN.blit(number_text, (box_border.x + number_text.get_width()//4.2, box_border.y - number_text.get_height()//9))
		else:
			WIN.blit(number_text, (box_border.x + number_text.get_width(), box_border.y - number_text.get_height()//9))

		#Add delta and check if the box will go past the width
		box_x += delta
		if box_x >= WIDTH:
			box_x = orignal_x
			box_y += delta

		box_list.append(box_border)


def draw_window(input_text):
	input_text = BASE_FONT.render(input_text, True, BLACK)

	WIN.fill(WHITE)

	#Draws input border and blits the text
	pygame.draw.rect(WIN, BLACK, INPUT_BORDER, 2) 
	WIN.blit(input_text, (INPUT_BORDER.x, INPUT_BORDER.y))


	create_inputs()
	WIN.blit(Dante2, (WIDTH//1.55, HEIGHT//2.1))

	pygame.display.update()



def main():
	clock = pygame.time.Clock()
	run = True
	
	input_text = '' #creating a empty string for input text
	can_enter = True
	can_operator = True

	while run:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				break

			if event.type == pygame.MOUSEBUTTONDOWN:
				for box in box_list:
					if box.collidepoint(event.pos):
						if box_list.index(box) <= 9 and can_enter:
							input_text += str(box_list.index(box))
						elif box_list.index(box) <= 15 and can_operator:
							if box_list.index(box) == 15:
								input_text = f"sqr({input_text})"
								can_enter = False
								can_operator = False
							else:
								input_text += ' ' + str(operators[box_list.index(box) - 10]) + ' '
								can_operator = False
						elif box_list.index(box) == 16:
							input_text = ''
							can_enter = True
							can_operator = True

						elif box_list.index(box) == 17:
							input_text = input_text[:-1]
							can_enter = True
							can_operator = True

						else:
							try:
								if input_text.split(' ')[1] in operators:
									if 'sqr' in input_text:
										number = input_text[4:]
										number = number[:-1]
										number = calculation(number, 0, 'sr')
										print(number)
										if len(str(number)) >= 15:
											input_text = str(number)[:len(str(number))//2] + '...'
											print(input_text)
										else:
											input_text = str(number)
											print(input_text)
										can_enter = True
										can_operator = True

									else:
										number = calculation(input_text.split(' ')[0], input_text.split(' ')[2], input_text.split(' ')[1])
										input_text = str(number)
										can_enter = True
										can_operator = True
										if len(str(number)) >= 15:
											input_text = str(number)[:len(str(number))//2] + '...'
											print(input_text)
										else:
											input_text = str(number)

								else:
									input_text = ''
									can_enter = True
									can_operator = True
							except:
								input_text = ''
								can_enter = True
								can_operator = True
								


		draw_window(input_text)



if __name__ == '__main__':
	main()